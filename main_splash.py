import sys

from PyQt5.QtCore import (
Qt, QTimer, pyqtSignal, QThread, pyqtSlot
)

from PyQt5.QtWidgets import (
QMainWindow,
QGraphicsDropShadowEffect,
QApplication
)

from PyQt5.QtGui import (
QColor
)

from ui.windows.splash_screen import Ui_MainWindow
from ui.windows import resources_rc

class ThreadMainSplash(QThread):
    onClose = pyqtSignal()

    def __init__(self, max_loads, splash, parent=None):
        QThread.__init__(self, parent)
        self.splash = splash
        self.max_loads = max_loads
        self.current_load = 0
        self.progress = 0

    def run(self):
        while self.progress < 100:
            self.msleep(300)
            self.app_progress()

        self.splash.ui.loading_state_info_label.setText('Done!')
        self.sleep(1)
        self.end_handler()

    @pyqtSlot(str)
    def set_data(self):
        self.current_load += 1

    @pyqtSlot(str)
    def set_text(self, text):
        self.splash.ui.loading_state_info_label.setText(text)

    def app_progress(self):
        to_load = int((self.current_load / self.max_loads) * 100)
        if(self.progress < to_load):
            self.progress += 4
            self.splash.ui.progressBar.setValue(self.progress)
        elif to_load == 100:
            self.progress += 1


    def end_handler(self):
        self.splash.close()
        self.onClose.emit()





class MainSplash(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(40)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(71, 40, 220, 150))

        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainSplash()
    sys.exit(app.exec())
