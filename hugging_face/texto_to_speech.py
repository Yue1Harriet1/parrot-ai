from TTS.api import TTS

# Load the text-to-speech pipeline
text_to_speech = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# Generating speech by cloning a voice using default settings
text_to_speech.tts_to_file(text="Hello world, I am an AI generated voice. I can speak in multiple languages. I can also clone voices. Let me say the name: Lucas Dantas.",
                file_path="output.wav",
                speaker_wav="audio_samples/female.wav",
                language="en")