from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "Nenhum arquivo enviado", 400
    
    file = request.files["file"]
    if file.filename == "":
        return "Nome de arquivo inválido", 400

    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return "Arquivo recebido com sucesso", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
