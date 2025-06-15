import streamlit as st
from agents import run_agent
from langdetect import detect
from deep_translator import GoogleTranslator

# Streamlit UI config
st.set_page_config(page_title="Faisal's AI Doctor", layout="centered")
st.title("🏥 Faisal's AI Doctor")
st.markdown("Ask your health question below. The app will auto-detect the relevant specialist and language.")

# User input
user_query = st.text_input("💬 Enter your health-related question:")
submit = st.button("🔎 Get Response")

if submit:
    if user_query.strip() != "":
        with st.spinner("Analyzing your question and contacting the doctor..."):
            try:
                # Detect language
                detected_lang = detect(user_query)
                english_query = GoogleTranslator(source='auto', target='en').translate(user_query)

                # Run medical agent
                english_reply = run_agent(english_query)

                # Translate reply if needed
                if detected_lang != 'en':
                    translated_reply = GoogleTranslator(source='en', target=detected_lang).translate(english_reply)
                    st.success("🩺 Doctor's Response:")
                    st.markdown(f"**In {detected_lang.upper()}**: {translated_reply}")
                    st.markdown("**In English**: " + english_reply)
                else:
                    st.success("🩺 Doctor's Response:")
                    st.markdown(english_reply)

            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter your question.")
