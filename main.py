import sys
import random

from PyQt5.QtCore import Qt, QPoint, QPointF
from PyQt5.QtGui import QPainter, QColor, QPainterPath, QMouseEvent, QCursor, \
    QScreen
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 186, 0))
        # (x1 - x2) ** 2 + (y1 - y2) ** 2 > (r1 + r2) ** 2
        src = []
        for i in range(random.randint(2, 5)):
            data = [random.randint(10, self.height() // 3),
                    random.randint(10, self.width()) // 3]
            x1, y1 = data
            r = random.randint(10, 100)
            while any((x1 - x2) ** 2 + (y1 - y2) ** 2 < (r + r2) ** 2 for (x2, y2, r2) in src):
                data = [random.randint(10, self.height() // 3),
                        random.randint(10, self.width()) // 3]
                x1, y1 = data
                r = random.randint(10, 100)

            qp.drawEllipse(data[0] - r // 2, data[1] - r // 2, r, r)
            src.append((data[0], data[1], r))

    def paint(self):
        self.do_paint = True
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())