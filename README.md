# Learning_Blind

![texto del vínculo](https://i.ytimg.com/vi/cFXg1xnPeig/maxresdefault.jpg)

The application converts text and PDFs into multilingual audio and Braille, facilitating access for people with visual disabilities. Ideal for creating accessible educational materials, it offers support for multiple languages, reading speed options, and downloading results in MP3 and TXT formats. Perfect to integrate into inclusion projects.


**FEATURES:**

**Setup:**
To begin, the necessary libraries are installed, including Streamlit for the web interface, PyPDF2 for PDF text extraction, gTTS for generating speech, langdetect for language identification, Mutagen for adding metadata to audio files, and st-social-media-links for social media icons.

**User Interface Design:**
The interface provides two input methods for users: uploading a PDF file or manually entering text. It is designed to be intuitive, with clear instructions and options for the user to interact with, ensuring an easy and smooth experience.

**Text Extraction and Language Detection:**
When the user uploads a PDF, the app uses PyPDF2 to extract the text from the document. The language of the text is detected using the langdetect library, ensuring the speech generation is in the correct language based on the user's input.

**Text-to-Speech Generation:**
Once the text is extracted and the language is identified, the app uses gTTS (Google Text-to-Speech) to convert the text into speech. The user can adjust the speech speed, and the generated audio is available for playback and download in MP3 format.

**Braille Conversion:**
In addition to the audio, the app converts the text into Braille using a predefined Braille map. The Braille translation is displayed on the interface and also available for download as a text file.

**Application Deployment:**
After completing the core functionality, the application is deployed on Streamlit Cloud. Users can access it online, upload PDFs or enter text manually, and use the speech and Braille conversion features without needing to install anything locally.

**Future Improvements:**
Possible future improvements include personalized voice integration, the ability to detect and ignore images in PDFs that may interfere with text extraction, handling larger audio files, and expanding language support for broader accessibility.

**TECHNOLOGIES:**

**Streamlit:**
Streamlit is used to build the interactive web application, allowing users to upload PDF files or manually enter text. It provides an easy-to-use framework for developing the user interface and handling input/output, making it ideal for rapid prototyping and deployment.

**PyPDF2:**
PyPDF2 is a Python library used for extracting text from PDF documents. In this project, it enables the app to process and retrieve readable content from uploaded PDFs, ensuring the text can be transformed into speech or Braille.

**gTTS (Google Text-to-Speech):**
gTTS is utilized to convert the extracted text or manually inputted text into speech. It provides a simple interface to generate audio files in different languages, which enhances accessibility for users who prefer auditory content.

**langdetect:**
The langdetect library is used to automatically detect the language of the extracted text. This is crucial for ensuring that the text-to-speech functionality works correctly by generating speech in the appropriate language based on user input.

**Mutagen:**
Mutagen is a library used to handle and manipulate audio metadata. In this project, it is employed to add metadata to the generated audio files, ensuring proper file management and better integration with audio players.

**st-social-media-links:**
st-social-media-links is a Streamlit component used to display social media icons on the app interface. This enhances the user experience by allowing easy access to the project's social media profiles, helping to promote and share the application.

**DOCUMENTATION**

!https://www.youtube.com/watch?v=t15kAnnBGJQ

!https://hackernoon.com/lang/es/un-tutorial-esencial-de-texto-a-voz-de-python-usando-la-biblioteca-pyttsx3
