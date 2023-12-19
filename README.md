# YouTube Transcript-Based Q&A Bot

This project allows users to input a YouTube URL, downloads the video audio, generates a transcript, and then enables the user to ask questions about the content of the transcript using OpenAI's GPT model. User can ask questions from a single video or then add another videos to the same context.

## Features

- **YouTube Audio Download:** Extracts audio from YouTube videos.
- **Audio Transcription:** Converts audio content to text using OpenAI's Whisper model.
- **Text Post-Processing:** Cleans up the transcript and corrects grammar.
- **Q&A Interaction:** Engages in a question-and-answer session about the video(s) based on the transcript.

## Getting Started

These instructions will guide you on how to set up and run the project on your local machine.

### Prerequisites

- Python 3.6 or higher
- OpenAI API key
- Python packages: `openai`, `pytube`, `python-dotenv`, `whisper`

### Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/Aleksim/yt_to_text_and_bot.git
cd yt_to_text_and_bot
```

Install the required packages:

```sh
pip install -r requirements.txt
```

Create a `.env` file at the root of your project and add your OpenAI API key:

```env
OPENAI_API_KEY=your-api-key
```

### Usage

Run the main script to start the process:

```sh
python main.py
```
Follow the prompt to input the YouTube URL and proceed with the transcription and Q&A session.
