import streamlit as st
from engines.utils import get_gemini_response

def render_page():
    st.header("❤️ Empathic & Cultural Translator")
    st.markdown("Translates meaning, not just words. Detects emotion and provides cultural context.")

    col1, col2 = st.columns(2)
    
    with col1:
        source_text = st.text_area("Enter text to translate:", height=200, placeholder="e.g., Break a leg!")
        target_lang = st.selectbox("Target Language", ["English", "Spanish", "French", "German", "Hindi", "Japanese"])
        
    with col2:
        st.write("### Settings")
        tone = st.select_slider("Target Tone", options=["Formal", "Neutral", "Warm", "Excited", "Empathetic"], value="Neutral")
        include_culture = st.checkbox("Show Cultural Notes", value=True)

    if st.button("Translate with Empathy", type="primary"):
        if not source_text:
            st.warning("Please enter some text.")
            return

        with st.spinner("Analyzing emotion and culture..."):
            # Construct Prompt
            prompt = f"""
            Act as an expert linguist and cultural consultant. 
            Translate the following text into {target_lang}.
            
            Source Text: "{source_text}"
            Desired Tone: {tone}
            
            Requirements:
            1. **Emotion Analysis**: Briefly state the detected emotion of the source.
            2. **Translation**: Provide a translation that perfectly captures the desired tone and emotional nuance.
            3. **Cultural Notes**: If there are idioms, slang, or cultural references, explain how they were adapted for the {target_lang} culture. If none, state "No specific cultural adaptations needed."
            
            Output Format:
            **Emotion Detected**: [Emotion]
            
            **Translation**: 
            [Translated Text]
            
            **Cultural Context**:
            [Notes]
            """
            
            response = get_gemini_response(prompt)
            st.markdown(response)
