from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import io

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

messages = []

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_message = request.form['message']
        if user_message:
            messages.append(user_message)
            # Calls the pipeline for audio generation
            try:
                # Generate or retrieve an audio file (simulated here)
                audio_data = generate_audio_response(user_message)  # Replace this with your logic
                
                # Append audio message to chat
                messages.append({'type': 'audio', 'content': audio_data})
                return jsonify({'status': 'success', 'message': 'Audio generated successfully.'})
            except Exception as e:
                return jsonify({'status': 'error', 'message': str(e)})
        return redirect(url_for('chat'))
    
    return render_template('index.html', messages=messages)

def generate_audio_response(message):
    # Simulating audio file generation
    # In practice, you'd use a library like gTTS, or return a real audio file
    audio_content = io.BytesIO()
    audio_content.write(b'Fake audio data for message: ' + message.encode())
    audio_content.seek(0)
    return audio_content

if __name__ == '__main__':
    app.run(debug=True)
