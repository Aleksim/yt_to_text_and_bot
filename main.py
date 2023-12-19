from downloader import download_audio_from_youtube
from transcriber import transcribe_audio
from post_processor import process_transcript
from assistant import ask_question_about_transcript
import os

def main():
    transcripts = []  # List to accumulate transcripts
    
    while True:
        context_length = sum(len(transcript.split()) for transcript in transcripts)
        context_length_msg = f"(FYI: current context length: {context_length} words)"
        action = input(f"Would you like to add a transcript, ask a question, or exit? (type 'add', 'ask' or 'exit'). {context_length_msg}").lower()

        if action == "add":
            youtube_url = input("\nEnter the YouTube video URL: ")
            audio_file_path = download_audio_from_youtube(youtube_url)

            if not audio_file_path:
                print("Failed to download audio from YouTube.")
                continue

            print("Transcribing audio to text...")
            transcript = transcribe_audio(audio_file_path)
            if not transcript:
                print("Failed to transcribe audio.")
                continue

            print("Processing the transcript...")
            processed_transcript = process_transcript(transcript)
            if processed_transcript:
                # Extract the name from the audio file path to be used as a title
                # We ensure we remove '_transcript.txt' correctly here
                title_without_extension = os.path.splitext(os.path.basename(audio_file_path))[0]
                transcript_title = title_without_extension.replace('_transcript', '')

                # Save the processed transcript to a text file named after the title
                cleaned_transcript_path = f"{transcript_title}_cleaned.txt"
                with open(cleaned_transcript_path, "w", encoding='utf-8') as file:
                    file.write(processed_transcript)
                print(f"Processed transcript saved to {cleaned_transcript_path}")

                # Append the title and the processed transcript to the transcripts list
                transcripts.append(f"Title: {transcript_title}\n\n{processed_transcript}")
                print(f"Added transcript '{transcript_title}' to the context.")

        elif action == "ask":
            if transcripts:
                context = "\n".join(transcripts)
                user_question = input("\nWhat is your question about the transcript(s)? ")
                answer = ask_question_about_transcript(context, user_question)
                print(f"\nAnswer: {answer}\n{context_length_msg}")
            else:
                print("Please add at least one transcript before asking questions.")

        elif action == "exit":
            print("\nExiting the program.")
            break

        else:
            print("\nInvalid input. Please enter 'add', 'ask', or 'exit'.")

if __name__ == "__main__":
    main()