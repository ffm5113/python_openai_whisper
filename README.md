# Python OpenAI Whisper Speech to Text Transcription

This script provides a simple interface to transcribe audio files using the OpenAI API's speech-to-text functionality, powered by the Whisper model. The result can be returned to the console as text or VTT (WebVTT) format.

## Installation

Before using the script, make sure to install the OpenAI Python client library. You can install it using pip:

```bash
pip install openai
```

### Usage

Clone this repository:

```bash
git clone https://github.com/ffm5113/python_openai_whisper.git
```

Navigate to the project directory:

```bash
cd your_repository
```

Run the script:

```bash
python whisper_local.py
```

Follow the prompts to enter the file path of the audio file and choose the desired response format (text or vtt).

**Note:** To access the OpenAI API, you will need an API key. Please refer to the OpenAI API documentation for instructions on how to obtain and use the API key.

### Documentation

- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/audio) - Refer to the official documentation for more details on the OpenAI audio API.
- [Whisper Model Repository](https://github.com/openai/whisper) - Repository for the open source Whisper model that powers the OpenAI API.
- [Introducing Whisper](https://openai.com/index/whisper/) - Learn more about the Whisper model on the OpenAI website.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
