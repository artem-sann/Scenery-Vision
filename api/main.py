import datetime
import logging

from flask import Flask, request, jsonify, make_response

from model import ModelRuT5
from utils import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = SESSION_TYPE
model = ModelRuT5()


def main():
    logging.info("API start.")
    app.run(port=PORT, host='127.0.0.1')
    logging.info("API stop.")


# @app.route('/scenery-vision/api/v1.0/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         return json.dumps(random.choice(SPECS), ensure_ascii=False)
#     else:
#         return "POST your sequences"


@app.route('/scenery-vision/api/v1.0/generation', methods=['POST'])
def generation():
    request_json = request.json
    log_request("/scenery-vision/api/v1.0/generation", "POST", request_json)
    response = model.generate(request_json)
    return json.dumps(response, ensure_ascii=False).encode('utf8')


@app.route('/scenery-vision/api/v1.0/retrain', methods=['POST'])
def retrain():
    request_json = request.json
    log_request("/scenery-vision/api/v1.0/retrain", "POST", request_json)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def log_request(address, method, request_data):
    logging.info("--------------------")
    logging.info(f"New Request to {address}. Method: {method}")
    logging.info(f"Request time: {datetime.datetime.now()}")
    logging.info(f"Request data: {str(request_data)}")


if __name__ == '__main__':
    main()
