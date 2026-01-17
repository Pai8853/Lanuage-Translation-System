import streamlit as st
from engines.utils import get_gemini_response

def render_page(is_professional=False):
    if is_professional:
        st.header("⚖️ Professional & Legal Simplifier")
        st.markdown("Turning complex jargon into plain, understandable language.")
        
        # Professional Mode UI
        source_text = st.text_area("Enter complex legal/medical text:", height=200, placeholder="e.g., The party of the first part hereby agrees to indemnify...")
        target_lang = st.selectbox("Target Language", ["English (Simplified)", "Spanish", "French", "German"])
        
        if st.button("Simplify & Translate", type="primary"):
            if not source_text: return
            
            with st.spinner("Simplifying..."):
                prompt = f"""
                Act as a professional legal/medical translator.
                Simplify the following text and translate it into {target_lang}.
                
                Input: "{source_text}"
                
                Requirements:
                1. **Simplify**: Remove jargon. Use "Layman terms".
                2. **Accuracy**: Do not lose the legal/medical meaning, but make it understandable to a 12-year-old.
                3. **Highlighting**: Bullet point the key takeaways if the text is long.
                """
                resp = get_gemini_response(prompt, temperature=0.3)
                st.markdown(resp)
                
    else:
        st.header("🗣️ Dialect & Slang Converter")
        st.markdown("Bridging the gap between street slang and boardrooms.")
        
        col1, col2 = st.columns(2)
        with col1:
            source_text = st.text_area("Enter text:", height=150, placeholder="e.g., Yo what's the move regarding the merger?")
            
        with col2:
            direction = st.radio("Direction", ["Slang -> Formal Business", "Formal -> Gen-Z Slang", "Regional Dialect (e.g. Scottish)"])
            if "Regional" in direction:
                 target_dialect = st.text_input("Specify Dialect", "Scottish")
            
        if st.button("Translate Dialect", type="primary"):
            if not source_text: return
            
            with st.spinner("Translating dialect..."):
                if "Regional" in direction:
                    target_style = f"heavy {target_dialect} dialect"
                elif "Slang -> Formal" in direction:
                    target_style = "Strict Formal Business English"
                else:
                    target_style = "Gen-Z Slang/Internet Speak"
                
                prompt = f"""
                Act as a linguistic expert.
                Rewrite the following text into: {target_style}.
                
                Input: "{source_text}"
                
                Output:
                Just the translated text.
                """
                resp = get_gemini_response(prompt, temperature=0.9)
                st.success(resp)
