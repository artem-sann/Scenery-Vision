import sys

from pyqt_part import MainWindow, QApplication


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
