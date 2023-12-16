import openai
import os
from dotenv import load_dotenv

load_dotenv() 
openai.api_key = os.getenv('OPENAI_API_KEY')

def process_transcript(transcript_text):
    # Define the prompt for OpenAI
    system_prompt = """
You are a helpful assistant. Correct any spelling discrepancies in the transcribed text and make the text easier to read by adding punctuation and paragraph breaks. Only use the context provided.
    """

    # Messages format for ChatCompletion
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": transcript_text}
    ]

    try:
        # Making a call to OpenAI's ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",  
            messages=messages,
            temperature=0  
        )

        # Extract the generated message content from the response
        output_message = response['choices'][0]['message']['content']

        return output_message

    except openai.error.OpenAIError as e:
        print(f"An OpenAI error occurred: {e}")
        return None
    except Exception as e:
        print(f"An error occurred while processing the transcript: {e}")
        return None