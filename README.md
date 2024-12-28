# Voice Assistant

This project is a Python-based speech recognition and text-to-speech assistant that listens to user voice commands, processes them using OpenAI's Gemini model (or another supported model), and responds with short answers. It also supports logging and clearing text files.

## Tech Stack

- **Python**: The primary programming language used.
- **SpeechRecognition**: For converting speech to text.
- **pyttsx3**: For text-to-speech conversion.
- **OpenAI (Gemini)**: For generating AI responses based on voice input.
- **Google's Speech Recognition API**: For converting speech input to text.
- **File I/O**: To save and clear text outputs in a log file.

## Requirements

- Python 3.x
- Libraries:
  - `speechrecognition` (for speech-to-text functionality)
  - `pyttsx3` (for text-to-speech conversion)
  - `openai` (for AI query generation)
  - `google-cloud-speech` (for speech-to-text API access)


# Setup

1. Install Python 3.x , portaudio and pyaudio on your system if not already installed.
2. Install the required Python libraries:

    ```bash
    pip install SpeechRecognition pyttsx3 openai google-cloud-speech
    ```

3. Set up your Gemini API key:
   - Create an account at [OpenAI](https://ai.google.dev/gemini-api/docs/api-key).
   - Get your API key and insert it in the code where the `client = OpenAI(api_key="your-api-key")` is defined.

# Usage

1. Run the script. The assistant will greet you with a voice message.
2. Speak commands or questions. The assistant will convert your speech to text and respond with a concise answer from the AI model.
3. Commands:
   - **Exit**: Say `quit`, `exit`, `bye`, `abort`, etc. to stop the program.
   - **Clear Log**: Say `clear`, `clean`, or any similar command to clear the log file (`output.txt`).
   - **General Queries**: Ask any question or make a command and the assistant will respond based on the AI model's answer.

### Example Interaction:

1. The assistant says: _"Hello there, start speaking to test"_
2. User speaks: _"What is the capital of France?"_
3. The assistant responds with: _"The capital of France is Paris."_
4. User can say `quit` or `clear` to exit or clear the log file.

# Files

- **output.txt**: Logs the user input and corresponding AI responses.
