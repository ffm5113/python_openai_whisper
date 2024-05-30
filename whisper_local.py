# This script transcribes audio files using the OpenAI API's speech-to-text functionality
# powered by the Whisper model. The result can be returned to console as text or vtt format.
# Before proceeding, openai python client library is required. Install with pip install openai
# File size limited to 25 MB

from openai import OpenAI
import os

def main():
    try:
        # Ask user for the file path of the audio file
        audio_file_path = input("Enter the file path of the audio file: ")

        # Remove quotation marks from the file path if present
        audio_file_path = audio_file_path.strip('\"')

        # Ask user for the desired response format (text or vtt)
        response_format = input("Enter the desired response format (text or vtt): ")

        # Check if the API key is provided as an environment variable
        api_key = os.getenv('OPENAI_API_KEY')

        # If the API key is not provided as an environment variable, ask the user to input it
        if not api_key:
            api_key = input("Enter your OpenAI API key: ")

        # Initialize OpenAI client with the provided API key
        client = OpenAI(api_key=api_key)

        # Open the audio file in binary read mode
        with open(audio_file_path, "rb") as audio_file:
            # Perform speech-to-text transcription
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format=response_format
            )

        # Print the transcription
        print("Transcription:")
        print(transcript)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
