
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MyButtonWidget(QWidget):



    def __init__(self):
        super().__init__()

        button = QPushButton("Animated Button", self)
        anim = QPropertyAnimation(button, "pos", self)
        anim.setDuration(10000)
        anim.setStartValue(QPoint(0, 0))
        anim.setEndValue(QPoint(100, 250))
        anim.start()

if __name__ == "__main__":

    a = QApplication()
    buttonAnimWidget = MyButtonWidget()
    buttonAnimWidget.resize(QSize(800, 600))
    buttonAnimWidget.show()
    a.exec()