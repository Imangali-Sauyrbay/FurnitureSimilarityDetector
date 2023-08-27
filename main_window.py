from PyQt5 import QtCore, QtWidgets, QtGui
import sys

from ui.windows.main_window import Ui_MainWindow
from ui.windows import resources_rc
from main_splash import MainSplash
from main_splash import ThreadMainSplash
from web_driver.chrome import ImageDriver
from configs import Config
from answer_counter import AnswerTaker


MAXIMIZED = False

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        splash = MainSplash()

        self.loader = ThreadMainSplash(3, splash, self)
        self.loader.onClose.connect(lambda: self.show())
        self.loader.start(QtCore.QThread.Priority.HighestPriority)

        def LoadWebDriver():
            self.loader.set_text('Loading web driver...')
            ImageDriver.get_instance()
            self.loader.set_data()

        def LoadConfig():
            self.loader.set_text('Loading config...')
            Config.get_instance()
            self.loader.set_data()
            QtCore.QTimer.singleShot(1000, LoadWebDriver)

        def LoadUI():
            self.loader.set_text('Loading ui...')
            self.init_ui()
            self.loader.set_data()
            QtCore.QTimer.singleShot(1000, LoadConfig)


        QtCore.QTimer.singleShot(2000, LoadUI)

    def init_ui(self):
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(40)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(71, 40, 220, 150))
        self.setGraphicsEffect(self.shadow)

        self.ui.close_btn.clicked.connect(lambda: self.close())
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.restore_btn.clicked.connect(lambda: self.restore_or_maximize_window())

        def moveWindow(e):
            if not self.isMaximized():
                if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clicked_pos)
                    self.clicked_pos = e.globalPos()
                    e.accept()
            else:
                p = e.pos()
                percent = p.x() / self.width(), p.y() / self.height()
                self.restore_or_maximize_window()
                self.move(p - QtCore.QPoint(int(self.width() * percent[0]), int(self.height() * percent[1])))

        self.ui.menu_toggle_btn.clicked.connect(self.toggle_left_menu)
        self.ui.main_header.mouseMoveEvent = moveWindow

        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

        self.ui.home_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        self.ui.experiments_page_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.experiment_page))
        self.ui.settings_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))

        for btn in self.ui.left_side_menu.findChildren(QtWidgets.QPushButton):
            btn.clicked.connect(self.apply_nav_btns_style)

        self.answers_ui = AnswerTaker(self.ui.home_page_layout, self)


    def restore_or_maximize_window(self):
        global MAXIMIZED
        self.showNormal() if MAXIMIZED else self.showMaximized()
        MAXIMIZED = not MAXIMIZED

        self.ui.restore_btn.setIcon(QtGui.QIcon(':/icons/icons/win_nav/restore-white.png' if MAXIMIZED
                                                else ':/icons/icons/win_nav/window-white.png'))


    def toggle_left_menu(self):
        width = self.ui.left_side_menu.width()
        new_width = 115 if width < 50 else 47

        self.animation = QtCore.QPropertyAnimation(self.ui.left_side_menu, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()

    def apply_nav_btns_style(self):
        if self.ui.left_side_menu.width() > 50:
            self.toggle_left_menu()

        for btn in self.ui.left_side_menu.findChildren(QtWidgets.QPushButton):
            if btn.objectName() != self.sender().objectName():
                btn.setProperty("active", False)
                btn.style().polish(btn)

        self.sender().setProperty("active", True)
        self.sender().style().polish(self.sender())



    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.clicked_pos = a0.globalPos()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super(MainWindow, self).closeEvent(a0)
        ImageDriver.get_instance().close()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
