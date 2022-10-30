import time

import pandas as pd
import requests
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot

from exel_part import load_and_processing_excel, transform_to_json

glob_size = 0
load_flag = False

class APIThread(QThread):
    update_api_data = pyqtSignal(pd.DataFrame)

    def __init__(self, path_to_table=""):
        super().__init__()
        self.batch = 3
        self.url_to_api = "http://127.0.0.1:3350/scenery-vision/api/v1.0/generation"

        self.path_to_table = path_to_table
        self.table = None
        self.size = 0
        self.count = 0
        self.flag = False

    def reset_file(self, path_to_table: str):
        self.path_to_table = path_to_table
        self.flag = True
        global load_flag
        load_flag = False

    def run(self):
        while True:
            print("Работает")
            try:
                if self.flag:
                    self.flag = False
                    self.table = load_and_processing_excel(self.path_to_table)
                    self.size = self.table.shape[0]
                    global glob_size
                    glob_size = self.size
                    self.count = 0
                if self.count >= self.size:
                    return
                slice = self.table.iloc[self.count: self.count + self.batch]
                json_slice = transform_to_json(slice)
                response = self.get_response(json_slice)
                slice["Описание"] = [unit["Описание"] for unit in response]
                self.update_api_data.emit(slice)

                global load_flag
                load_flag = True
                self.count += self.batch
            except Exception as ex:
                print(ex)
                time.sleep(1)

    def get_response(self, json_request):
        response = requests.post(self.url_to_api, json=json_request)
        return response.json()
