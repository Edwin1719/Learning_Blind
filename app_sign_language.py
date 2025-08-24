import pypdf, tempfile, streamlit as st, edge_tts, asyncio, base64, re, os, unicodedata, io, json, time
from langdetect import detect
from openai import OpenAI
from PIL import Image, ImageDraw, ImageFont
from st_social_media_links import SocialMediaIcons
from dotenv import load_dotenv

load_dotenv()

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN UNIFICADA (SOLO AUDIO + BRAILLE)
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
# FUNCIONES CORE
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
    """Convierte texto a Braille"""
    return ''.join(BRAILLE_MAP.get(char.lower(), char) for char in clean_text(text))

async def generate_speech_edge(text, voice):
    """Genera audio usando Edge TTS"""
    tts = edge_tts.Communicate(text, voice)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        async for chunk in tts.stream():
            if chunk["type"] == "audio":
                tmp_file.write(chunk["data"])
        return tmp_file.name

def generate_speech_openai(text, voice, api_key):
    """Genera audio usando OpenAI TTS"""
    client = OpenAI(api_key=api_key)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        response = client.audio.speech.create(model="tts-1", voice=voice, input=text)
        tmp_file.write(response.content)
        return tmp_file.name

def extract_text_from_pdf(uploaded_file):
    """Extrae texto de PDF"""
    pdf_reader = pypdf.PdfReader(uploaded_file)
    return "\n\n".join(page.extract_text() for page in pdf_reader.pages)

def extract_text_from_image(uploaded_file, api_key):
    """Extrae texto de imagen usando OpenAI Vision"""
    if not api_key:
        return None
    
    client = OpenAI(api_key=api_key)
    base64_image = base64.b64encode(uploaded_file.read()).decode()
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": "Extrae todo el texto de esta imagen de manera precisa y ordenada."},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]
        }],
        max_tokens=1000
    )
    return response.choices[0].message.content

# ═══════════════════════════════════════════════════════════════════════════════
# INTERFAZ PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════════

st.image("https://img.myloview.com.br/quadros/podcast-background-recording-studio-microphone-with-audio-waveform-broadcast-radio-or-podcasting-dark-banner-with-copy-space-700-256423810.jpg")
st.title('🤟 EDUCA LABS - GENERADOR ACCESIBLE')
st.markdown("##### 🚀 PDF/Imágenes/Texto → Audio + Braille | Tecnología de Inclusión")

# CONFIGURACIÓN INICIAL
st.sidebar.header("⚙️ Configuración")

# API Key OpenAI
api_key = st.sidebar.text_input("🔑 OpenAI API Key:", type="password", 
                               value=st.session_state.get('openai_api_key', ''))
if api_key: st.session_state.openai_api_key = api_key

# ENTRADA DE CONTENIDO
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Entrada de Contenido")
    
    input_method = st.radio("Método de entrada:", 
                           ["📝 Texto directo", "📄 Archivo PDF", "🖼️ Imagen con texto"])
    
    content_text = ""
    
    if input_method == "📝 Texto directo":
        content_text = st.text_area("Ingresa tu texto:", height=200, 
                                   placeholder="Escribe o pega tu contenido aquí...")
    
    elif input_method == "📄 Archivo PDF":
        uploaded_file = st.file_uploader("Sube tu PDF:", type="pdf")
        if uploaded_file:
            with st.spinner("📖 Extrayendo texto del PDF..."):
                content_text = extract_text_from_pdf(uploaded_file)
                st.success(f"✅ Texto extraído ({len(content_text)} caracteres)")
    
    elif input_method == "🖼️ Imagen con texto":
        if not get_api_key():
            st.error("🔑 Se requiere OpenAI API Key para OCR de imágenes")
        else:
            uploaded_file = st.file_uploader("Sube tu imagen:", type=["png", "jpg", "jpeg"])
            if uploaded_file:
                st.image(uploaded_file, caption="Imagen cargada", use_column_width=True)
                with st.spinner("👁️ Extrayendo texto de la imagen..."):
                    content_text = extract_text_from_image(uploaded_file, get_api_key())
                    if content_text:
                        st.success("✅ Texto extraído con IA")
                    else:
                        st.error("❌ Error extrayendo texto")

with col2:
    st.subheader("🎛️ Configuración de Audio")
    
    # Motor TTS
    tts_engine = st.selectbox("🔊 Motor TTS:", ["Edge TTS (Gratis)", "OpenAI TTS (Pago)"])
    
    # Configuración específica por motor
    if tts_engine == "Edge TTS (Gratis)":
        selected_voice = st.selectbox("🎤 Voz:", list(CONFIG['edge_voices'].items()), 
                                     format_func=lambda x: x[1])
        voice_id = selected_voice[0]
        char_limit = CONFIG['tts_limits']['edge']
    else:
        if not get_api_key():
            st.error("🔑 Se requiere OpenAI API Key")
            voice_id = None
        else:
            selected_voice = st.selectbox("🎤 Voz:", list(CONFIG['openai_voices'].items()),
                                         format_func=lambda x: x[1])
            voice_id = selected_voice[0]
            char_limit = CONFIG['tts_limits']['openai']

# PROCESAMIENTO PRINCIPAL
if content_text and st.button("🚀 Generar Audio + Braille", type="primary"):
    if not content_text.strip():
        st.error("❌ No hay contenido para procesar")
    else:
        # Validar longitud
        if len(content_text) > char_limit:
            st.error(f"❌ Texto muy largo. Máximo {char_limit:,} caracteres para {tts_engine}")
        else:
            # LAYOUT: RESULTADOS
            col1, col2 = st.columns(2)
            
            with col1:
                # BRAILLE
                st.subheader("⠃ Texto en Braille")
                braille_text = to_braille(content_text)
                
                st.text_area("Braille:", braille_text, height=200)
                
                # Descarga Braille
                st.download_button(
                    "📥 Descargar Braille",
                    braille_text,
                    file_name="texto_braille.txt",
                    mime="text/plain"
                )
            
            with col2:
                # AUDIO
                st.subheader("🔊 Audio Generado")
                
                if voice_id:
                    try:
                        with st.spinner("🎵 Generando audio..."):
                            if tts_engine == "Edge TTS (Gratis)":
                                audio_file = asyncio.run(generate_speech_edge(clean_text(content_text), voice_id))
                            else:
                                audio_file = generate_speech_openai(clean_text(content_text), voice_id, get_api_key())
                        
                        # Reproducir audio
                        st.audio(audio_file, format="audio/mp3")
                        
                        # Descarga audio
                        with open(audio_file, "rb") as f:
                            st.download_button(
                                "📥 Descargar Audio",
                                f,
                                file_name="audio_generado.mp3",
                                mime="audio/mp3"
                            )
                        
                        # Limpiar archivo temporal
                        os.unlink(audio_file)
                        
                    except Exception as e:
                        st.error(f"❌ Error generando audio: {str(e)}")
                else:
                    st.warning("⚠️ Configura una voz para generar audio")

# FOOTER
st.markdown("---")
st.markdown("**👨‍💻 Edwin Quintero Alzate** | egqa1975@gmail.com | 🤟 **Tecnología Inclusiva**")