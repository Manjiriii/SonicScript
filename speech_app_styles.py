custom_css = """
/* ==========================================================================
   Gradio 6 Theme & Background Overrides
   ========================================================================== */

.gradio-container,
.gradio-container-6-19-0,
div[data-testid="trigger-button"] {
    background: #F8F5FF !important;
    background-color: #F8F5FF !important;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif !important;
}

/* ==========================================================================
   Hero Header Section
   ========================================================================== */

.hero {
    background: linear-gradient(135deg, #7C3AED, #A855F7, #EC4899) !important;
    color: white !important;
    border-radius: 22px !important;
    padding: 35px !important;
    text-align: center !important;
    margin-bottom: 20px !important;
    box-shadow: 0 10px 25px rgba(124, 58, 237, 0.25) !important;
}

.hero h1 {
    font-size: 38px !important;
    margin-bottom: 8px !important;
    color: white !important;
}

.hero p {
    font-size: 18px !important;
    opacity: .95 !important;
    color: #F3E8FF !important;
}

/* ==========================================================================
   Cards & Layout Panels
   ========================================================================== */

.card,
.side-card,
.languages,
.gradio-block,
.type-row {
    background: white !important;
    background-color: white !important;
    border-radius: 20px !important;
    padding: 25px !important;
    box-shadow: 0 5px 18px rgba(124, 58, 237, 0.06) !important;
    border: none !important;
}

.side-panel h2,
.languages h3 {
    color: #7C3AED !important;
    margin-bottom: 15px !important;
    font-weight: 700 !important;
}

/* ==========================================================================
   Interactive Buttons
   ========================================================================== */

button,
.gr-button {
    border-radius: 12px !important;
    transition: all 0.3s ease !important;
}

button:hover,
.gr-button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 15px rgba(124, 58, 237, 0.2) !important;
}

/* ==========================================================================
   Language Chips & Feature Lists
   ========================================================================== */

.chip-container {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 12px !important;
    justify-content: center !important;
}

.chip {
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    background: #F3E8FF !important;
    background-color: #F3E8FF !important;
    color: #6D28D9 !important;
    padding: 10px 18px !important;
    border-radius: 25px !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    border: 1px solid #D8B4FE !important;
    opacity: 1 !important;
    visibility: visible !important;
    transition: all 0.3s ease !important;
    cursor: default !important;
}

.chip:hover {
    background: linear-gradient(135deg, #7C3AED, #EC4899) !important;
    color: white !important;
    transform: translateY(-3px) scale(1.03) !important;
    box-shadow: 0 8px 20px rgba(124, 58, 237, 0.3) !important;
    border-color: transparent !important;
}

.feature-list {
    list-style: none !important;
    padding: 0 !important;
}

.feature-list li {
    background: #F3E8FF !important;
    margin: 10px 0 !important;
    padding: 12px !important;
    border-radius: 12px !important;
    color: #4C1D95 !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.feature-list li:hover {
    background: #7C3AED !important;
    color: white !important;
}

/* ==========================================================================
   Counters & Footer
   ========================================================================== */

.counter {
    color: #7C3AED !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    padding: 5px 0 !important;
}

hr {
    margin: 25px 0 !important;
    border: 0 !important;
    border-top: 1px solid #E9D5FF !important;
}

.footer {
    text-align: center !important;
    color: #6b7280 !important;
    margin-top: 25px !important;
    font-size: 14px !important;
}

/* ==========================================================================
   Status Notifications
   ========================================================================== */

.status-message {
    padding: 12px !important;
    margin-top: 10px !important;
    border-radius: 10px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    display: block !important;
}

.success {
    background: #ECFDF5 !important;
    color: #6D28D9 !important;
    border: 1px solid #10B981 !important;
}

.error {
    background: #FEF2F2 !important;
    color: #4C1D95 !important;
    border: 1px solid #EF4444 !important;
}
"""