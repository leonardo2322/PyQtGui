import sys
from PyQt6.QtWidgets import (
    QApplication,
    QDockWidget,
    QHBoxLayout,
    QLayout,
    QMainWindow,
    QWidget,
    QGridLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QTabWidget,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import Fm


class Window(QWidget):
    def __init__(self, *arg, **kwarg):
        super(Window, self).__init__(*arg, **kwarg)
        # wid = Fm.windowbt(self)
        self.setFixedSize(1250, 1000)
        self.setWindowTitle("EvaSystem")

        btn = QPushButton("usuarios")

        saludo = print("click")
        winds = QTabWidget()
        btn.clicked.connect(lambda: saludo)
        self.texttitle = QLabel("Proyect gui")
        layout = QHBoxLayout()
        layout.addWidget(self.texttitle)
        layout.addWidget(btn)
        layout.addWidget(winds)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = Window()
    root.show()
    sys.exit(app.exec())
