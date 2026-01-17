import streamlit as st
from engines.utils import get_gemini_response

def render_page():
    st.header("🎭 The Polyglot Poet")
    st.markdown("Translates text into poetry, preserving rhythm and rhyme where possible.")

    col1, col2 = st.columns(2)
    
    with col1:
        source_text = st.text_area("Enter text or concepts to poeticize:", height=200, placeholder="e.g., A lonely robot looking for love in a cyberpunk city")
        target_lang = st.selectbox("Target Language", ["English", "Spanish", "French", "Italian", "Japanese", "Urdu"])
        
    with col2:
        st.write("### Poetic Structure")
        style = st.selectbox("Poetic Form", ["Free Verse", "Rhyming Couplets", "Haiku", "Sonnet", "Limerick"])
        creativity = st.slider("Creativity Level", 0.0, 1.0, 0.8)

    if st.button("Weave Magic", type="primary"):
        if not source_text:
            st.warning("Please provide inspiration (text).")
            return

        with st.spinner(f"Composing a {style} in {target_lang}..."):
            prompt = f"""
            Act as a master poet fluent in {target_lang}.
            Transform the following input text (or concept) into a {style}.
            
            Input: "{source_text}"
            
            Requirements:
            1. **Strict Form**: Adhere strictly to the rules of a {style} (e.g., syllable count for Haiku, meter for Sonnet).
            2. **Language**: The poem must be in {target_lang}.
            3. **Meaning**: Preserve the core meaning or emotion of the input.
            
            Output:
            Provide ONLY the poem, followed by a brief 1-sentence English explanation of the meaning if the target language is not English.
            """
            
            response = get_gemini_response(prompt, temperature=creativity)
            st.markdown("### 📜 Result")
            st.markdown(response)
