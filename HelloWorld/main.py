import sys
from HelloWorld import HelloWorld

from PyQt5.QtWidgets import QApplication, QMainWindow



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = HelloWorld.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())