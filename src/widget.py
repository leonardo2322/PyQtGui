import sys
from PyQt6.QtWidgets import QApplication, QDockWidget, QHBoxLayout, QLayout, QMainWindow, QWidget, QGridLayout,QPushButton,QLabel,QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import Fm

class Window(QMainWindow):
    def __init__(self, *arg, **kwarg):
        super(Window,self).__init__(*arg, **kwarg)
        # wid = Fm.windowbt(self)
        self.setFixedSize(1250,1000)
        self.setWindowTitle('EvaSystem')
        
        

        self.ventana = QDockWidget('ventana1',self)
        self.ventana.setFixedSize(800,400)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea,self.ventana )
        self.ventana.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)

        self.ventana2 = QDockWidget('ventana2', self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.ventana2)
        btn = QPushButton('usuarios', self.ventana)
        btn.clicked.connect(lambda:self.fm())



    def fm(self):
        vemt = Fm.windowbt()
        vemt.show()
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    root = Window()
    root.show()
    sys.exit(app.exec())