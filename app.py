import json
import os

from flask import Flask, request, Response
from werkzeug.utils import secure_filename

from core import Core

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = 'files'

core = Core(os.path.join(app.config["UPLOAD_FOLDER"]), delete_files=True)


@app.route("/barcode", methods=['POST'])
def barcode():
    file = request.files.get("arquivo")
    if file is None:
        result_text = "Envie o arquivo junto à requisição HTTP POST"
        status = 422
    else:
        secured_filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], secured_filename))
        if '.pdf' in secured_filename:
            result_text = core.extract_barcode_from_pdf(f'files/{secured_filename}')
        else:
            result_text = core.extract_barcode_from_image(f'files/{secured_filename}')
        status = 200
    data = {
        'linhadigitavel': result_text
    }
    js = json.dumps(data)
    resp = Response(js, status=status, mimetype='application/json')
    return resp


if __name__ == "__main__":
    app.run()
