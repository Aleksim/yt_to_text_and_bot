from downloader import download_audio_from_youtube
from transcriber import transcribe_audio
from post_processor import process_transcript
from assistant import ask_question_about_transcript

def main():
    # Ask the user for the YouTube URL
    youtube_url = input("Enter the YouTube video URL: ")
    
    # 1. Download the audio from YouTube
    print("Downloading audio from YouTube...")
    audio_file_path = download_audio_from_youtube(youtube_url)

    # Check if audio file was downloaded successfully
    if not audio_file_path:
        print("Failed to download audio from YouTube.")
        return
    
    # 2. Transcribe the audio file to text
    print("Transcribing audio to text...")
    transcript = transcribe_audio(audio_file_path)
    
    # Check if transcription was successful
    if not transcript:
        print("Failed to transcribe audio.")
        return
    
    # 3. Post-process the transcript
    print("Processing the transcript...")
    processed_transcript = process_transcript(transcript)

    if processed_transcript:
        # 4. Save the processed transcript to a file
        with open("final_transcript.txt", "w", encoding='utf-8') as file:
            file.write(processed_transcript)
        print("The processed transcript is saved to final_transcript.txt.")
        
        # 5. Load the processed transcript for the Q&A session
        print("\nYou can now ask questions about the video.")
        while True:
            user_question = input("\nWhat is your question? (Type 'exit' to end the Q&A session): ")
            if user_question.lower() == 'exit':
                break

            # Get the answer to the question based on the transcript
            answer = ask_question_about_transcript(processed_transcript, user_question)
            print(f"Answer:\n{answer}\n")
    else:
        print("Failed to process transcript or an error occurred.")

if __name__ == "__main__":
    main()