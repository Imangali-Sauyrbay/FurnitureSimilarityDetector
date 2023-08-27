from PyQt5 import QtCore, QtGui, QtWidgets

class ScaledPixmapLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setScaledContents(True)

    def paintEvent(self, event):
        if self.pixmap():
            pm = self.pixmap()
            originalRatio = pm.width() / pm.height()
            currentRatio = self.width() / self.height()
            if originalRatio != currentRatio:
                qp = QtGui.QPainter(self)
                pm = self.pixmap().scaled(self.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                rect = QtCore.QRect(0, 0, pm.width(), pm.height())
                rect.moveCenter(self.rect().center())
                qp.drawPixmap(rect, pm)
                return
        super().paintEvent(event)