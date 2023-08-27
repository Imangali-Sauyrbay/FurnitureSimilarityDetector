from PyQt5 import QtCore, QtWidgets, QtGui

from ui.windows.image_window import Ui_MainWindow
from web_driver.chrome import ImageDriver
from configs import Config

class ShowResult(QtWidgets.QMainWindow):
    onClose = QtCore.pyqtSignal()

    def __init__(self, answers, suffix,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.answers = answers
        self.suffix = suffix
        self.candidates = []
        self.config = Config.get_instance()

        self.current_i = 0

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.img_driver = ImageDriver.get_instance()

        self.ui.close_btn.clicked.connect(lambda: self.close())
        self.ui.next_btn.clicked.connect(lambda: QtCore.QTimer.singleShot(10, self.next_object))
        self.ui.refresh_btn.clicked.connect(lambda: QtCore.QTimer.singleShot(10, self.next))



        def moveWindow(e):
            if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clicked_pos)
                self.clicked_pos = e.globalPos()
                e.accept()

        self.ui.header_frame.mouseMoveEvent = moveWindow

        self.show()
        self.process_objects()
        def load():
            self.load_data()
            self.next_img()
            self.update_screen()
        QtCore.QTimer.singleShot(100, load)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.clicked_pos = a0.globalPos()

    def next_object(self):
        if self.current_i < (len(self.candidates) - 1):
            self.current_i += 1
        else:
            self.current_i = 0
        self.load_data()
        self.next_img()
        self.update_screen()

    def next(self):
        self.next_img()
        self.update_screen()

    def load_data(self):
        self.img_driver.load_page(self.candidates[self.current_i]['name'] + ' ' + self.suffix)

    def next_img(self):
        self.curr_data = self.img_driver.next_image()

    def update_screen(self):
        self.ui.name.setText('<a href="{0}" style="color: white; text-decoration: none;">{1} (Сходство: {2}%)</a>'.format(
            self.curr_data[1],
            self.candidates[self.current_i]['alias'],
            self.candidates[self.current_i]['percent']))

        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.curr_data[0])
        pixmap.scaledToWidth(self.ui.photo.width())
        self.ui.photo.setPixmap(pixmap)

    def process_objects(self):
        furnitures = self.config.get('furnitures')

        for furniture in furnitures:
            temp = {}
            temp['name'] = furniture['name']
            temp['alias'] = furniture['alias']

            occassions = 0
            for answer in self.answers:
                if answer in furniture['tags']:
                    occassions += 1

            temp['percent'] = int((occassions / len(furniture['tags'])) * 100)
            self.candidates.append(temp)

        self.candidates.sort(reverse=True, key=lambda i: i['percent'])

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super(ShowResult, self).closeEvent(a0)
        self.onClose.emit()