# 🤝 Guía de Contribuciones

¡Gracias por tu interés en contribuir a **Educa Labs**! Este proyecto busca hacer la tecnología más accesible para personas con discapacidades. Toda contribución es bienvenida.

## 🌟 Formas de Contribuir

### 🐛 **Reportar Bugs**
- Usa el template de [Bug Report](https://github.com/Edwin1719/educa-labs/issues/new?template=bug_report.md)
- Incluye pasos para reproducir el problema
- Especifica tu sistema operativo y versión de Python
- Adjunta capturas de pantalla si es posible

### 💡 **Sugerir Mejoras**
- Usa el template de [Feature Request](https://github.com/Edwin1719/educa-labs/issues/new?template=feature_request.md)
- Explica el problema que resolvería
- Describe la solución propuesta
- Considera el impacto en accesibilidad

### 🔧 **Contribuir Código**
- Fork el repositorio
- Crea una rama descriptiva (`git checkout -b feature/nueva-funcionalidad`)
- Sigue las convenciones de código
- Agrega tests si es necesario
- Actualiza la documentación

## 📋 Proceso de Desarrollo

### **1. Configuración Local**
```bash
# Clonar tu fork
git clone https://github.com/tu-usuario/educa-labs.git
cd educa-labs

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements_optimized.txt
pip install -r requirements-dev.txt
```

### **2. Ejecutar Tests**
```bash
# Ejecutar aplicaciones para verificar funcionamiento
streamlit run app.py
streamlit run app_optimized.py
streamlit run app_sign_language.py

# Verificar lint (cuando se agregue)
# flake8 .
# black --check .
```

### **3. Commit y Push**
```bash
git add .
git commit -m "feat: descripción clara del cambio"
git push origin feature/nueva-funcionalidad
```

### **4. Pull Request**
- Usa el template de PR
- Describe los cambios realizados
- Incluye screenshots/demos si aplica
- Referencia issues relacionados

## 📝 Convenciones de Código

### **Estilo Python**
- Usar **PEP 8** para formato
- Nombres de funciones en `snake_case`
- Nombres de clases en `PascalCase`
- Docstrings en español para funciones públicas

### **Commits**
Usar [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` nueva funcionalidad
- `fix:` corrección de bug
- `docs:` cambios en documentación
- `style:` formato, sin cambios de lógica
- `refactor:` refactoring de código
- `test:` agregar o corregir tests

### **Estructura de Archivos**
```
educa-labs/
├── app.py                 # Versión básica
├── app_optimized.py       # Versión optimizada  
├── app_sign_language.py   # Versión completa
├── utils/                 # Utilidades comunes
├── tests/                 # Tests unitarios
└── docs/                  # Documentación adicional
```

## 🎯 Áreas de Contribución

### **🔊 Audio y TTS**
- Mejoras en calidad de síntesis
- Soporte para más idiomas/voces
- Optimización de rendimiento

### **⠃ Braille**
- Soporte para Braille grado 2
- Mejoras en mapeo de caracteres
- Validación de conversiones

### **👁️ OCR y Visión**
- Mejoras en precisión de extracción
- Soporte para más formatos de imagen
- Procesamiento de documentos complejos

### **🌐 Accesibilidad**
- Navegación por teclado
- Soporte para lectores de pantalla
- Mejoras en contraste y usabilidad

### **📱 Interfaz Usuario**
- Diseño responsive
- Componentes reutilizables
- Experiencia de usuario mejorada

### **🧪 Testing**
- Tests unitarios
- Tests de integración
- Tests de accesibilidad

### **📖 Documentación**
- Tutoriales y guías
- Ejemplos de uso
- Traducción a otros idiomas

## ❓ Preguntas Frecuentes

### **¿Necesito experiencia en accesibilidad?**
No es obligatorio, pero es valorado. Proporcionamos recursos para aprender.

### **¿Puedo contribuir sin saber programar?**
¡Sí! Puedes ayudar con:
- Documentación y traducción
- Testing y reporte de bugs
- Diseño UI/UX
- Feedback de usuarios con discapacidades

### **¿Cómo puedo probar con lectores de pantalla?**
Recursos recomendados:
- **NVDA** (gratuito, Windows)
- **JAWS** (Windows)
- **VoiceOver** (macOS)
- **Orca** (Linux)

## 🛡️ Código de Conducta

### **Nuestros Valores**
- **Inclusión**: Bienvenidos desarrolladores de todos los niveles
- **Respeto**: Comunicación constructiva y empática
- **Accesibilidad**: Prioridad en diseño universal
- **Colaboración**: Trabajo en equipo hacia objetivos comunes

### **Comportamiento Esperado**
- Usar lenguaje inclusivo y profesional
- Ser paciente con preguntas de principiantes
- Aceptar críticas constructivas
- Enfocarse en el beneficio de la comunidad

### **Comportamiento Inaceptable**
- Lenguaje discriminatorio o ofensivo
- Ataques personales o trolling
- Spam o contenido fuera de tema
- Violación de privacidad

## 📞 Contacto

### **Mantenedor Principal**
**Edwin Quintero Alzate**
- 📧 [egqa1975@gmail.com](mailto:egqa1975@gmail.com)
- 🐙 [@Edwin1719](https://github.com/Edwin1719)
- 💼 [LinkedIn](https://www.linkedin.com/in/edwinquintero0329/)

### **Canales de Comunicación**
- **Issues**: Para bugs y feature requests
- **Discussions**: Para preguntas generales
- **Email**: Para asuntos sensibles o privados

## 🙏 Reconocimientos

Todos los contribuidores serán reconocidos en:
- Lista de contribuidores en README
- Release notes cuando aplique
- Hall of fame del proyecto

¡Gracias por hacer la tecnología más accesible para todos! 🌟

---

*Este documento está vivo y se actualiza regularmente. Sugerencias para mejorarlo son bienvenidas.*