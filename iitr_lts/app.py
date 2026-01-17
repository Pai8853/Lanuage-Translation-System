import streamlit as st
import os

# Set page config
st.set_page_config(
    page_title="Universal Translation Hub",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar - Branding & Config
st.sidebar.title("🌍 Universal Translator")
st.sidebar.markdown("---")

# API Key Input
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password", help="Get your key from Google AI Studio")
if api_key:
    os.environ["GEMINI_API_KEY"] = api_key

st.sidebar.markdown("---")

# Gateway Selection
mode = st.sidebar.radio(
    "Select Translation Mode",
    ["Empathic & Cultural", "Polyglot Poet", "Dialect/Slang Converter", "Professional/Legal"]
)

st.title(f"{mode} Gateway")

# Routing to Engines
if not api_key:
    st.warning("⚠️ Please provide a Gemini API Key in the sidebar to proceed.")
else:
    # We will import these dynamically to avoid circular issues or early loading
    if mode == "Empathic & Cultural":
        from engines import context_engine
        context_engine.render_page()
    elif mode == "Polyglot Poet":
        from engines import poetic_engine
        poetic_engine.render_page()
    elif mode == "Dialect/Slang Converter":
        from engines import dialect_engine
        dialect_engine.render_page()
    elif mode == "Professional/Legal":
         # Re-using dialect engine pattern or a new one
        from engines import dialect_engine
        st.info("Professional mode: Transforming complex jargon into simple terms.")
        dialect_engine.render_page(is_professional=True)
