# -*- coding: utf-8 -*-

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *
# start of designer code---------------------------------------------------------------------------------
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 600)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 75, 51))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 10, 500,51))
        self.webBrowser =  QWebEngineView(Form)
        self.webBrowser.setObjectName(u"textBrowser")
        self.webBrowser.setGeometry(QRect(10, 80, 1180, 500))

#added stuff
        self.lineEdit.setText("https://www.youtube.com/watch?v=OvixR1EsrlE")



        self.pushButton.clicked.connect(self.my_action)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
# end of designer code ---------------------------------------------------------------------------------

    def my_action(self):
      #  self.textBrowser.append(self.lineEdit.text())

        url = self.lineEdit.text()
        self.webBrowser.load(QUrl(url))
        #self.lineEdit.clear()
        print("in my action")




if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    app.exec()


