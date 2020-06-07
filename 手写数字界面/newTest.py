import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from 手写数字界面 import Test

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Test.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())