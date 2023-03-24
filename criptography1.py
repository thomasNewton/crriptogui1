from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap, QPainter, QBrush, QColor

def rot(original, key):
    rotated = ''

    for character in original:
        rotated += chr(ord(character) + key)
    return rotated


def unrot(cypher_text, key):
    original = ""
    for character in cypher_text:
        original += chr(ord(character) - key)
    return original






class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(901, 1131)
        Form.setStyleSheet(u"color:rgb(15, 7, 112);\n"
"background-color: rgb(221, 255, 240);\n"
"font: 20pt \"Sitka Heading\";")

        icon = QIcon()
        icon.addFile(u"usmc.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)

        pixmap = QPixmap("usmc.jpg")
        background_label = QLabel(Form)
        background_label.setPixmap(pixmap)
        background_label.setGeometry(400, 0, 1200, 1800)








        self.key = 13
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 70, 631, 241))
        self.textEdit.setStyleSheet(u"color:rgb(125, 27, 58);\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit_2 = QTextEdit(Form)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 390, 631, 241))
        self.textEdit_2.setStyleSheet(u"border-color: rgb(255, 69, 56);\n"
"color: rgb(0, 0, 98);\n"
"background-color: rgb(255, 255, 229);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 441, 51))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 330, 441, 51))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 650, 441, 51))
        self.textEdit_3 = QTextEdit(Form)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(0, 710, 631, 241))
        self.textEdit_3.setStyleSheet(u"color: rgb(14, 5, 115);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalScrollBar = QScrollBar(Form)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(840, 90, 20, 1021))
        self.verticalScrollBar.setMaximum(256)
        self.verticalScrollBar.setSliderPosition(13)
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(660, 10, 211, 51))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(640, 440, 161, 91))
        self.retranslateUi(Form)
        self.verticalScrollBar.valueChanged.connect(self.key_update)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle("Ceaser Cyphers")
        self.label.setText("Original Text")
        self.label_2.setText("Encoded Text")
        self.label_3.setText("Decoded Text ")
        self.label_4.setText("Set Key 0-256")
        self.label_5.setText("Key "+str(self.key))
        self.label_5.setGeometry(QRect(658, 445, 71, 81))
        self.label_5.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(660, 80, 91, 41))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit.setText(str(self.key))
        self.lineEdit.textChanged.connect(self.label_update)

    def label_update(self):  # action if triggered by changing the text area
        self.key = int(self.lineEdit.text())
        self.label_5.setText("Key " + str(self.key))
        self.verticalScrollBar.setValue(self.key)
        self.encode()
        self.decode()

    def key_update(self):   # action if triggered by changing the slider
        self.key=self.verticalScrollBar.value()
        self.label_5.setText("Key "+str(self.key))
        self.lineEdit.setText(str(self.key))
        print(self.key)
        self.encode()
        self.decode()

    def encode(self):
        raw = self.textEdit.toPlainText()
        self.textEdit_2.setText(rot(raw, self.key))
        # self.textEdit.clear()
        print("in encode")

    def decode(self):
        cypher_text = self.textEdit_2.toPlainText()
        self.textEdit_3.setText(unrot(cypher_text, self.key))


app = QApplication([])
window = QMainWindow()
ui = Ui_Form()
ui.setupUi(window)
window.show()
app.exec()
