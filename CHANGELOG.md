# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planeado para futuras versiones
- Integración con más motores TTS
- Soporte para Braille grado 2
- API REST para integraciones externas
- Modo offline para funcionalidades básicas

## [1.0.0] - 2025-08-24

### 🎉 Lanzamiento Inicial

Primera versión pública de **Educa Labs** - Generador Accesible

### ✨ Added
- **Tres aplicaciones principales**:
  - `app.py` - Versión básica con gTTS y PyPDF2
  - `app_optimized.py` - Versión mejorada con Edge TTS
  - `app_sign_language.py` - Versión completa con OpenAI OCR/TTS
  
- **Funcionalidades multimodales**:
  - Extracción de texto desde archivos PDF
  - OCR inteligente con OpenAI GPT-4o para imágenes
  - Entrada de texto directo con soporte markdown
  
- **Síntesis de voz avanzada**:
  - Edge TTS gratuito con 4 voces en español
  - OpenAI TTS premium con control de parámetros
  - Detección automática de idioma
  - Soporte para 6 idiomas principales
  
- **Conversión a Braille**:
  - Mapeo completo de caracteres latinos
  - Soporte para acentos y caracteres especiales
  - Exportación directa a archivos .txt
  
- **Interfaz de usuario**:
  - Diseño responsive y accesible
  - Configuración persistente de preferencias
  - Descarga directa de archivos generados
  - Feedback visual en tiempo real

- **Bases de datos incluidas**:
  - `palabras.txt` - 5,000 palabras frecuentes en español
  - `real_signs_db.json` - Base de datos de señas LSE (para futuro uso)

### 🛠️ Technical
- **Arquitectura modular** con separación clara de funcionalidades
- **Manejo robusto de errores** y validaciones
- **Configuración centralizada** para fácil mantenimiento
- **Soporte para variables de entorno** (.env)

### 📚 Documentation
- README.md completo con guías de instalación
- Comparativa detallada entre versiones
- Casos de uso específicos para diferentes usuarios
- Solución de problemas comunes

### 🔧 Development
- Estructura de proyecto organizada
- Dependencias optimizadas (básicas y avanzadas)
- Configuración de desarrollo lista

---

## Categorías de Cambios

Para futuras versiones, usaremos estas categorías:

- **Added** - Nuevas funcionalidades
- **Changed** - Cambios en funcionalidades existentes
- **Deprecated** - Funcionalidades que serán removidas
- **Removed** - Funcionalidades removidas
- **Fixed** - Corrección de bugs
- **Security** - Correcciones de seguridad

## Versionado

Este proyecto usa [Semantic Versioning](https://semver.org/):

- **MAJOR** (X.y.z) - Cambios incompatibles en la API
- **MINOR** (x.Y.z) - Funcionalidades nuevas compatibles hacia atrás
- **PATCH** (x.y.Z) - Correcciones de bugs compatibles

## Links de Versiones

- [Unreleased](https://github.com/Edwin1719/educa-labs/compare/v1.0.0...HEAD)
- [1.0.0](https://github.com/Edwin1719/educa-labs/releases/tag/v1.0.0)