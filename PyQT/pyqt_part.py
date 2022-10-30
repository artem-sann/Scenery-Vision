##############################################################################################################
# # IMPORTS
##############################################################################################################
import sys
import time

from PyQt5.QtGui import QFont

import Thread
from exel_part import download_image, excel_save
from resources import *
from PyQt5.QtWidgets import *
from PySide2 import *

# IMPORT GUI FILE
from interface import *
# QT MATERIAL
from qt_material import *
import pandas as pd

from Thread import APIThread, final_data, f_data_cnt, first_load_flag

##############################################################################################################
# # MAIN WINDOW CLASS
##############################################################################################################

page_index = 0
char_index = 0
desc_index = 0



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.clickPosition = None
        self.oldPosition = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # fonts init
        ################################################################################################################
        font_abhaya_libre_id = QFontDatabase.addApplicationFont(":/fonts/fonts/AbhayaLibre-Regular.ttf")
        fontName = QFontDatabase.applicationFontFamilies(font_abhaya_libre_id)[0]
        self.font_abhaya_libre = QFont(fontName, 42)
        self.ui.scenary_vision_label.setFont(self.font_abhaya_libre)

        font_mulish_medium_id = QFontDatabase.addApplicationFont(":/fonts/fonts/Mulish-Medium.ttf")
        fontName = QFontDatabase.applicationFontFamilies(font_mulish_medium_id)[0]
        self.font_mulish_medium = QFont(fontName, 24)
        self.ui.title_label.setFont(self.font_mulish_medium)

        font_mulish_bold_id = QFontDatabase.addApplicationFont(":/fonts/fonts/Mulish-Bold.ttf")
        fontName = QFontDatabase.applicationFontFamilies(font_mulish_bold_id)[0]
        self.font_mulish_bold = QFont(fontName, 12)
        self.ui.label_2.setFont(self.font_mulish_bold)
        self.ui.label_5.setFont(self.font_mulish_bold)

        font_mulish_regular_id = QFontDatabase.addApplicationFont(":/fonts/fonts/Mulish-Regular.ttf")
        fontName = QFontDatabase.applicationFontFamilies(font_mulish_regular_id)[0]
        self.font_mulish_regular = QFont(fontName, 10)
        self.ui.characteristics_label.setFont(self.font_mulish_regular)
        self.ui.descreption_label.setFont(self.font_mulish_regular)
        ################################################################################################################
        # Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # type: ignore
        self.ui.stackedWidget.setCurrentWidget(self.ui.exel_page)
        # Set window title and icon
        # These title and icon will not appear on our app because we removed the title bar
        self.setWindowTitle("Scenery Vision")
        # # self.setWindowIcon("")

        self.api_thread = APIThread()
        self.ui.title_label.setText("ddddddddddddddd")


        # Hiding unnecessary buttons
        # self.ui.add_button.hide()
        # self.ui.download_button.hide()

        # Minimize window
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        # Close window
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        # Restore/Maximize window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        # Exel huge button
        self.ui.exel_button.clicked.connect(self.browse_files)

        self.ui.left_arrow_button.clicked.connect(self.change_page_left)
        self.ui.right_arrow_button.clicked.connect(self.change_page_right)

        # Add button
        self.ui.add_button.clicked.connect(self.browse_files)
        # Add button
        self.ui.download_button.clicked.connect(self.save_files)

        # Function to Move window on mouse drag event on the title bar
        def moveWindow(e):
            if not self.isMaximized():
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.ui.top_header.mouseMoveEvent = moveWindow  # type: ignore
        #
        # # Left menu toggle button (Show/hide menu labels)
        # self.ui.pushButton.clicked.connect(lambda: self.slideLeftMenu())

        self.show()

    # Browse files function
    def browse_files(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.exel_page)
        file_name = QFileDialog.getOpenFileName(self, 'open file', 'C:', 'XLSX files (*xlsx)')[0]
        self.ui.stackedWidget.setCurrentWidget(self.ui.loading_page)
        if file_name != "":

            self.api_thread.reset_file(file_name)
            self.api_thread.start()
            while not Thread.load_flag:
                print("ждемс")
                print(Thread.load_flag)

            self.ui.stackedWidget.setCurrentIndex(1)
            self.load_page(download_image(Thread.final_data["Путь к фото"][page_index],
            Thread.final_data["Наименование"][page_index]), Thread.final_data, page_index, 0, 0)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.exel_page)


    def save_files(self):
        file_name = QFileDialog.getSaveFileName(self, 'save file', 'C:', 'XLSX files (*xlsx)')[0] + '.xlsx'
        print(file_name)
        print(Thread.final_data)
        excel_save(Thread.final_data, file_name)


    def change_page_left(self):  # left
        global page_index
        print(page_index)
        if page_index > 0:
            page_index = page_index - 1
            print(page_index)
            self.load_page(download_image(Thread.final_data["Путь к фото"][page_index],
                                          Thread.final_data["Наименование"][page_index]), Thread.final_data, page_index,
                           0, 0)

    def change_page_right(self):  # Right
        global page_index

        print(page_index)
        if page_index < 15:
            page_index = page_index + 1
            print(page_index)
            self.load_page(download_image(Thread.final_data["Путь к фото"][page_index],
                                          Thread.final_data["Наименование"][page_index]), Thread.final_data, page_index,
                           0, 0)



    def load_chars(self, chars_data: pd.Series) -> None:
        generated_text = "\n".join(
            [f"{char_key}: {char_val}" for char_key, char_val in zip(chars_data.index, chars_data.values)])
        self.ui.characteristics_label.setText(generated_text)
        self.ui.characteristics_label.setWordWrap(True)

    def load_description(self, description_data: pd.Series, description_idx: int) -> None:
        generated_description = description_data.values[description_idx]
        self.ui.descreption_label.setText(generated_description)   # type: ignore
        self.ui.descreption_label.setWordWrap(True)

    def load_page(
            self, image_path: str,
            generated_data: pd.DataFrame,
            page_idx: int, chars_idx: int,
            description_idx: int,
            description_col: str = "Описание",
            chars_on_page: int = 4
    ) -> None:
        # Load image
        # TODO: Resize image (can be done serverside or in download func)
        pixmap = QtGui.QPixmap(image_path)
        self.ui.image_label.setPixmap(pixmap)
        self.ui.title_label.setText(generated_data["Наименование для сайта"][page_idx])
        self.ui.title_label.setWordWrap(True)

        characteristics = generated_data.drop(description_col, axis=1).columns.tolist()
        cur_characteristics = characteristics[chars_idx:chars_idx + chars_on_page]
        characteristics_data = generated_data[cur_characteristics].iloc[page_idx].copy()
        self.load_chars(characteristics_data)
        self.load_description(description_data=generated_data[description_col],
                              description_idx=description_idx)

    # Add mouse events to the window

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    # Update restore button icon on maximizing or minimizing window
    # Also it is possible to add changing icon on the button
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.ui.restore_window_button.setStyleSheet("QPushButton#restore_window_button {\nwidth: 30px;\nheight: 30px;\nborder-image: url(:/newPrefix/images/restore_maximize_2.svg);\n}\nQPushButton#restore_window_button::hover {\nwidth: 30px;\nheight: 30px;\nbackground-color: rgb(85, 170, 255);\nborder-image: url(:/newPrefix/images/restore_maximize_2.svg);\n}")
            self.showNormal()
        else:
            self.ui.restore_window_button.setStyleSheet("QPushButton#restore_window_button {\nwidth: 30px;\nheight: 30px;\nborder-image: url(:/newPrefix/images/restore_maximize_1.svg);\n}\nQPushButton#restore_window_button::hover {\nwidth: 30px;\nheight: 30px;\nbackground-color: rgb(85, 170, 255);\nborder-image: url(:/newPrefix/images/restore_maximize_1.svg);\n}")
            self.showMaximized()


##############################################################################################################
# # EXECUTE APP
##############################################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

##############################################################################################################
# # END
##############################################################################################################
