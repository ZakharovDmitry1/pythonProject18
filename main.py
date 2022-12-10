import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PIL import Image, ImageDraw


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'untitled.ui', self)  # Загружаем дизайн
        self.btn.clicked.connect(self.hello)
        self.coeff = 1
        self.n = 0
        self.run()

    def run(self):
        pass

    def hello(self):
        try:
            self.coeff = float(self.edit1.text())
            self.n = int(self.edit2.text())
        except Exception:
            return
        im = Image.new("RGB", (300, 300), (255 - 17, 255 - 17, 255 - 17))
        drawler = ImageDraw.Draw(im)
        array = ((0, 0), (299, 0), (299, 299), (0, 299))
        for i in range(self.n):
            drawler.polygon(array, width=1, outline=(255, 0, 0))
            array = self.nextRect(*array)
        im.save('img.png')
        self.myLabel.setPixmap(QPixmap('img.png'))


    def nextRect(self, coord1: tuple, coord2: tuple, coord3: tuple, coord4: tuple) -> tuple:
        x1, y1 = coord1
        x2, y2 = coord2
        x3, y3 = coord3
        x4, y4 = coord4
        return self.newCoord((x1, y1), (x2, y2)), \
               self.newCoord((x2, y2), (x3, y3)), \
               self.newCoord((x3, y3), (x4, y4)), \
               self.newCoord((x4, y4), (x1, y1))

    def newCoord(self, first: tuple, second: tuple) -> tuple:
        x1, y1 = first
        x2, y2 = second
        newx = (int)(x1 - x2) * self.coeff + x2
        newy = (int)(y1 - y2) * self.coeff + y2
        return newx, newy


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
