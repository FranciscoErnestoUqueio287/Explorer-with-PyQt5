from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.la = QLabel("Movie will be here")
        layout.addWidget(self.la,0,0)
        self.n = QPushButton("Play")
        layout.addWidget(self.n,1,0)
        self.n.clicked.connect(self.play)
    def play(self):
        e = QFileDialog()
        v = e.getOpenFileName()
        if len(v) > 3:
            self.m = QMovie(v)
            self.la.setMovie(m)
            
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
