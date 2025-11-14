# transcriber.py
import subprocess
import whisper
import os
import shutil

def extract_audio(video_path: str, audio_path: str = "temp_audio.wav") -> str:
    """
    Extracts the audio track from `video_path` and writes it to `audio_path`
    using ffmpeg. Raises RuntimeError with a helpful message if ffmpeg is not
    found or extraction fails.
    """
    # Ensure ffmpeg is available
    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "ffmpeg not found on PATH. Please install ffmpeg and ensure it's available in your PATH. "
            "E.g., `conda install -c conda-forge ffmpeg` or download from https://ffmpeg.org/."
        )

    # If a previous audio file exists, remove it
    if os.path.exists(audio_path):
        try:
            os.remove(audio_path)
        except Exception as e:
            raise RuntimeError(f"Could not remove existing audio file {audio_path}: {e}")

    # Build the ffmpeg command correctly (list elements must be separate)
    command = [
        "ffmpeg",
        "-y",            # overwrite output if exists
        "-i", video_path,
        "-vn",           # no video
        "-acodec", "pcm_s16le",
        "-ac", "1",
        "-ar", "16000",
        audio_path
    ]

    try:
        # Run ffmpeg and capture stderr only for debugging purposes
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        stderr = e.stderr.decode() if e.stderr else str(e)
        raise RuntimeError(f"ffmpeg failed to extract audio:\n{stderr}") from e

    if not os.path.exists(audio_path):
        raise RuntimeError(f"ffmpeg command completed but {audio_path} not found.")

    return audio_path


def transcribe_audio(audio_path: str, model_size: str = "base") -> str:
    """
    Loads whisper model and transcribes the given audio file.
    """
    if not os.path.exists(audio_path):
        raise RuntimeError(f"Audio file not found: {audio_path}")

    # Load whisper model (this may take time)
    model = whisper.load_model(model_size)

    # transcribe returns a dict with "text"
    result = model.transcribe(audio_path)
    transcript = result.get("text", "")
    return transcript
