from PyQt6.QtWidgets import  QWidget, QGridLayout,QPushButton,QLabel,QLineEdit
from PyQt6.QtGui import QIcon, QPixmap

class Windowbt2(QWidget):
    def __init__(self, *arg, **kwarg):
        super(Windowbt2,self).__init__(*arg, **kwarg)
        self.setFixedSize(400,200)

#--------------------btn-----------------------------------------
        btn_show = QPushButton('Usuarios')
        btn_show.setIcon(QIcon('img/user.svg'))
        self.btn_Options = QPushButton('Opciones')
        self.btn_Options.setIcon(QIcon('img/example.svg'))
#----------------------titles-------------------------------------            
        show_text= QLabel('esto es una prueba')
#-----------------------entryes-----------------------------------            
        entry = QLineEdit()
#------------------------layaout----------------------------------
        layout = QGridLayout(self)
        layout.addWidget(btn_show,0,0)
        layout.addWidget(show_text,1,0)
        layout.addWidget(entry,1,1)
        layout.addWidget(self.btn_Options,2,0)