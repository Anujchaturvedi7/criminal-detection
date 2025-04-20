import streamlit as st
import subprocess

st.set_page_config(page_title="Criminal Detection", layout="centered")
st.title("🕵️‍♂️ Criminal Detection System")

st.markdown("Click the button below to start live webcam detection.")

if st.button("🚨 Start Detection"):
    st.success("Webcam launched. Close the camera window to stop.")
    subprocess.run(["python", "live_detector.py"])
