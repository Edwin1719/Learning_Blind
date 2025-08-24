import pypdf, tempfile, streamlit as st, edge_tts, asyncio, base64, re, os, unicodedata, io
from langdetect import detect
from openai import OpenAI
from PIL import Image
from st_social_media_links import SocialMediaIcons
from dotenv import load_dotenv

load_dotenv()

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN UNIFICADA
# ═══════════════════════════════════════════════════════════════════════════════

CONFIG = {
    'braille_chars': "abcdefghijklmnopqrstuvwxyzáéíóúüñ0123456789 .,?!¿¡;:()-\"'/@#%&*+=<>[]{}\\",
    'braille_unicode': "⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵⠷⠮⠌⠬⠾⠳⠻⠚⠁⠃⠉⠙⠑⠋⠛⠓⠊⠀⠲⠂⠦⠖⠢⠖⠆⠒⠷⠾⠤⠦⠄⠌⠈⠁⠼⠓⠨⠴⠈⠯⠐⠔⠬⠨⠅⠈⠣⠈⠜⠨⠷⠨⠾⠸⠷⠸⠾⠡",
    'languages': {"en": "en", "es": "es", "pt": "pt", "it": "it", "de": "de", "fr": "fr"},
    'edge_voices': {
        "es-CO-SalomeNeural": "🇨🇴 Salomé (Colombia, Femenina)",
        "es-CO-GonzaloNeural": "🇨🇴 Gonzalo (Colombia, Masculina)",
        "es-ES-ElviraNeural": "🇪🇸 Elvira (España, Femenina)",
        "es-MX-DaliaNeural": "🇲🇽 Dalia (México, Femenina)"
    },
    'openai_voices': {
        "alloy": "Alloy (Neutral)", "echo": "Echo (Masculina)", 
        "nova": "Nova (Femenina)", "onyx": "Onyx (Profunda)"
    },
    'tts_limits': {"edge": 10000, "openai": 4000}
}

BRAILLE_MAP = dict(zip(CONFIG['braille_chars'], CONFIG['braille_unicode']))

# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES CORE (ULTRA-COMPACTAS)
# ═══════════════════════════════════════════════════════════════════════════════

def get_api_key(): 
    return (st.session_state.get('openai_api_key') or os.getenv('OPENAI_API_KEY', '')).strip() or None

def clean_text(text):
    """Limpia markdown/texto para TTS y Braille"""
    text = re.sub(r'#{1,6}\s+(.+)', r'\1.', text)
    text = re.sub(r'\*\*([^*]+)\*\*|__([^_]+)__', r'\1\2', text)
    text = re.sub(r'\*([^*]+)\*|_([^_]+)_', r'\1\2', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'^[-*+]\s+|^\d+\.\s+', '', text, flags=re.M)
    return re.sub(r'[`|\\>#]', '', text).strip()

def to_braille(text):
    """Convierte texto a Braille estándar"""
    text = unicodedata.normalize('NFC', text)
    return ''.join(BRAILLE_MAP.get(c, '⠠' + BRAILLE_MAP.get(c.lower(), c) if c.isupper() else c) for c in text)

def split_text(text, mode="edge"):
    """División inteligente por modo TTS"""
    limit = CONFIG['tts_limits'][mode]
    if len(text) <= limit: return [text]
    
    chunks, current = [], ""
    for paragraph in text.split('\n\n'):
        if len(current) + len(paragraph) <= limit:
            current += paragraph + "\n\n"
        else:
            if current: chunks.append(current.strip())
            current = paragraph + "\n\n"
    if current: chunks.append(current.strip())
    return chunks

def detect_lang(text):
    """Detecta idioma con fallback"""
    try: return CONFIG['languages'].get(detect(text), 'en')
    except: return 'en'

# ═══════════════════════════════════════════════════════════════════════════════
# PROCESADORES UNIFICADOS
# ═══════════════════════════════════════════════════════════════════════════════

def process_pdf(file):
    """Procesador PDF unificado"""
    try:
        return "\n".join(page.extract_text() for page in pypdf.PdfReader(file).pages[:100]).strip()
    except Exception as e:
        st.error(f"Error PDF: {e}")
        return ""

def process_image(file, mode="ocr"):
    """Procesador de imágenes OpenAI Vision"""
    api_key = get_api_key()
    if not api_key: 
        st.error("🔑 Requiere API Key OpenAI")
        return ""
    
    try:
        # Codificar imagen
        img = Image.open(file).convert('RGB')
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=85)
        b64 = base64.b64encode(buffer.getvalue()).decode()
        
        # Prompt según modo
        prompt = "Extrae TODO el texto en formato markdown limpio." if mode == "ocr" else \
                 "Describe esta imagen detalladamente para accesibilidad, en markdown estructurado."
        
        # Llamada API
        response = OpenAI(api_key=api_key).chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": [{
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{b64}"}
                }]
            }, {"role": "system", "content": prompt}],
            max_tokens=1000, temperature=0.1
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Error procesando imagen: {e}")
        return ""

def generate_audio(text, mode="edge", **kwargs):
    """Generador de audio unificado"""
    try:
        if mode == "edge":
            async def _gen():
                comm = edge_tts.Communicate(text, kwargs.get('voice', 'es-CO-SalomeNeural'), 
                                          rate=kwargs.get('rate', '+0%'), volume=kwargs.get('volume', '+0%'))
                temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
                async for chunk in comm.stream():
                    if chunk["type"] == "audio": temp.write(chunk["data"])
                temp.close()
                return temp.name
            
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(_gen())
            loop.close()
            return result
            
        else:  # OpenAI TTS
            api_key = get_api_key()
            if not api_key: return None
            
            response = OpenAI(api_key=api_key).audio.speech.create(
                model="tts-1-hd", voice=kwargs.get('voice', 'nova'), 
                input=text, speed=kwargs.get('speed', 1.0)
            )
            temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            temp.write(response.content)
            temp.close()
            return temp.name
            
    except Exception as e:
        st.error(f"Error audio: {e}")
        return None

# ═══════════════════════════════════════════════════════════════════════════════
# INTERFAZ MINIMALISTA
# ═══════════════════════════════════════════════════════════════════════════════

st.image("https://img.myloview.com.br/quadros/podcast-background-recording-studio-microphone-with-audio-waveform-broadcast-radio-or-podcasting-dark-banner-with-copy-space-700-256423810.jpg")
st.title('🎯 EDUCA LABS - GENERADOR ACCESIBLE MINIMALISTA')
st.markdown("##### 🚀 Convierte PDF/Imágenes/Texto → Audio + Braille | Optimizado y Profesional")

# INPUT UNIFICADO
input_type = st.radio("📥 Entrada:", ("PDF", "Imagen", "Texto"))
text, file_name = "", "manual"

if input_type == "PDF":
    file = st.file_uploader("Archivo PDF", type="pdf")
    if file and file.size <= 10*1024*1024:
        with st.spinner("📄 Procesando PDF..."):
            text = process_pdf(file)
            file_name = file.name.split(".")[0]
            if text: st.success(f"✅ {len(text)} caracteres extraídos")

elif input_type == "Imagen":
    col1, col2 = st.columns(2)
    mode = col1.selectbox("Tipo:", ("OCR - Texto", "Descripción - Accesibilidad"))
    file = st.file_uploader("Imagen", type=["png", "jpg", "jpeg", "gif", "bmp", "webp"])
    
    if file and file.size <= 20*1024*1024:
        st.image(file, use_container_width=True)
        with st.spinner(f"🔍 Procesando con OpenAI..."):
            text = process_image(file, "ocr" if "OCR" in mode else "description")
            file_name = file.name.split(".")[0]
            if text: 
                st.success(f"✅ {len(text)} caracteres procesados")
                with st.expander("📝 Resultado", expanded=True): st.markdown(text)

else:
    text = st.text_area("✍️ Tu texto:", height=200, placeholder="Escribe aquí...")

# PROCESAMIENTO PRINCIPAL
if text and text.strip():
    st.text_area("📝 Texto final:", text, height=150)
    lang = detect_lang(text)
    st.write(f"🌍 Idioma: **{lang.upper()}**")
    
    # CONFIGURACIÓN API
    with st.expander("🔑 OpenAI API (opcional)"):
        api_input = st.text_input("API Key:", type="password", placeholder="sk-proj-...")
        if api_input: st.session_state['openai_api_key'] = api_input
        
        current_key = get_api_key()
        if current_key: st.success(f"✅ Configurada: {current_key[:8]}...{current_key[-4:]}")
    
    # AUDIO CONFIG
    audio_mode = st.radio("🎵 Audio:", ("🚀 Edge TTS (Gratis)", "🎭 OpenAI TTS"))
    
    if "Edge" in audio_mode:
        col1, col2, col3 = st.columns(3)
        voice = col1.selectbox("Voz:", CONFIG['edge_voices'].keys(), format_func=CONFIG['edge_voices'].get)
        rate = col2.selectbox("Velocidad:", ["-25%", "+0%", "+25%"], index=1)
        volume = col3.selectbox("Volumen:", ["+0%", "+25%"], index=0)
        audio_params = {'voice': voice, 'rate': rate, 'volume': volume}
        mode_key = "edge"
    else:
        col1, col2 = st.columns(2)
        voice = col1.selectbox("Voz:", CONFIG['openai_voices'].keys(), format_func=CONFIG['openai_voices'].get)
        speed = col2.slider("Velocidad:", 0.5, 2.0, 1.0)
        audio_params = {'voice': voice, 'speed': speed}
        mode_key = "openai"
    
    # GENERAR
    if st.button("🚀 GENERAR TODO", type="primary"):
        with st.spinner("Generando Audio + Braille..."):
            # Audio
            chunks = split_text(clean_text(text), mode_key)
            audio_files = []
            
            for i, chunk in enumerate(chunks):
                audio_file = generate_audio(chunk, mode_key, **audio_params)
                if audio_file: 
                    audio_files.append(audio_file)
                    st.success(f"✅ Audio {i+1}/{len(chunks)}")
            
            # Mostrar audios
            for i, audio in enumerate(audio_files):
                st.audio(audio)
                with open(audio, "rb") as f:
                    st.download_button(f"📥 Audio {i+1}", f, f"audio_{i+1}.mp3")
            
            # Braille
            braille = to_braille(text)
            st.subheader("⠃ Texto Braille")
            st.text_area("", braille, height=150)
            
            # Descarga Braille
            braille_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w', encoding='utf-8')
            braille_file.write(braille)
            braille_file.close()
            
            with open(braille_file.name, "rb") as f:
                st.download_button("📥 Descargar Braille", f, "braille.txt")

# PIE DE PÁGINA
st.markdown("""
---
**👨‍💻 Edwin Quintero Alzate** | egqa1975@gmail.com | 🚀 Versión Ultra-Minimalista
""")

SocialMediaIcons([
    "https://www.facebook.com/edwin.quinteroalzate",
    "https://www.linkedin.com/in/edwinquintero0329/",
    "https://github.com/Edwin1719"
]).render()