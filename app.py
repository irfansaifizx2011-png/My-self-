import streamlit as st

# --- पेज की सेटिंग ---
st.set_page_config(page_title="इरफान की वेबसाइट", page_icon="🇮🇳", layout="centered")

# --- बैनर और स्वागत मैसेज ---
st.markdown(
    """
    <div style="background-color:#ff9933; padding:20px; border-radius:10px; text-align:center;">
        <h1 style="color:white; margin:0;">🇮🇳 भारत 🇮🇳</h1>
        <h2 style="color:white; margin:10px 0 0 0;">हैलो एवरीवन!</h2>
        <p style="color:white; font-size:18px; margin-top:10px;">
            इरफान के लिंक पर आपका स्वागत है! 👦 👦
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.success("✨ लिंक सफलतापूर्वक खुल गया है!")
