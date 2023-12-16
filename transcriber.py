import whisper


def transcribe_audio(file_path):
    # Load the Whisper model (use device="cuda" for GPU acceleration if available)
    model = whisper.load_model("base", device="cpu")  # Specify device according to your environment

    # Transcribe the audio file
    result = model.transcribe(file_path)
    
    # Extract the text from the transcription result
    transcript = result["text"]
    
    # Optionally, save the transcription to a file with UTF-8 encoding to support a wide range of characters
    transcript_file = f"{file_path}_transcript.txt"
    with open(transcript_file, 'w', encoding='utf-8') as f:
        f.write(transcript)
    
    print(f"Transcription complete. Transcript saved to {transcript_file}.")
    return transcript
