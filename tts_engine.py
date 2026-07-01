import os
import uuid
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
    # Base padding style for the message block
    base_style = "padding: 12px; margin-top: 10px; border-radius: 10px; font-size: 16px; font-weight: 600; display: block;"
    
    # 1. Validation check if text is empty
    if not text or not text.strip():
        return None, (
            f"<div style='{base_style} background: #FEF2F2; border: 1px solid #EF4444;'>"
            f"  <span style='color: #4C1D95 !important;'>❌ Error: Please enter some text first.</span>"
            f"</div>"
        )

    try:
        # 2. Create outputs directory if it doesn't exist
        os.makedirs("outputs", exist_ok=True)
        filename = f"outputs/{uuid.uuid4().hex}.mp3"

        # 3. Generate speech using gTTS
        tts = gTTS(
            text=text,
            lang=LANGUAGE_CODES[language],
            slow=slow
        )
        tts.save(filename)

        # 4. Return BOTH the generated audio file path and the explicit text-colored success message
        return filename, (
            f"<div style='{base_style} background: #ECFDF5; border: 1px solid #10B981;'>"
            f"  <span style='color: #6D28D9 !important;'>✅ Speech generated successfully!</span>"
            f"</div>"
        )

    except Exception as e:
        
        return None, (
            f"<div style='{base_style} background: #FEF2F2; border: 1px solid #EF4444;'>"
            f"  <span style='color: #4C1D95 !important;'>❌ Error generating speech: {str(e)}</span>"
            f"</div>"
        )