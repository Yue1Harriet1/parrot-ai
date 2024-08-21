from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
from TTS.api import TTS
import os
import random

# Basic Flask instantiation, and TTS model loading (this should be done outside the app for better modularization)
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
text_to_speech = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# Global variables to store messages and control application state (this should be replaced by a database)
messages = []
output_dir = "audio_outputs/"
input_dir = "audio_inputs/"

# Basic Flask route to handle the chat page (the only page in this example)
@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_message = request.form['message']
        if user_message:
            # Append the user message to the chat history
            messages.append({'type': 'text', 'content': user_message})
            try:
                audio_filename = generate_random_filename()
                output_path = output_dir + audio_filename
                speaker_wav = get_latest_audio_sample()
                text_to_speech.tts_to_file(text=user_message, file_path=output_path, speaker_wav=speaker_wav, language="pt")
                messages.append({'type': 'audio', 'content': audio_filename})
                return jsonify({'status': 'success', 'audio_url': url_for('get_audio', filename=audio_filename)})
            except Exception as e:
                return jsonify({'status': 'error', 'message': str(e)})
        return redirect(url_for('chat'))
    return render_template('index.html', messages=messages)

@app.route('/upload_voice_sample', methods=['POST'])
def upload_voice_sample():
    if 'audio' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'})
    file = request.files['audio']
    if file and file.filename.endswith('.wav'):
        filename = generate_random_filename()
        filepath = os.path.join(input_dir, filename)
        file.save(filepath)
        return jsonify({'status': 'success', 'audio_url': url_for('get_audio', filename=filename)})
    return jsonify({'status': 'error', 'message': 'Invalid file format'})

@app.route('/upload_wav_file', methods=['POST'])
def upload_wav_file():
    if 'audio' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'})
    file = request.files['audio']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file and file.filename.endswith('.wav'):
        filename = generate_random_filename()
        file_path = os.path.join(input_dir, filename)
        file.save(file_path)
        # Return the URL to the uploaded audio file
        return jsonify({'status': 'success', 'audio_url': url_for('get_audio', filename=filename)})
    return jsonify({'status': 'error', 'message': 'Invalid file format. Only .wav files are allowed.'})

@app.route('/get_audio/<filename>', methods=['GET'])
def get_audio(filename):
    if os.path.exists(output_dir + filename):
        return send_file(output_dir + filename, mimetype='audio/wav')
    elif os.path.exists(input_dir + filename):
        return send_file(input_dir + filename, mimetype='audio/wav')
    return jsonify({'status': 'error', 'message': 'No audio file found.'})

def get_latest_audio_sample():
    files = [os.path.join(input_dir, file) for file in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, file))]
    return max(files, key=os.path.getctime)

def generate_random_filename():
    return f"audio_{random.randint(1000, 9999)}.wav"

if __name__ == '__main__':
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(input_dir, exist_ok=True)
    app.run(debug=True)
