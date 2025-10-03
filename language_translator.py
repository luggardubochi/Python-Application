from deep_translator import GoogleTranslator
from gtts import gTTS
import streamlit as st 


#Application title
st.title("🌍 Language Translator")

#User input text
text = st.text_input("Enter text to translate:")


#Choose Target Language
target_lang = st.selectbox(
    "Choose target Language", 
    options=["fr", "es", "de", "it", "ig", "yo", "ha", "sw"], #French, Spanish, German, Italian, Igbo, Yoruba, Hausa, Swahili
    index=0
)

# Translate when text is entered
if text:
    try:
        translation = GoogleTranslator(source='auto', target=target_lang).translate(text)
        st.subheader("✅ Translated Text:")
        st.write(translation)

        # Voice Reader (Pronunciation)
        tts = gTTS(text=translation, lang=target_lang)
        audio_file = "translation_audio.mp3"
        tts.save(audio_file)

        # Play audio
        st.audio(audio_file, format="audio/mp3")

        # Optional: Download button
        with open(audio_file, "rb") as f:
            st.download_button("⬇️ Download Pronunciation", f, file_name="translation.mp3")

    except Exception as e:
        st.error(f"Translation failed: {e}")