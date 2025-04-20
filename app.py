import streamlit as st
import cv2
import numpy as np
import time

def main():
    st.title("Missing Person Finder - Live Camera Feed")

    # Start video capture
    video_capture = cv2.VideoCapture(0)

    # Create a placeholder for the video stream
    frame_placeholder = st.empty()

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        
        if not ret:
            st.error("Failed to capture video.")
            break
        
        # Process the frame (optional - can add face detection or processing here)
        # For demonstration, we will just convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the resulting frame
        frame_placeholder.image(frame_rgb, channels="RGB")

        # Allow Streamlit to refresh and update the frame
        time.sleep(0.01)

    # Release video capture when done
    video_capture.release()

if __name__ == "__main__":
    main()