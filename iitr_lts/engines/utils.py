import google.generativeai as genai
import streamlit as st
import os

def get_gemini_response(prompt: str, temperature: float = 0.7) -> str:
    """
    Sends a prompt to Gemini Pro and returns the text response.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "Error: API Key not found. Please enter it in the sidebar."

    try:
        genai.configure(api_key=api_key)
        # using the generic alias 'gemini-flash-latest' which is safer for availability
        model = genai.GenerativeModel("gemini-flash-latest")
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(temperature=temperature)
        )
        return response.text
    except Exception as e:
        return f"Error connecting to AI: {str(e)}"
