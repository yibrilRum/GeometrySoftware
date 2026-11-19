from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("Interior design tool")
window.setGeometry(100, 100, 800, 600)

label = QLabel("Hello interior design", parent=window)
label.move(50, 50)

window.show()
app.exec_()
