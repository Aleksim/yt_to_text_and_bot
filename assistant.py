import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def ask_question_about_transcript(transcript, question):
    # Provide instructions to the model
    system_prompt = "You are a helpful assistant. Your mission is to use the following transcript of a video to answer accurately questions related to it."

    # Messages to establish context with the assistant
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": transcript}
    ]

    # Include the user's question
    messages.append({"role": "user", "content": question})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",  
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

# Example usage (for testing purposes, not to be included in production code)
if __name__ == "__main__":
    sample_transcript = "This is a sample transcript text."
    sample_question = "What is discussed in the transcript?"
    print(ask_question_about_transcript(sample_transcript, sample_question))