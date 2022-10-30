# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 760)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/scenery_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"}")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget {\n"
"    \n"
"    background-image: url(:/newPrefix/images/main_backround.png);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 100))
        self.header.setMaximumSize(QtCore.QSize(16777215, 10000))
        self.header.setStyleSheet("QFrame#header {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 140));\n"
"}\n"
"\n"
"")
        self.header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header.setFrameShadow(QtWidgets.QFrame.Plain)
        self.header.setLineWidth(0)
        self.header.setObjectName("header")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.header)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.top_header = QtWidgets.QFrame(self.header)
        self.top_header.setStyleSheet("")
        self.top_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_header.setObjectName("top_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_header)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_with_window_buttons = QtWidgets.QFrame(self.top_header)
        self.frame_with_window_buttons.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_with_window_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_with_window_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_with_window_buttons.setObjectName("frame_with_window_buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_with_window_buttons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_with_window_buttons)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/restore_maximize_1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_5.setAutoRepeat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.minimize_window_button = QtWidgets.QPushButton(self.frame_with_window_buttons)
        self.minimize_window_button.setStyleSheet("QPushButton#minimize_window_button::hover {\n"
"    background-color: rgb(17, 164, 255);\n"
"}")
        self.minimize_window_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images/minimize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_window_button.setIcon(icon2)
        self.minimize_window_button.setObjectName("minimize_window_button")
        self.horizontalLayout_2.addWidget(self.minimize_window_button)
        self.restore_window_button = QtWidgets.QPushButton(self.frame_with_window_buttons)
        self.restore_window_button.setStyleSheet("QPushButton#restore_window_button::hover {\n"
"    background-color: rgb(17, 164, 255);\n"
"}")
        self.restore_window_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/images/restore_maximize_2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restore_window_button.setIcon(icon3)
        self.restore_window_button.setObjectName("restore_window_button")
        self.horizontalLayout_2.addWidget(self.restore_window_button)
        self.close_window_button = QtWidgets.QPushButton(self.frame_with_window_buttons)
        self.close_window_button.setEnabled(True)
        self.close_window_button.setStyleSheet("QPushButton#close_window_button::hover {\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.close_window_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/images/Close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_window_button.setIcon(icon4)
        self.close_window_button.setObjectName("close_window_button")
        self.horizontalLayout_2.addWidget(self.close_window_button)
        self.horizontalLayout.addWidget(self.frame_with_window_buttons, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_8.addWidget(self.top_header)
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setEnabled(True)
        self.frame_3.setToolTip("")
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 15)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.left_header_frame_with_buttons = QtWidgets.QFrame(self.frame_3)
        self.left_header_frame_with_buttons.setStyleSheet("")
        self.left_header_frame_with_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_header_frame_with_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_header_frame_with_buttons.setObjectName("left_header_frame_with_buttons")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.left_header_frame_with_buttons)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.add_button = QtWidgets.QPushButton(self.left_header_frame_with_buttons)
        self.add_button.setAutoFillBackground(False)
        self.add_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/images/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon5)
        self.add_button.setIconSize(QtCore.QSize(60, 60))
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_9.addWidget(self.add_button)
        self.download_button = QtWidgets.QPushButton(self.left_header_frame_with_buttons)
        self.download_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/images/download.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_button.setIcon(icon6)
        self.download_button.setIconSize(QtCore.QSize(60, 60))
        self.download_button.setObjectName("download_button")
        self.horizontalLayout_9.addWidget(self.download_button)
        self.horizontalLayout_12.addWidget(self.left_header_frame_with_buttons, 0, QtCore.Qt.AlignLeft)
        self.scenary_vision_label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scenary_vision_label.sizePolicy().hasHeightForWidth())
        self.scenary_vision_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Abhaya Libre")
        font.setPointSize(42)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.scenary_vision_label.setFont(font)
        self.scenary_vision_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.scenary_vision_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scenary_vision_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scenary_vision_label.setObjectName("scenary_vision_label")
        self.horizontalLayout_12.addWidget(self.scenary_vision_label)
        self.right_header_frame_with_buttons = QtWidgets.QFrame(self.frame_3)
        self.right_header_frame_with_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_header_frame_with_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_header_frame_with_buttons.setObjectName("right_header_frame_with_buttons")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.right_header_frame_with_buttons)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.exel_page_button = QtWidgets.QPushButton(self.right_header_frame_with_buttons)
        self.exel_page_button.setObjectName("exel_page_button")
        self.horizontalLayout_8.addWidget(self.exel_page_button)
        self.main_page_button = QtWidgets.QPushButton(self.right_header_frame_with_buttons)
        self.main_page_button.setObjectName("main_page_button")
        self.horizontalLayout_8.addWidget(self.main_page_button)
        self.loading_page_button = QtWidgets.QPushButton(self.right_header_frame_with_buttons)
        self.loading_page_button.setObjectName("loading_page_button")
        self.horizontalLayout_8.addWidget(self.loading_page_button)
        self.horizontalLayout_12.addWidget(self.right_header_frame_with_buttons)
        self.verticalLayout_8.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.header)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.exel_page = QtWidgets.QWidget()
        self.exel_page.setStyleSheet("")
        self.exel_page.setObjectName("exel_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.exel_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.exel_button = QtWidgets.QPushButton(self.exel_page)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.exel_button.setFont(font)
        self.exel_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.exel_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.exel_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.exel_button.setAcceptDrops(False)
        self.exel_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exel_button.setAutoFillBackground(False)
        self.exel_button.setStyleSheet("")
        self.exel_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/images/add_exel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exel_button.setIcon(icon7)
        self.exel_button.setIconSize(QtCore.QSize(300, 300))
        self.exel_button.setCheckable(False)
        self.exel_button.setAutoDefault(False)
        self.exel_button.setDefault(False)
        self.exel_button.setFlat(False)
        self.exel_button.setObjectName("exel_button")
        self.verticalLayout_2.addWidget(self.exel_button, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.exel_page)
        self.main_page = QtWidgets.QWidget()
        self.main_page.setStyleSheet("")
        self.main_page.setObjectName("main_page")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.main_page)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.left_arrow_frame = QtWidgets.QFrame(self.main_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_arrow_frame.sizePolicy().hasHeightForWidth())
        self.left_arrow_frame.setSizePolicy(sizePolicy)
        self.left_arrow_frame.setStyleSheet("")
        self.left_arrow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_arrow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_arrow_frame.setObjectName("left_arrow_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_arrow_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.left_arrow_button = QtWidgets.QPushButton(self.left_arrow_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_arrow_button.sizePolicy().hasHeightForWidth())
        self.left_arrow_button.setSizePolicy(sizePolicy)
        self.left_arrow_button.setStyleSheet("")
        self.left_arrow_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/images/arrow_to_left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_arrow_button.setIcon(icon8)
        self.left_arrow_button.setIconSize(QtCore.QSize(100, 200))
        self.left_arrow_button.setObjectName("left_arrow_button")
        self.verticalLayout_3.addWidget(self.left_arrow_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_4.addWidget(self.left_arrow_frame, 0, QtCore.Qt.AlignLeft)
        self.main_area_wrap_frame = QtWidgets.QFrame(self.main_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_area_wrap_frame.sizePolicy().hasHeightForWidth())
        self.main_area_wrap_frame.setSizePolicy(sizePolicy)
        self.main_area_wrap_frame.setStyleSheet("")
        self.main_area_wrap_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_area_wrap_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_area_wrap_frame.setObjectName("main_area_wrap_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_area_wrap_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.main_information_frame = QtWidgets.QFrame(self.main_area_wrap_frame)
        self.main_information_frame.setStyleSheet("")
        self.main_information_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_information_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_information_frame.setObjectName("main_information_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.main_information_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.title_frame = QtWidgets.QFrame(self.main_information_frame)
        self.title_frame.setEnabled(True)
        self.title_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius: 20px;\n"
"border-top-left-radius: 20px;\n"
"")
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.title_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.title_label = QtWidgets.QLabel(self.title_frame)
        font = QtGui.QFont()
        font.setFamily("Mulish Medium")
        font.setPointSize(24)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_5.addWidget(self.title_label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6.addWidget(self.title_frame)
        self.info_frame = QtWidgets.QFrame(self.main_information_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_frame.sizePolicy().hasHeightForWidth())
        self.info_frame.setSizePolicy(sizePolicy)
        self.info_frame.setStyleSheet("background-color: rgba(255, 250, 237, 230);\n"
"border-bottom-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;")
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.info_frame)
        self.verticalLayout_7.setContentsMargins(40, 10, 40, 20)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.first_line = QtWidgets.QFrame(self.info_frame)
        self.first_line.setMinimumSize(QtCore.QSize(0, 0))
        self.first_line.setStyleSheet("background-color: None;")
        self.first_line.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.first_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.first_line.setObjectName("first_line")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.first_line)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.image_label = QtWidgets.QLabel(self.first_line)
        self.image_label.setMinimumSize(QtCore.QSize(250, 250))
        self.image_label.setMaximumSize(QtCore.QSize(250, 250))
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap(":/newPrefix/images/example_image.png"))
        self.image_label.setScaledContents(True)
        self.image_label.setObjectName("image_label")
        self.horizontalLayout_6.addWidget(self.image_label)
        self.characteristics_frame = QtWidgets.QFrame(self.first_line)
        self.characteristics_frame.setMinimumSize(QtCore.QSize(0, 250))
        self.characteristics_frame.setMaximumSize(QtCore.QSize(16777215, 250))
        self.characteristics_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px\n"
"\n"
"\n"
"")
        self.characteristics_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.characteristics_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.characteristics_frame.setObjectName("characteristics_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.characteristics_frame)
        self.verticalLayout_10.setContentsMargins(20, 20, 20, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.characteristics_text_frame = QtWidgets.QFrame(self.characteristics_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.characteristics_text_frame.sizePolicy().hasHeightForWidth())
        self.characteristics_text_frame.setSizePolicy(sizePolicy)
        self.characteristics_text_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.characteristics_text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.characteristics_text_frame.setObjectName("characteristics_text_frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.characteristics_text_frame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.characteristics_text_frame)
        font = QtGui.QFont()
        font.setFamily("Mulish")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.characteristics_label = QtWidgets.QLabel(self.characteristics_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.characteristics_label.sizePolicy().hasHeightForWidth())
        self.characteristics_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Mulish")
        font.setPointSize(10)
        self.characteristics_label.setFont(font)
        self.characteristics_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.characteristics_label.setObjectName("characteristics_label")
        self.verticalLayout_11.addWidget(self.characteristics_label)
        self.verticalLayout_10.addWidget(self.characteristics_text_frame)
        self.buttons_frame = QtWidgets.QFrame(self.characteristics_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons_frame.sizePolicy().hasHeightForWidth())
        self.buttons_frame.setSizePolicy(sizePolicy)
        self.buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_frame.setObjectName("buttons_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.buttons_frame)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.characteristics_button_1 = QtWidgets.QPushButton(self.buttons_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.characteristics_button_1.sizePolicy().hasHeightForWidth())
        self.characteristics_button_1.setSizePolicy(sizePolicy)
        self.characteristics_button_1.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/images/pushed_circle_button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.characteristics_button_1.setIcon(icon9)
        self.characteristics_button_1.setIconSize(QtCore.QSize(25, 25))
        self.characteristics_button_1.setDefault(True)
        self.characteristics_button_1.setFlat(False)
        self.characteristics_button_1.setObjectName("characteristics_button_1")
        self.horizontalLayout_3.addWidget(self.characteristics_button_1)
        self.characteristics_button_2 = QtWidgets.QPushButton(self.buttons_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.characteristics_button_2.sizePolicy().hasHeightForWidth())
        self.characteristics_button_2.setSizePolicy(sizePolicy)
        self.characteristics_button_2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/images/circle_button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.characteristics_button_2.setIcon(icon10)
        self.characteristics_button_2.setIconSize(QtCore.QSize(25, 25))
        self.characteristics_button_2.setObjectName("characteristics_button_2")
        self.horizontalLayout_3.addWidget(self.characteristics_button_2)
        self.characteristics_button_3 = QtWidgets.QPushButton(self.buttons_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.characteristics_button_3.sizePolicy().hasHeightForWidth())
        self.characteristics_button_3.setSizePolicy(sizePolicy)
        self.characteristics_button_3.setText("")
        self.characteristics_button_3.setIcon(icon10)
        self.characteristics_button_3.setIconSize(QtCore.QSize(25, 25))
        self.characteristics_button_3.setObjectName("characteristics_button_3")
        self.horizontalLayout_3.addWidget(self.characteristics_button_3)
        self.verticalLayout_10.addWidget(self.buttons_frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.characteristics_frame)
        self.verticalLayout_7.addWidget(self.first_line)
        self.description_frame = QtWidgets.QFrame(self.info_frame)
        self.description_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.description_frame.setStyleSheet("background-color: None;")
        self.description_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.description_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.description_frame.setObjectName("description_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.description_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.description_text_frame = QtWidgets.QFrame(self.description_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description_text_frame.sizePolicy().hasHeightForWidth())
        self.description_text_frame.setSizePolicy(sizePolicy)
        self.description_text_frame.setMinimumSize(QtCore.QSize(0, 200))
        self.description_text_frame.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);")
        self.description_text_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.description_text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.description_text_frame.setObjectName("description_text_frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.description_text_frame)
        self.verticalLayout_12.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.description_text_frame)
        font = QtGui.QFont()
        font.setFamily("Mulish")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
        self.descreption_label = QtWidgets.QLabel(self.description_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descreption_label.sizePolicy().hasHeightForWidth())
        self.descreption_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Mulish")
        font.setPointSize(10)
        self.descreption_label.setFont(font)
        self.descreption_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.descreption_label.setObjectName("descreption_label")
        self.verticalLayout_12.addWidget(self.descreption_label)
        self.horizontalLayout_7.addWidget(self.description_text_frame)
        self.buttons_frame_2 = QtWidgets.QFrame(self.description_frame)
        self.buttons_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_frame_2.setObjectName("buttons_frame_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.buttons_frame_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.description_button_1 = QtWidgets.QPushButton(self.buttons_frame_2)
        self.description_button_1.setText("")
        self.description_button_1.setIcon(icon9)
        self.description_button_1.setIconSize(QtCore.QSize(25, 25))
        self.description_button_1.setObjectName("description_button_1")
        self.verticalLayout_9.addWidget(self.description_button_1, 0, QtCore.Qt.AlignHCenter)
        self.description_button_2 = QtWidgets.QPushButton(self.buttons_frame_2)
        self.description_button_2.setText("")
        self.description_button_2.setIcon(icon10)
        self.description_button_2.setIconSize(QtCore.QSize(25, 25))
        self.description_button_2.setObjectName("description_button_2")
        self.verticalLayout_9.addWidget(self.description_button_2, 0, QtCore.Qt.AlignHCenter)
        self.description_button_3 = QtWidgets.QPushButton(self.buttons_frame_2)
        self.description_button_3.setText("")
        self.description_button_3.setIcon(icon10)
        self.description_button_3.setIconSize(QtCore.QSize(25, 25))
        self.description_button_3.setObjectName("description_button_3")
        self.verticalLayout_9.addWidget(self.description_button_3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_7.addWidget(self.buttons_frame_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_7.addWidget(self.description_frame)
        self.verticalLayout_6.addWidget(self.info_frame)
        self.verticalLayout_5.addWidget(self.main_information_frame, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_4.addWidget(self.main_area_wrap_frame)
        self.frame_6 = QtWidgets.QFrame(self.main_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("background: None;\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.right_arrow_button = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_arrow_button.sizePolicy().hasHeightForWidth())
        self.right_arrow_button.setSizePolicy(sizePolicy)
        self.right_arrow_button.setStyleSheet("border: none;\n"
"outline: none;\n"
"background: None;")
        self.right_arrow_button.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/newPrefix/images/arrow_to_rightsvg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right_arrow_button.setIcon(icon11)
        self.right_arrow_button.setIconSize(QtCore.QSize(100, 200))
        self.right_arrow_button.setObjectName("right_arrow_button")
        self.verticalLayout_4.addWidget(self.right_arrow_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignRight)
        self.stackedWidget.addWidget(self.main_page)
        self.loading_page = QtWidgets.QWidget()
        self.loading_page.setObjectName("loading_page")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.loading_page)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.progressBar = QtWidgets.QProgressBar(self.loading_page)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    width: 300px;\n"
"    height: 30px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(63, 36, 35);\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_10.addWidget(self.progressBar, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.loading_page)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scenery Vision"))
        self.scenary_vision_label.setText(_translate("MainWindow", "S  c  e  n  e  r  y      V  i  s  i  o  n"))
        self.exel_page_button.setText(_translate("MainWindow", "Exel_page"))
        self.main_page_button.setText(_translate("MainWindow", "Main_page"))
        self.loading_page_button.setText(_translate("MainWindow", "Loading_page"))
        self.title_label.setText(_translate("MainWindow", "Кольцо из золота с бриллиантами"))
        self.label_2.setText(_translate("MainWindow", "Общие характеристики"))
        self.characteristics_label.setText(_translate("MainWindow", "fergrgresgrgresgrsegrg"))
        self.label_5.setText(_translate("MainWindow", "Описание"))
        self.descreption_label.setText(_translate("MainWindow", "gfrgsrgrgrgr"))
import resources
