import io
import os
import random
import shutil
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
        return json.dumps(random.choice(SPECS))
    else:
        return "POST your file sequences"


if __name__ == "__main__":
    app.run(port=PORT)
