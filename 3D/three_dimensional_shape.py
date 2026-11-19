from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class DrawingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wireframe Viewer")
        self.setGeometry(100, 100, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black, 2)
        painter.setPen(pen)

        painter.drawRect(100, 100, 400, 300)

        painter.drawRect(200, 200, 100, 50)

if __name__ == "__main__":
    app = QApplication([])
    window = DrawingWindow()
    window.show()
    app.exec_()
