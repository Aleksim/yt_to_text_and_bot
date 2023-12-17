import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def ask_question_about_transcript(transcripts, question):
    # Provide instructions to the model
    system_prompt = "You are a helpful assistant. Answer the following question based on the video transcripts provided."

    # Concatenate all transcripts into a single context
    full_transcript = "\n\n".join(transcripts)  # Add some space between each transcript
    
    # Messages to establish context with the assistant 
    # Modified for multiple transcripts
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": full_transcript}
    ]

    # Include the user's question
    messages.append({"role": "user", "content": question})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",  # Replace with the correct model you have access to
            messages=messages
        )
        # Extract and return the response to the user's question
        answer = response['choices'][0]['message']['content']
        return answer.strip()  # Strip whitespace for cleaner output

    except openai.error.OpenAIError as e:
        print(f"OpenAI API error occurred: {e}")
        return "I am unable to answer the question at the moment."
    except Exception as e:
        print(f"An error occurred while answering the question: {e}")
        return "There was an issue with generating an answer."