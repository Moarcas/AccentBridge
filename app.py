from flask import Flask, render_template, request, send_file

app = Flask(__name__,  static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        audio_file.save('uploads/audio.webm')
        return 'audio.webn'
    else:
        return 'No audio file received.', 400

@app.route('/audio')
def get_audio():
    audio_file_path = 'uploads/audio.webm'
    try:
        return send_file(audio_file_path, as_attachment=True)
    except FileNotFoundError:
        return 'Audio file not found.', 404

if __name__ == '__main__':
    app.run(debug=True)
