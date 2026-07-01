import gradio as gr
from tts_engine import generate_speech
from speech_app_styles import custom_css
from utils import get_counts

# ==========================================================
# Helper Functions
# ==========================================================

MAX_CHARACTERS = 5000


def load_sample():
    sample_text = (
        "Hello! Welcome to the AI Text-to-Speech Generator.\n\n"
        "This application converts text into natural-sounding speech "
        "using Google's Text-to-Speech technology."
    )

    return (
        sample_text,
        f"<div class='counter'>📝 Characters: {len(sample_text)} / {MAX_CHARACTERS}</div>",
        f"<div class='counter'>📖 Words: {len(sample_text.split())}</div>",
    )


def clear_all():
    return (
        "",
        f"<div class='counter'>📝 Characters: 0 / {MAX_CHARACTERS}</div>",
        "<div class='counter'>📖 Words: 0</div>",
        None,
        "<div style='display:none;'></div>" # Clean hidden structural reset
    )


# ==========================================================
# Supported Languages
# ==========================================================

LANGUAGES = [
    "🇺🇸 English",
    "🇮🇳 Hindi",
    "🇮🇳 Marathi",
    "🇫🇷 French",
    "🇩🇪 German",
    "🇪🇸 Spanish",
    "🇮🇹 Italian",
    "🇵🇹 Portuguese",
    "🇷🇺 Russian",
    "🇯🇵 Japanese",
    "🇰🇷 Korean",
    "🇨🇳 Chinese (Simplified)",
    "🇸🇦 Arabic",
    "🇮🇳 Gujarati",
    "🇮🇳 Tamil",
    "🇮🇳 Telugu",
    "🇮🇳 Kannada",
    "🇮🇳 Punjabi",
    "🇮🇳 Bengali",
    "🇳🇱 Dutch",
]


# ==========================================================
# UI Configuration (CSS Injected directly into Blocks for Gradio 6)
# ==========================================================

with gr.Blocks(
    title="SonicScript - AI Text-to-Speech",
    css=custom_css  
    
) as demo:

    # ------------------------------------------------------
    # Hero
    # ------------------------------------------------------

    gr.HTML(
        """
        <div class="hero">
            <h1>🎤 SonicScript</h1>
            <p>
                Convert text into natural-sounding speech
                using Google's pre-trained Text-to-Speech model.
            </p>
        </div>
        """
    )

    # ------------------------------------------------------
    # Main Dashboard
    # ------------------------------------------------------

    with gr.Row(equal_height=True):

        # ==================================================
        # LEFT PANEL
        # ==================================================

        with gr.Column(scale=2, elem_classes="card"):

            text = gr.Textbox(
                label="📝 Enter Text",
                placeholder="Type or paste your text here...",
                lines=10,
                max_lines=15,
                max_length=5000,
            )

            with gr.Row():

                characters = gr.HTML(
                    f"<div class='counter'>📝 Characters: 0 / {MAX_CHARACTERS}</div>"
                )

                words = gr.HTML(
                    "<div class='counter'>📖 Words: 0</div>"
                )

            language = gr.Dropdown(
                choices=LANGUAGES,
                value="🇺🇸 English",
                label="🌍 Select Language",
            )

            slow = gr.Checkbox(
                label="🐢 Slow Speech",
                value=False,
            )

            with gr.Row():

                sample = gr.Button(
                    "📄 Sample Text",
                    variant="secondary"
                )

                clear = gr.Button(
                    "🧹 Clear",
                    variant="secondary"
                )

            generate = gr.Button(
                "🎤 Generate Speech",
                variant="primary",
                size="lg"
            )

            # Initializing with an empty structure to prevent browser layout issues
            status = gr.HTML("<div></div>") 

        # ==================================================
        # RIGHT PANEL
        # ==================================================

        with gr.Column(scale=1, elem_classes="side-card"):

            gr.HTML(
                """
                <div class="side-panel">
                    <h2>🌍 Supported Languages</h2>
                    <div class="chip-container">
                        <span class="chip">🇺🇸 English</span>
                        <span class="chip">🇮🇳 Hindi</span>
                        <span class="chip">🇮🇳 Marathi</span>
                        <span class="chip">🇫🇷 French</span>
                        <span class="chip">🇩🇪 German</span>
                        <span class="chip">🇪🇸 Spanish</span>
                        <span class="chip">🇮🇹 Italian</span>
                        <span class="chip">🇵🇹 Portuguese</span>
                        <span class="chip">🇷🇺 Russian</span>
                        <span class="chip">🇯🇵 Japanese</span>
                        <span class="chip">🇰🇷 Korean</span>
                        <span class="chip">🇨🇳 Chinese</span>
                        <span class="chip">🇸🇦 Arabic</span>
                        <span class="chip">🇮🇳 Gujarati</span>
                        <span class="chip">🇮🇳 Tamil</span>
                        <span class="chip">🇮🇳 Telugu</span>
                        <span class="chip">🇮🇳 Kannada</span>
                        <span class="chip">🇮🇳 Punjabi</span>
                        <span class="chip">🇮🇳 Bengali</span>
                        <span class="chip">🇳🇱 Dutch</span>
                    </div>
                    <hr>
                    <h2>✨ Features</h2>
                    <ul class="feature-list">
                        <li>🎤 Natural AI Voice</li>
                        <li>🌍 20+ Languages</li>
                        <li>⚡ Fast Speech Generation</li>
                        <li>⬇️ Download MP3</li>
                        <li>🐢 Slow Speech Mode</li>
                        <li>📱 Responsive Design</li>
                    </ul>
                </div>
                """
            )

    # ------------------------------------------------------
    # Audio Section
    # ------------------------------------------------------

    audio = gr.Audio(
        label="🔊 Generated Audio",
        type="filepath",
    )

    # ------------------------------------------------------
    # Footer
    # ------------------------------------------------------

    gr.HTML(
        """
        <div class="footer">
        </div>
        """
    )

    # ==========================================================
    # Live Character & Word Counter
    # ==========================================================

    text.input(
        fn=get_counts,
        inputs=text,
        outputs=[
            characters,
            words
        ]
    )

    text.change(
        fn=get_counts,
        inputs=text,
        outputs=[
            characters,
            words
        ]
    )

    # ==========================================================
    # Sample Text Button
    # ==========================================================

    sample.click(
        fn=load_sample,
        inputs=[],
        outputs=[
            text,
            characters,
            words
        ]
    )

    # ==========================================================
    # Clear Button
    # ==========================================================

    clear.click(
        fn=clear_all,
        inputs=[],
        outputs=[
            text,
            characters,
            words,
            audio,
            status
        ]
    )

    # ==========================================================
    # Generate Speech
    # ==========================================================

    generate.click(
        fn=generate_speech,
        inputs=[
            text,
            language,
            slow
        ],
        outputs=[
            audio,
            status
        ]
    )


# ==========================================================
# Launch App
# ==========================================================
if __name__ == "__main__":
    demo.launch()  