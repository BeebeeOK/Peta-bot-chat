import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Set up page config
st.set_page_config(page_title="Peta Bot Live 💬", page_icon="🌼", layout="centered")

# Set up Google Sheets access
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("peta_credentials.json", scope)
client = gspread.authorize(creds)

# Open the sheet
sheet = client.open("PetaBot_ChatLog").worksheet("Chat")

# Load messages
messages = sheet.get_all_values()

# Title
st.title("🌼 Peta Bot — Real-Time Chat")
st.caption("Made for Brae & Mum 💖")

# Sender selection
sender = st.selectbox("Who's chatting?", ["Brae", "Mum"])
user_input = st.text_input("Write a message")

# Send message
if st.button("Send ✉️"):
    timestamp = datetime.now().strftime("%H:%M")
    sheet.append_row([timestamp, sender, user_input.strip()])
    st.experimental_rerun()

# Display chat log
st.markdown("### 💬 Chat Log")
for row in messages:
    if len(row) == 3:
        time, name, msg = row
        icon = "💖" if name == "Brae" else "🌼"
        st.markdown(f"{icon} **{name}** [{time}]: {msg}")

# Reset (clear) chat log
if st.button("🌸 Reset Vibes"):
    sheet.batch_clear(["A2:C1000"])  # Keep headers intact
    st.experimental_rerun()