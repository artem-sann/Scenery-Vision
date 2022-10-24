import io
import os
import shutil
import json
import zipfile

from flask import Flask, flash, request, redirect
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

        for file in request.files:
        return json.dumps([])
    else:
        return "POST your image sequences"


if __name__ == "__main__":
    app.run(port=PORT)
