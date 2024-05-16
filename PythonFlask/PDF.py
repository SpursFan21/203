from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('PDF_submit.jinja')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file'
    
    if file:
        filename = file.filename
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print("Saving file to:", save_path)  # Debugging statement
        file.save(save_path)
        return render_template('PDF_display.jinja', filename=filename)


@app.route('/uploads/<filename>')
def display_file(filename):
    return send_from_directory(os.path.join(os.getcwd(), 'uploads'), filename)


if __name__ == '__main__':
    app.run(debug=True)
