import streamlit as st
import os
from main import video_to_summary

def main():
    st.title("Video Summarizer AI")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        with open("uploaded_video.mp4", "wb") as f:
            f.write(uploaded_file.read())

        st.write("Transcribing and summarizing. This may take a few moments...")

        # Run the pipeline
        summary_result = video_to_summary(
            video_path="uploaded_video.mp4",
            model_size="base",     # Whisper model
            summarizer_model_name="facebook/bart-large-cnn",
            use_chunking=True      # Set True if you expect longer transcripts
        )

        # Display the final summary
        st.subheader("Summary")
        st.write(summary_result)

        # Clean up the temporary video file if you like
        if os.path.exists("uploaded_video.mp4"):
            os.remove("uploaded_video.mp4")

if __name__ == "__main__":
    main()