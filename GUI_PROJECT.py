import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtGui import QFont,QPixmap 
import math
import matplotlib
matplotlib.use("qt5agg")
import matplotlib.pyplot as plt
import os 
import multiprocessing

def graph(t0,x0,y0,tf,h,A,W,B,fp):

    ax = plt.axes(projection = '3d')

    xquards = []
    yquards = []
    zquards = []

    def func1(y0):
        return y0

    def func2(t0,x0,y0):
        return -A*y0-W*x0-B*x0*x0+fp*math.sin(t0)

    n = int((tf-t0)/h)
    for i in range(n):
        k1 = func1(y0)
        p1=func2(t0,x0,y0)
        k2=func1(y0+0.5*p1*h)
        p2=func2(t0+0.5*h,x0+0.5*k1*h,y0+0.5*p1*h)
        k3=func1(y0+0.5*p2*h)
        p3=func2(t0+0.5*h,x0+0.5*k2*h,y0+0.5*p2*h)
        k4=func1(y0+p3*h)
        p4=func2(t0+h,x0+k3*h,y0+p3*h)   

        t0 = round(t0,6)
        x0 = round(x0,6)
        y0 = round(y0,6)
         
        xquards.append(t0)
        yquards.append(x0)
        zquards.append(y0)

        x0=x0+((h/6.0)*(k1+2*k2+2*k3+k4));
        y0=y0+((h/6.0)*(p1+2*p2+2*p3+p4));
        t0=t0+h;

    for i in range(len(xquards)):
        print(f"{xquards[i]} {yquards[i]} {zquards[i]}")

    ax.plot3D(xquards,yquards,zquards)
    plt.show()

class dappa(QMainWindow):
    def __init__(self):
        super(dappa, self).__init__()
        self.psglogo = QPixmap('psglogo.jpeg')
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'icon1.jpg'))
        self.setGeometry(0,0,500,400)
        self.setMaximumWidth(self.width())
        self.setMaximumHeight(self.height())
        self.setMinimumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setStyleSheet("background-image: url(D:/Project/GIT HUB/bg1.jpg); background-attachment: fixed")
        self.setWindowTitle("Graph Plotter - Oscillator x64.exe")
        self.initUI()

    def initUI(self):
        self.Time = QLabel(self, text = "t0:")
        self.Time.setGeometry(220,20,100,25)
        self.Time.setStyleSheet("color: white")
        self.Time.setFont(QFont('Helvetica', 15))

        self.X = QLabel(self, text = "x0:")
        self.X.setGeometry(220,50,100,25)
        self.X.setStyleSheet("color: white")
        self.X.setFont(QFont('Helvetica', 15))

        self.Y = QLabel(self, text = "y0:")
        self.Y.setGeometry(220,80,100,25)
        self.Y.setStyleSheet("color: white")
        self.Y.setFont(QFont('Helvetica', 15))

        self.FTime = QLabel(self, text = "tf :")
        self.FTime.setGeometry(220,110,100,25)
        self.FTime.setStyleSheet("color: white")
        self.FTime.setFont(QFont('Helvetica', 15))

        self.H = QLabel(self, text = "h :")
        self.H.setGeometry(220,140,100,25)
        self.H.setStyleSheet("color: white")
        self.H.setFont(QFont('Helvetica', 15))

        self.A = QLabel(self, text = "A :")
        self.A.setGeometry(220,170,100,25)
        self.A.setStyleSheet("color: white")
        self.A.setFont(QFont('Helvetica', 15))

        self.B = QLabel(self, text = "B :")
        self.B.setGeometry(220,200,100,25)
        self.B.setStyleSheet("color: white")
        self.B.setFont(QFont('Helvetica', 15))

        self.W = QLabel(self, text = "W:")
        self.W.setGeometry(220,230,100,25)
        self.W.setStyleSheet("color: white")
        self.W.setFont(QFont('Helvetica', 15))

        self.F = QLabel(self, text = "F :")
        self.F.setGeometry(220,260,100,25)
        self.F.setStyleSheet("color: white")
        self.F.setFont(QFont('Helvetica', 15))

        self.initTimeInput = QLineEdit(self)
        self.initTimeInput.setGeometry(QtCore.QRect(250, 20, 40, 20))
        self.initTimeInput.setStyleSheet("color: skyblue")

        self.initXInput = QLineEdit(self)
        self.initXInput.setGeometry(QtCore.QRect(250, 50, 40, 20))
        self.initXInput.setStyleSheet("color: skyblue")
        
        self.initYInput = QLineEdit(self)
        self.initYInput.setGeometry(QtCore.QRect(250, 80, 40, 20))
        self.initYInput.setStyleSheet("color: skyblue")

        self.initFTimeInput = QLineEdit(self)
        self.initFTimeInput.setGeometry(QtCore.QRect(250, 110, 40, 20))
        self.initFTimeInput.setStyleSheet("color: skyblue")

        self.initHInput = QLineEdit(self)
        self.initHInput.setGeometry(QtCore.QRect(250, 140, 40, 20))
        self.initHInput.setStyleSheet("color: skyblue")

        self.initAInput = QLineEdit(self)
        self.initAInput.setGeometry(QtCore.QRect(250, 170, 40, 20))
        self.initAInput.setStyleSheet("color: skyblue")

        self.initBInput = QLineEdit(self)
        self.initBInput.setGeometry(QtCore.QRect(250, 200, 40, 20))
        self.initBInput.setStyleSheet("color: skyblue")

        self.initWInput = QLineEdit(self)
        self.initWInput.setGeometry(QtCore.QRect(250, 230, 40, 20))
        self.initWInput.setStyleSheet("color: skyblue")

        self.initFInput = QLineEdit(self)
        self.initFInput.setGeometry(QtCore.QRect(250, 260, 40, 20))
        self.initFInput.setStyleSheet("color: skyblue")

        self.startB = QtWidgets.QPushButton(self, text="START")
        self.startB.setGeometry(QtCore.QRect(215, 300, 70, 30))
        self.startB.setStyleSheet("color: white; border: solid white; border-width: 4px;")
        self.startB.clicked.connect(self.start_button)

        self.clearB = QtWidgets.QPushButton(self, text="CLEAR")
        self.clearB.setGeometry(QtCore.QRect(215, 340, 70, 30))
        self.clearB.setStyleSheet("color: white; border: solid white; border-width: 4px")
        self.clearB.clicked.connect(self.clear_button)

    def start_button(self):
        t0 = float(self.initTimeInput.text() or 0)
        x0 = float(self.initXInput.text() or 0)
        y0 = float(self.initYInput.text() or 0)
        tf = float(self.initFTimeInput.text() or 0)
        h  = float(self.initHInput.text() or 1)
        A  = float(self.initAInput.text() or 0)
        W  =float(self.initWInput.text() or 0)
        B  =float(self.initBInput.text() or 0)
        fp =float(self.initFInput.text() or 0)     
        
        
        #graph(t0,x0,y0,tf,h,A,W,B,fp,)

        x = multiprocessing.Process(target = graph, args =(t0,x0,y0,tf,h,A,W,B,fp,))
        x.start()

    def clear_button(self):
        self.initTimeInput.clear()
        self.initXInput.clear()
        self.initYInput.clear()
        self.initFTimeInput.clear()
        self.initHInput.clear()
        self.initAInput.clear()
        self.initWInput.clear()
        self.initBInput.clear()
        self.initFInput.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = dappa()
    win.show()
    sys.exit(app.exec())
        
