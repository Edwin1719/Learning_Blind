# Learning_Blind

![texto del vínculo](https://i.ytimg.com/vi/cFXg1xnPeig/maxresdefault.jpg)

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green)](https://openai.com)
[![Edge TTS](https://img.shields.io/badge/Edge%20TTS-Free-orange)](https://github.com/rany2/edge-tts)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Una suite completa de herramientas de **accesibilidad digital** que convierte contenido multimodal (PDF, imágenes, texto) en **audio de alta calidad** y **texto Braille**, diseñada para personas con discapacidades visuales y auditivas.

## 🌟 Características Principales

### 📝 **Entrada Multimodal**
- **PDF a Texto**: Extracción automática de contenido de documentos PDF
- **OCR Inteligente**: Conversión de imágenes a texto usando IA (OpenAI GPT-4o)
- **Texto Directo**: Entrada manual con soporte completo de markdown
- **Descripción de Imágenes**: Generación automática de descripciones detalladas para accesibilidad

### 🔊 **Síntesis de Voz Avanzada**
- **Edge TTS (Gratuito)**: 4 voces en español de diferentes países
- **OpenAI TTS (Premium)**: Voces de alta fidelidad con control de velocidad
- **Soporte Multiidioma**: Detección automática y síntesis en 6 idiomas
- **Control de Parámetros**: Velocidad, volumen y tono personalizables

### ⠃ **Conversión a Braille**
- **Braille Estándar**: Mapeo completo de caracteres latinos y especiales
- **Soporte Multiidioma**: Acentos y caracteres especiales del español
- **Exportación**: Descarga directa de archivos .txt en Braille

### 🎨 **Interfaz Intuitiva**
- **Diseño Responsive**: Optimizado para diferentes dispositivos
- **Feedback Visual**: Indicadores de progreso y estado en tiempo real
- **Descarga Directa**: Archivos de audio (.mp3) y Braille (.txt)
- **Configuración Persistente**: Guardado automático de preferencias

## 🏗️ Arquitectura del Proyecto

```
Educa_Labs/
├── app.py                      # 📱 Aplicación básica (gTTS + PyPDF2)
├── app_optimized.py            # 🚀 Versión optimizada (Edge TTS + pypdf)
├── app_sign_language.py        # 🤟 Versión completa con OCR avanzado
├── requirements.txt            # 📦 Dependencias básicas
├── requirements_optimized.txt  # 📦 Dependencias optimizadas
├── palabras.txt               # 📚 Base de datos de 5,000 palabras
├── real_signs_db.json         # 🤟 Base de datos de señas LSE
├── crear_lista.py             # 🛠️ Utilidad para generar listas
└── README.md                  # 📖 Documentación
```

## 🚀 Instalación y Configuración

### 1. **Requisitos del Sistema**
```bash
Python 3.8+
pip (gestor de paquetes)
```

### 2. **Clonación del Repositorio**
```bash
git clone https://github.com/Edwin1719/educa-labs.git
cd educa-labs
```

### 3. **Instalación de Dependencias**

**Para la versión básica:**
```bash
pip install -r requirements.txt
```

**Para la versión optimizada (recomendada):**
```bash
pip install -r requirements_optimized.txt
```

### 4. **Configuración de OpenAI (Opcional)**
Para funciones premium de OCR y TTS:

1. Obtén tu API Key en [OpenAI Platform](https://platform.openai.com/api-keys)
2. Crea un archivo `.env`:
```bash
OPENAI_API_KEY=tu_api_key_aqui
```

**O configura directamente en la aplicación mediante la interfaz.**

### 5. **Ejecución**
```bash
# Versión básica
streamlit run app.py

# Versión optimizada (recomendada)
streamlit run app_optimized.py

# Versión completa con OCR
streamlit run app_sign_language.py
```

## 📊 Comparación de Versiones

| Característica | app.py | app_optimized.py | app_sign_language.py |
|---------------|--------|------------------|---------------------|
| **Motor TTS** | gTTS | Edge TTS + OpenAI | Edge TTS + OpenAI |
| **PDF** | PyPDF2 | pypdf (mejorado) | pypdf (mejorado) |
| **OCR** | ❌ | Básico | IA Avanzado (GPT-4o) |
| **Voces** | Básicas | 4 profesionales | 4 + 4 premium |
| **Braille** | ✅ | ✅ Mejorado | ✅ Completo |
| **API Key** | ❌ | Opcional | Recomendado |
| **Calidad Audio** | Buena | Excelente | Premium |

## 🎯 Casos de Uso

### 👁️ **Para Personas con Discapacidad Visual**
- Conversión de documentos PDF a audio narrado
- Lectura de libros digitales con voces naturales
- Conversión de imágenes con texto a audio
- Generación de material educativo en Braille

### 👂 **Para Personas con Discapacidad Auditiva**
- Transcripción visual de contenido hablado
- Conversión de audio a texto estructurado
- Descripción detallada de contenido visual

### 🏫 **Para Educadores**
- Creación rápida de material audiovisual accesible
- Conversión de apuntes a múltiples formatos
- Herramientas de inclusión educativa

### 📚 **Para Estudiantes**
- Conversión de material de estudio a audio
- Accesibilidad de documentos académicos
- Soporte para diferentes estilos de aprendizaje

## 🔧 Configuración Avanzada

### **Variables de Entorno**
```bash
# .env file
OPENAI_API_KEY=sk-...                    # API Key de OpenAI
STREAMLIT_SERVER_PORT=8501               # Puerto personalizado
STREAMLIT_SERVER_HEADLESS=true           # Modo servidor
```

### **Personalización de Voces**
```python
# En app_optimized.py o app_sign_language.py
CONFIG['edge_voices'] = {
    "es-AR-ElenaNeural": "🇦🇷 Elena (Argentina)",
    "es-CL-CatalinaNeural": "🇨🇱 Catalina (Chile)",
    # Agregar más voces según necesidad
}
```

### **Límites de Texto**
```python
CONFIG['tts_limits'] = {
    "edge": 10000,    # Caracteres gratuitos
    "openai": 4000    # Caracteres premium
}
```

## 🛠️ Solución de Problemas

### **Error: OpenAI API Key no válida**
- Verifica tu API Key en [OpenAI Platform](https://platform.openai.com/api-keys)
- Asegúrate de tener créditos disponibles
- Revisa que la key esté correctamente configurada

### **Error: Edge TTS no funciona**
- Verifica tu conexión a internet
- Reinicia la aplicación
- Actualiza edge-tts: `pip install --upgrade edge-tts`

### **Error: PDF no se puede leer**
- Verifica que el PDF no esté protegido
- Algunos PDFs escaneados requieren OCR
- Usa la función de imagen como alternativa

### **Error: Streamlit no inicia**
- Verifica la instalación: `pip install --upgrade streamlit`
- Revisa el puerto: `streamlit run app.py --server.port 8501`
- Limpia caché: `streamlit cache clear`

## 📈 Roadmap

### **v2.0 (Próximo Release)**
- [ ] Integración con más motores TTS
- [ ] Soporte para más idiomas
- [ ] API REST para integración externa
- [ ] Dashboard de analíticas de uso

### **v2.1 (Futuro)**
- [ ] Modo offline para TTS básico
- [ ] Integración con servicios de almacenamiento en la nube
- [ ] Soporte para subtítulos automáticos
- [ ] Integración con sistemas de gestión de aprendizaje (LMS)

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

### **Guidelines de Contribución**
- Sigue las convenciones de código existentes
- Agrega tests para nuevas funcionalidades
- Actualiza la documentación
- Asegúrate de que todos los tests pasen

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT** - ve el archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Autor

**Edwin Quintero Alzate**
- 📧 Email: [egqa1975@gmail.com](mailto:egqa1975@gmail.com)
- 🌐 LinkedIn: [edwinquintero0329](https://www.linkedin.com/in/edwinquintero0329/)
- 🐙 GitHub: [Edwin1719](https://github.com/Edwin1719)
- 📘 Facebook: [edwin.quinteroalzate](https://www.facebook.com/edwin.quinteroalzate)

## 🌟 Agradecimientos

- **OpenAI** por las APIs de GPT-4o y TTS
- **Microsoft** por Edge TTS gratuito
- **Streamlit** por el framework web
- **Comunidad Open Source** por las librerías utilizadas
- **Comunidad de Accesibilidad** por el feedback y sugerencias

## 📞 Soporte

¿Necesitas ayuda o tienes sugerencias?

- 📧 Contacto directo: [egqa1975@gmail.com](mailto:egqa1975@gmail.com)
- 🐛 Reporta bugs: [GitHub Issues](https://github.com/Edwin1719/educa-labs/issues)
- 💬 Discusiones: [GitHub Discussions](https://github.com/Edwin1719/educa-labs/discussions)

---

<div align="center">

**🤟 Construyendo tecnología más inclusiva, un proyecto a la vez**

[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red.svg)](https://github.com/Edwin1719)
[![Powered by Python](https://img.shields.io/badge/Powered%20by-Python-blue.svg)](https://www.python.org/)
[![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red.svg)](https://streamlit.io/)

</div>
