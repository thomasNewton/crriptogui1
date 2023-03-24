import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("Web Renderer")
        self.setFixedSize(600, 600)

        # Create a text input widget for the URL
        self.url_input = QLineEdit(self)
        self.url_input.setGeometry(10, 10, 580, 30)

        # Create a button to trigger the URL load
        self.load_button = QPushButton("Load", self)
        self.load_button.setGeometry(500, 50, 90, 30)
        self.load_button.clicked.connect(self.load_url)

        # Create a QWebEngineView widget to render the web page
        self.webview = QWebEngineView(self)
        self.webview.setGeometry(10, 90, 580, 500)

    def load_url(self):
        # Get the URL from the text input
        url = self.url_input.text()

        # Load the URL into the QWebEngineView widget
        self.webview.load(QUrl(url))

if __name__ == '__main__':
    # Create the Qt application and the main window
    app = QApplication(sys.argv)
    window = MainWindow()

    # Show the main window and start the Qt event loop
    window.show()
    sys.exit(app.exec_())
