from deep_translator import GoogleTranslator
import streamlit as st

# App title
st.title("🌍 Language Translator")

# User input text
text = st.text_input("Enter text to translate:")

# Choose target language
target_lang = st.selectbox(
    "Choose target language",
    options=["fr", "es", "de", "ig", "yo", "ha", "sw"],  # French, Spanish, German, Igbo, Yoruba, Hausa, Swahili
    index=0
)

# Translate when text is entered
if text:
    try:
        translation = GoogleTranslator(source='auto', target=target_lang).translate(text)
        st.subheader("✅ Translated Text:")
        st.write(translation)
    except Exception as e:
        st.error(f"Translation failed: {e}")
