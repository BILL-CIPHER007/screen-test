import os
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado", 400

    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)  

    return "Arquivo recebido com sucesso!", 200

@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files)

@app.route('/files/<filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/gallery', methods=['GET'])
def gallery():
    files = os.listdir(UPLOAD_FOLDER)
    images_html = "".join([f'<img src="/files/{file}" style="width:200px;margin:10px;">' for file in files])
    return f"<html><body>{images_html}</body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
