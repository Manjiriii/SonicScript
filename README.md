# 🎤 SonicScript

<p align="center">

<img src="assets/SonicScript_Banner.png" width="100%">

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)

![Gradio](https://img.shields.io/badge/Gradio-UI-orange?style=for-the-badge)

![gTTS](https://img.shields.io/badge/gTTS-Google-green?style=for-the-badge)

![AI](https://img.shields.io/badge/Artificial%20Intelligence-Text--to--Speech-purple?style=for-the-badge)

</p>

---

## 📖 Overview

AI Text-to-Speech Generator is an interactive web application that converts written text into natural-sounding speech using Google's Text-to-Speech (gTTS) engine.

The application features a modern purple-themed interface, supports multiple languages, and allows users to instantly generate downloadable MP3 audio from text.

---

## ✨ Features

- 🎤 Natural AI Speech Generation
- 🌍 20+ Supported Languages
- ⚡ Fast Audio Generation
- 🐢 Slow Speech Mode
- 📄 Sample Text
- 🧹 Clear Input
- 📊 Live Character Counter
- 📖 Live Word Counter
- 💜 Modern Purple UI
- 📱 Responsive Design
- ⬇️ Download Generated MP3

---

## 📸 Screenshots

### Home Page

<img src="assets/screenshot1.png" width="100%">

<img src="assets/screenshot2.png" width="100%">

<img src="assets/screenshot3.png" width="100%">

---

### Text Input

<img src="assets/screenshot4.png" width="100%">

---

### Generated Audio

<img src="assets/screenshot5.png" width="100%">

---

## 🛠️ Technologies Used

SonicScript is engineered using modern, light-weight open-source Python technologies:
* **Frontend UI:** Designed natively with [Gradio](https://github.com/gradio-app/gradio) utilizing deep layout styling injections and fully custom CSS rules.
* **AI Voice Engine:** Powered by the Google Text-to-Speech API (`gTTS`) to supply highly reliable and clean multi-lingual speech models.
* **Backend Automation:** Structured with Python, handling unique identification hashing (`uuid`) to securely manage and store temporary file generations.

---

## 📂 Project Structure

```text
SonicScript/
│
├── app.py
├── tts_engine.py
├── utils.py
├── speech_app_styles.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── assets/
│   ├── banner.png
│   ├── screenshot1.png
│   ├── screenshot2.png
|   ├── screenshot3.png
|   ├── screenshot4.png
│   └── screenshot5.png
│
├── _pycache_/
└── outputs/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Text-to-Speech-Generator.git
```

Go to the project folder

```bash
cd AI-Text-to-Speech-Generator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

## 💻 Usage

1. Enter or paste text.
2. Select a language.
3. Enable Slow Speech (optional).
4. Click **Generate Speech**.
5. Listen to the generated audio.
6. Download the MP3 file.

---

## 🌐 Live Demo

🔗 **Hugging Face Space**

[PWA deployed on Hugging Face.](https://manjiri12-sonic-script.hf.space/)



---

## 🔮 Future Enhancements

- 🎙️ Multiple Voice Options
- ⚡ Faster Speech Models
- 📥 Audio History
- 🌙 Dark/Light Theme Toggle
- ☁️ Cloud Storage
- 🔊 Voice Preview
- 🎵 Background Music Support

---

## 👩‍💻 Author

**Manjiri Chavan**

Made using Python and Artificial Intelligence.
