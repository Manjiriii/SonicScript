import tempfile
from gtts import gTTS

LANGUAGE_CODES = {
    "🇺🇸 English": "en",
    "🇮🇳 Hindi": "hi",
    "🇮🇳 Marathi": "mr",
    "🇫🇷 French": "fr",
    "🇩🇪 German": "de",
    "🇪🇸 Spanish": "es",
    "🇮🇹 Italian": "it",
    "🇵🇹 Portuguese": "pt",
    "🇷🇺 Russian": "ru",
    "🇯🇵 Japanese": "ja",
    "🇰🇷 Korean": "ko",
    "🇨🇳 Chinese (Simplified)": "zh-CN",
    "🇸🇦 Arabic": "ar",
    "🇮🇳 Gujarati": "gu",
    "🇮🇳 Tamil": "ta",
    "🇮🇳 Telugu": "te",
    "🇮🇳 Kannada": "kn",
    "🇮🇳 Punjabi": "pa",
    "🇮🇳 Bengali": "bn",
    "🇳🇱 Dutch": "nl"
}


def generate_speech(text, language, slow):

    base_style = (
        "padding:12px; margin-top:10px; border-radius:10px;"
        "font-size:16px; font-weight:600;"
    )

    if not text.strip():
        return None, (
            f"<div style='{base_style} background:#FEF2F2;"
            f"border:1px solid #EF4444;color:#4C1D95;'>"
            "❌ Please enter some text first."
            "</div>"
        )

    try:

        tts = gTTS(
            text=text,
            lang=LANGUAGE_CODES[language],
            slow=slow
        )

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        temp_file.close()

        tts.save(temp_file.name)

        return temp_file.name, (
            f"<div style='{base_style} background:#ECFDF5;"
            f"border:1px solid #10B981;color:#6D28D9;'>"
            "✅ Speech generated successfully!"
            "</div>"
        )

    except Exception as e:

        return None, (
            f"<div style='{base_style} background:#FEF2F2;"
            f"border:1px solid #EF4444;color:#4C1D95;'>"
            f"❌ {e}"
            "</div>"
        )