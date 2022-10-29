##############################################################################################################
# IMPORTS
##############################################################################################################
import sys

from exel_part import pd
from resources import *
from typing import Iterable
from PyQt5.QtWidgets import *
from PySide2 import *

# IMPORT GUI FILE
from interface import *
# QT MATERIAL
from qt_material import *

##############################################################################################################
global file_name
file_name = "hello"


##############################################################################################################
# MAIN WINDOW CLASS
##############################################################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.clickPosition = None
        self.oldPosition = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # type: ignore

        # Set window title and icon
        # These title and icon will not appear on our app because we removed the title bar
        self.setWindowTitle("UTIL Manager")
        # self.setWindowIcon("")

        # Cheat buttons
        self.ui.exel_page_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.exel_page))
        self.ui.main_page_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_page))
        self.ui.loading_page_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.loading_page))

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

        # Add button
        self.ui.add_button.clicked.connect(self.browse_files)

        # Function to Move window on mouse drag event on the title bar
        def moveWindow(e):
            if not self.isMaximized():
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.ui.top_header.mouseMoveEvent = moveWindow  # type: ignore
        #
        # Left menu toggle button (Show/hide menu labels)
        # self.ui.pushButton.clicked.connect(lambda: self.slideLeftMenu())

        self.show()

    # Browse files function
    def browse_files(self):
        global file_name
        file_name = QFileDialog.getOpenFileName(self, 'open file', 'C:', 'XLSX files (*xlsx)')

    def change_page(self):
        # TODO: Тут нужен индекс страницы
        raise NotImplementedError

    def change_chars_page(self):
        # TODO: Тут нужен индекс страницы
        raise NotImplementedError

    def load_chars(self, chars_data: pd.Series) -> None:
        generated_text = "\n".join([f"{char_key}: {char_val}" for char_key, char_val in zip(chars_data.index, chars_data.values)])
        self.ui.characteristics_label.setText(generated_text)

    def load_page(self, image_path: str, generated_data: pd.DataFrame, page_idx: int, chars_idx: int, description_col: str = "Описание", chars_on_page: int = 4) -> None:
        # Load image
        # TODO: Resize image (can be done serverside or in download func)
        pixmap = QtGui.QPixmap(image_path)
        self.ui.image_label.setPixmap(pixmap)

        characteristics = generated_data.drop(description_col, axis=0).columns.tolist()
        cur_characteristics = characteristics[chars_idx:chars_idx + chars_on_page]
        characteristics_data = generated_data[cur_characteristics].iloc[page_idx].copy()
        self.load_chars(characteristics_data)

        generated_description = generated_data[description_col].iloc[page_idx].values[0]
        self.ui.descreption_label.setText(generated_description)

    # Add mouse events to the window

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    # Slide left menu function
    # def slideLeftMenu(self):
    #     width = self.ui.left_menu_cont_frame.width()
    #
    #     if width == 40:
    #         newWidth = 200
    #     else:
    #         newWidth = 40
    #
    #     self.animation = QPropertyAnimation(self.ui.left_menu_cont_frame, b"minimumWidth")
    #     self.animation.setDuration(250)
    #     self.animation.setStartValue(width)
    #     self.animation.setEndValue(newWidth)
    #     self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    #     self.animation.start()

    # Update restore button icon on maximizing or minimizing window
    # Also it is possible to add changing icon on the button
    def restore_or_maximize_window(self):
        if self.isMaximized():
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images/restore_maximize_2.svg"), QtGui.QIcon.Normal,  # type: ignore
                            QtGui.QIcon.Off)  # type: ignore
            self.ui.restore_window_button.setIcon(icon2)
            self.showNormal()
        else:
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/restore_maximize_1.svg"), QtGui.QIcon.Normal,  # type: ignore
                            QtGui.QIcon.Off)  # type: ignore
            self.ui.restore_window_button.setIcon(icon1)
            self.showMaximized()


##############################################################################################################
# EXECUTE APP
##############################################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

##############################################################################################################
# END
##############################################################################################################
