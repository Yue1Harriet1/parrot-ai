# ParrotAI

ParrotAI is a Flask/Python-based application that serves as a proof of concept for generating speech using the `coqui/TTS` model from HuggingFace. This project is a quick proof of concept designed to explore the use of HuggingFace models for text-to-speech (TTS) synthesis while providing a simple user interface with options for selecting languages, recording voice samples, or submitting `.wav` files for custom voice generation.

> **Note**: This application is not production-ready and requires many enhancements before it can be considered for production use.

## Features

- **Text-to-Speech (TTS)**: Generates speech from text using the HuggingFace `coqui/TTS` model.
- **Language Selection**: Users can select from a variety of languages to generate the audio.
- **Voice Sample Recording**: Users can record their own voice samples in `.wav` format, which the model will use to generate personalized responses.
- **File Upload**: Users can upload `.wav` files to be used for generating audio responses.
- **Default Audio**: If no custom voice samples are provided, the application will use a standard `female.wav` file to generate audio.
- **Responsive Frontend**: The frontend is styled using Tailwind CSS (from the CDN) and provides a user-friendly interface for selecting languages, recording voice samples, and submitting files.

## Prerequisites

- **Python 3.10.12**: This application requires Python version 3.10.12 to run properly.
- **HuggingFace Account**: The application connects to HuggingFace to use the `coqui/TTS` model, so you'll need access to HuggingFace models.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dantasl/parrot-ai.git
   cd ParrotAI
   ``` 
2. **Set up a Virtual Environment**:
    ```bash
    python3.10 -m venv venv
    source venv/bin/activate
    ```
3. **Install Required Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Start the Flask Application:

```
flask run
```

## Access the Application:
Once the Flask server is running, you can access the application in your browser at:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Language Selection:
- Select the language from the dropdown menu (e.g., English, French, Spanish, etc.).
- Type your message in the textarea and submit it.

## Recording a Voice Sample:
- Click on the "Record" button to start recording your voice.
- After recording, click "Stop" to save the sample, which will be used to generate audio for subsequent requests.

## Upload a `.wav` File:
- Use the file input to upload a `.wav` file.
- The application will use the latest uploaded file to generate the audio response.

## Audio Generation:
- The application will generate a `.wav` audio file based on the latest voice sample submitted.
- If no voice sample is available, a default `female.wav` file will be used.

## Directory Structure:

```
ParrotAI/
│
├── audio_outputs/            # Directory where generated .wav files are stored
├── audio_inputs/             # Directory where the uploaded .wav files are stored
├── templates/
│   └── index.html            # Frontend HTML template with Tailwind CSS
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
└── README.md                 # Project README file
```

## Enhancements Required for Production
While ParrotAI is a functional proof of concept, several improvements would be needed to bring it to production:

- **Error Handling**: More robust error handling and logging for both the frontend and backend.
- **Database Integration**: Store user interactions, uploaded files, and language preferences in a database.
- **Authentication**: Implement user authentication and authorization.
- **Security Enhancements**: Secure file uploads, CSRF protection, and other Flask security best practices.
- **Model Optimization**: Optimize the TTS model for performance and scale it for higher loads.
- **Testing**: Add unit and integration tests to ensure application stability.

## Technology Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, Tailwind CSS (via CDN)
- **Text-to-Speech**: HuggingFace `coqui/TTS` model
- **Audio Handling**: `.wav` file recording and uploading