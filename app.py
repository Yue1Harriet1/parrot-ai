from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
from TTS.api import TTS
import os
import random

# Basic Flask instantiation, and TTS model loading (this should be done outside the app for better modularization)
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
text_to_speech = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
output_dir = "audio_outputs/"

# Global variable to store messages (this should be replaced by a database)
messages = []

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
                text_to_speech.tts_to_file(text=user_message, file_path=output_path, speaker_wav="audio_samples/female.wav", language="en")
                messages.append({'type': 'audio', 'content': audio_filename})
                return jsonify({'status': 'success', 'audio_url': url_for('get_audio', filename=audio_filename)})
            except Exception as e:
                return jsonify({'status': 'error', 'message': str(e)})
        return redirect(url_for('chat'))
    return render_template('index.html', messages=messages)

@app.route('/get_audio/<filename>')
def get_audio(filename):
    return send_file(os.path.join(output_dir, filename), mimetype='audio/wav')

def generate_random_filename():
    return f"output_{random.randint(1000, 9999)}.wav"

if __name__ == '__main__':
    os.makedirs(output_dir, exist_ok=True)
    app.run(debug=True)
