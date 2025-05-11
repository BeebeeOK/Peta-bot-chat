import streamlit as st
import random
from datetime import datetime

# Set up page config
st.set_page_config(page_title="Peta Bot", page_icon="🤖", layout="centered")

# Apply pastel background using custom HTML/CSS
pastel_css = '''
<style>
body {
    background: linear-gradient(to bottom right, #ffe0f0, #d0f0ff);
    font-family: "Segoe UI", sans-serif;
}
div.stButton > button {
    border-radius: 20px;
}
</style>
'''
st.markdown(pastel_css, unsafe_allow_html=True)

st.title("🤖 Peta Bot")
st.caption("Your soft-spoken digital buddy ✨")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "theme" not in st.session_state:
    st.session_state.theme = "Pastel"

# Theme toggle button
if st.button("🌗 Toggle Theme"):
    if st.session_state.theme == "Pastel":
        st.session_state.theme = "Night"
        st.markdown(
            '''
            <style>
            body {
                background: linear-gradient(to bottom right, #1c1c2e, #3e3e60);
                color: #f0eaff;
            }
            </style>
            ''',
            unsafe_allow_html=True,
        )
    else:
        st.session_state.theme = "Pastel"
        st.markdown(pastel_css, unsafe_allow_html=True)

# Nickname & emoji assignment
nicknames = {
    "Brae": ["Brae the Bold", "Boss Brae", "Queen Braelyn", "Soft Bean"],
    "Mum": ["Mumzilla", "Mama Bear", "Queen Mum", "Lady M"]
}
profile_icons = {
    "Brae": "💖",
    "Mum": "🌼"
}

sender = st.selectbox("Who's chatting?", ["Brae", "Mum"])
user_input = st.text_input("Type your message", "")

if st.button("Send ✉️"):
    if user_input.strip() != "":
        name = sender
        nickname = random.choice(nicknames[name])
        icon = profile_icons[name]
        timestamp = datetime.now().strftime("%H:%M")

        st.session_state.chat_history.append(
            f"{icon} **{nickname}** [{timestamp}]: {user_input.strip()}"
        )

# Display chat history
st.markdown("### 💬 Chat")
for msg in st.session_state.chat_history:
    st.markdown(msg)

# Emoji shortcut buttons
st.markdown("### ✨ Quick Reactions")
col1, col2, col3, col4 = st.columns(4)
if col1.button("😊"):
    st.session_state.chat_history.append("💖 **Peta Bot**: I'm so glad you're smiling! 😊")
if col2.button("😢"):
    st.session_state.chat_history.append("💖 **Peta Bot**: I'm here for you, always. 💕")
if col3.button("😴"):
    st.session_state.chat_history.append("💖 **Peta Bot**: Nap time is sacred. 💤")
if col4.button("👋"):
    st.session_state.chat_history.append("💖 **Peta Bot**: Waving back atcha! 👋")

# Reset chat
if st.button("🌸 Reset Vibes"):
    st.session_state.chat_history = []