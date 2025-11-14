🎥✨ AI Agent — Video Transcription & Summarization
Convert long videos into clean transcripts and concise AI summaries using Whisper + BART
<p align="center"> <img src="https://img.shields.io/badge/AI%20Powered-Yes-blueviolet?style=for-the-badge"/> <img src="https://img.shields.io/badge/Transcription-Whisper-green?style=for-the-badge"/> <img src="https://img.shields.io/badge/Summarization-BART-orange?style=for-the-badge"/> <img src="https://img.shields.io/badge/UI-Streamlit-red?style=for-the-badge"/> <img src="https://img.shields.io/badge/Category-ML%20Application-yellow?style=for-the-badge"/> </p>
🌟 Overview

This project is a powerful AI-driven video processing tool that automatically converts video files into:

📝 Complete text transcripts

🧠 Well-structured AI summaries

🌐 Using a simple, modern Streamlit interface

Whether you're a student, content creator, researcher, or professional, this tool saves hours by extracting insights from long videos instantly.

📸 Application Screenshot
<p align="center"> <img src="Screenshot 2025-11-14 210816.png" width="85%" alt="App Screenshot"/> </p>
🚀 Features
1️⃣ 🎬 Video-to-Audio Extraction

Uses FFmpeg to extract clean audio from MP4, MOV, AVI, MKV

Ensures high-quality input for transcription

2️⃣ 🗣️ Whisper Speech-to-Text

Powered by OpenAI Whisper

Handles multiple accents, background noise, and long videos

Produces accurate, punctuation-ready transcripts

3️⃣ ✂️ Smart Text Chunking

Automatically splits long transcripts

Avoids token overflow for summarization models

Maintains flow and context across chunks

4️⃣ 🧠 BART-Based Text Summarization

Uses Hugging Face BART

Generates clean, concise, human-like summaries

Ideal for note-taking, research, and quick understanding

5️⃣ 🌐 Modern Streamlit UI

Drag-and-drop video upload

Real-time processing indicators

Dark mode friendly interface

Zero technical knowledge required

🔄 Processing Pipeline
🎥 Video Input
      ↓
🎧 Audio Extraction (FFmpeg)
      ↓
🗣️ Speech-to-Text (Whisper)
      ↓
✂️ Text Chunking
      ↓
🧠 BART AI Summarization
      ↓
📝 Final Output (Transcript + Summary)

📁 Project Structure
AI-Agent-Transcribing-and-Summarizing-Videos/
│
├── app.py                     # Streamlit UI
├── main.py                    # Main pipeline controller
├── transcriber.py             # Whisper + audio extraction
├── summarizer.py              # BART summarization logic
├── utils.py                   # Chunking and text helpers
├── requirements.txt           # Project dependencies
├── Screenshot 2025-11-14.png  # Screenshot used in README
└── notes.txt

⚙️ Technology Stack
🤖 Machine Learning Models

Whisper (Speech-to-Text)

BART Transformer (Summarization)

PyTorch backend

🧩 Tools & Frameworks

Streamlit

FFmpeg / ffmpeg-python

Hugging Face Transformers

🖥️ Programming

Python 3.10+

🛠️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/AI-Agent-Transcribing-and-Summarizing-Videos.git
cd AI-Agent-Transcribing-and-Summarizing-Videos

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Install FFmpeg

Windows: download from ffmpeg.org

macOS: brew install ffmpeg

Linux: sudo apt install ffmpeg

▶️ Run the Application
streamlit run app.py


Your browser will open with the interface where you can upload videos for transcription and summarization.

📝 Example Summary Output

“A Data Scientist is a professional who uses data to solve business problems.
They work with large datasets, apply statistical models, machine learning,
and computational methods to derive insights and make data-driven decisions.”

🛣️ Roadmap

 Multi-language transcription

 Multi-model summarization support

 Export transcript + summary to PDF

 Time-stamped transcripts

 Cloud deployment

 UI enhancements and animations

🤝 Contributing

Pull requests are welcome!
If you have suggestions or want to add new features, feel free to open an issue.

📝 License

This project is open-source and available under the MIT License.
