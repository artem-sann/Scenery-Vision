import requests
import threading

from pyqt_part import *
from exel_part import *


def execute_app():
    ##############################################################################################################
    # EXECUTE APP
    ##############################################################################################################
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

    ##############################################################################################################
    # END
    ##############################################################################################################


def api_thread_execute(table):
    print("Start thread")
    # преобразуем срез таблицы в json
    json_request = transform_to_json(table)[:2]
    # отправляем запрос и ждем ответа
    response = requests.post("http://127.0.0.1:3350/scenery-vision/api/v1.0/generation", json=json_request)

    global response_json_text
    response_json_text = response.json()
    global mess
    mess = "Передал"

    # print(response_json_text)
    print("End thread")


def logic_execute():
    global file_name
    while True:
        print(file_name)


app_thread = threading.Thread(target=execute_app, args=()).start()
api_thread = threading.Thread(target=api_thread_execute, args=()).start()
logic_thread = threading.Thread(target=logic_execute, args=()).start()
