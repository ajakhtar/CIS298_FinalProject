import streamlit as st

st.set_page_config(
    page_title="Choose Your Own Adventure",
    page_icon="📖",
    layout="centered"
)

st.title("📖 Choose Your Own Adventure")
st.write("Welcome! Your story is about to begin...")

# Placeholder start button
if st.button("Start Adventure"):
    st.info("Game logic coming soon...")