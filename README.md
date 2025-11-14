AI Agent for Transcribing and Summarizing Videos 🎥🧠

This project is a complete AI-powered system designed to convert videos into accurate text transcripts and concise summaries. It automates the entire pipeline — from video processing to transcription and summarization — through a beginner-friendly Streamlit interface. The goal is to make long videos easy to understand, study, and review.

⭐ Features
1. Video-to-Audio Extraction

Uses FFmpeg to extract audio from videos (MP4, MOV, AVI, MKV).

Ensures clean, high-quality audio for better transcription accuracy.

2. Speech-to-Text Transcription (Whisper)

Utilizes OpenAI Whisper, a powerful ASR model.

Works for long videos, noisy audio, and multiple accents.

Produces clean, accurate transcripts without needing any API.

3. Smart Text Chunking

Long transcripts are automatically split into smaller chunks.

Prevents token overflow during summarization.

Maintains coherence and context across large content.

4. AI-Based Text Summarization

Uses Hugging Face BART model to create structured, meaningful summaries.

Summaries capture key ideas for quick understanding.

5. Streamlit User Interface

Simple web app for uploading videos and viewing results.

No programming knowledge required.

Clean, fast, and easy to use.

📁 Project Structure
AI-Agent-Transcribing-and-Summarizing-Videos/
│
├── app.py               # Streamlit interface
├── main.py              # Full pipeline: audio → transcript → summary
├── transcriber.py       # FFmpeg + Whisper transcription logic
├── summarizer.py        # BART summarization logic
├── utils.py             # Chunking + helper functions
├── example_video.mp4    # (Optional) Sample video
└── notes.txt            # Notes / references

🛠️ Technologies Used

Python 3.10+

FFmpeg / ffmpeg-python

OpenAI Whisper

Hugging Face Transformers (BART)

PyTorch

Streamlit

🚀 How It Works (Pipeline)

User uploads a video in Streamlit.

Video audio is extracted using FFmpeg.

Whisper transcribes the audio into text.

The transcript is chunked for long-form processing.

BART generates a final summary.

Both transcript and summary are displayed in the UI.

🎯 Use Cases

Lecture summarization

YouTube video notes

Podcasts and interviews

Meeting transcription

Research and content repurposing

Academic writing and study support

📦 Installation
1. Clone the repository
git clone https://github.com/your-username/AI-Agent-Transcribing-and-Summarizing-Videos.git
cd AI-Agent-Transcribing-and-Summarizing-Videos

2. Install dependencies
pip install -r requirements.txt

3. Install FFmpeg

Make sure FFmpeg is installed and added to PATH:

Windows: download from ffmpeg.org

macOS (Homebrew): brew install ffmpeg

Linux (apt): sudo apt install ffmpeg

▶️ Run the Application
streamlit run app.py


Your browser will open with the interface where you can upload videos.

📌 Future Improvements

Add timestamps in transcripts

Support multiple summarization models

Multi-language transcription

Export summary as PDF

Add progress indicators

🤝 Contributing

Pull requests are welcome!
If you’d like to suggest improvements or report issues, please open an issue in the repository.

📄 License

This project is open-source and available under the MIT License.
