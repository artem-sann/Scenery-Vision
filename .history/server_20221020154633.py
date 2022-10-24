import io
import os
import shutil
import zipfile

from flask import Flask, flash, request, redirect, send_file
from glob import glob
from utils import *
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = SESSION_TYPE


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if SERVER_FILE_PATH not in request.files:
            flash('No file part')
            return redirect(request.url)

        

        shutil.make_archive("result", 'zip', RESULT_FOLDER)

        return send_file("result.zip", mimetype='application/zip')
    else:
        return "POST your image sequences"


if __name__ == "__main__":
    app.run(port=PORT)
