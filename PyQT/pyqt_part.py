##############################################################################################################
# # IMPORTS
##############################################################################################################
import sys
import os

import psutil
import PySide2extn
from PyQt5.uic import loadUi

from resources import *
import PyQt5.QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtProperty, QPropertyAnimation
from PySide2 import *

# IMPORT GUI FILE
from interface import *
# QT MATERIAL
from qt_material import *

##############################################################################################################
global file_name
file_name = "hello"


##############################################################################################################
# # MAIN WINDOW CLASS
##############################################################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.clickPosition = None
        self.oldPosition = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set window title and icon
        # These title and icon will not appear on our app because we removed the title bar
        self.setWindowTitle("UTIL Manager")
        # # self.setWindowIcon("")

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

        self.ui.top_header.mouseMoveEvent = moveWindow
        #
        # # Left menu toggle button (Show/hide menu labels)
        # self.ui.pushButton.clicked.connect(lambda: self.slideLeftMenu())

        self.show()

    # Browse files function
    def browse_files(self):
        global file_name
        file_name = QFileDialog.getOpenFileName(self, 'open file', 'C:', 'XLSX files (*xlsx)')


    # Add mouse events to the window
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    # # Slide left menu function
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
            icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images/restore_maximize_2.svg"), QtGui.QIcon.Normal,
                            QtGui.QIcon.Off)
            self.ui.restore_window_button.setIcon(icon2)
            self.showNormal()
        else:
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/restore_maximize_1.svg"), QtGui.QIcon.Normal,
                            QtGui.QIcon.Off)
            self.ui.restore_window_button.setIcon(icon1)
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
