import sys
import os
import multiprocessing
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtGui import QFont
import math
import matplotlib

matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt


def graph(t0, x0, y0, tf, h, A, W, B, fp):
    ax = plt.axes(projection='3d')

    x_coords = []
    y_coords = []
    z_coords = []

    def func2(t0, x0, y0):
        return -A * y0 - W * x0 - B * x0 * x0 + fp * math.sin(t0)

    n = int((tf - t0) / h)
    for i in range(n):
        k1 = y0
        p1 = func2(t0, x0, y0)
        k2 = y0 + 0.5 * p1 * h
        p2 = func2(t0 + 0.5 * h, x0 + 0.5 * k1 * h, y0 + 0.5 * p1 * h)
        k3 = y0 + 0.5 * p2 * h
        p3 = func2(t0 + 0.5 * h, x0 + 0.5 * k2 * h, y0 + 0.5 * p2 * h)
        k4 = y0 + p3 * h
        p4 = func2(t0 + h, x0 + k3 * h, y0 + p3 * h)

        x_coords.append(round(t0, 6))
        y_coords.append(round(x0, 6))
        z_coords.append(round(y0, 6))

        x0 = x0 + ((h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4))
        y0 = y0 + ((h / 6.0) * (p1 + 2 * p2 + 2 * p3 + p4))
        t0 = t0 + h

    ax.plot3D(x_coords, y_coords, z_coords)
    plt.show()


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'icon1.jpg'))
        self.setGeometry(0, 0, 500, 500)
        self.setMaximumWidth(self.width())
        self.setMaximumHeight(self.height())
        self.setMinimumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setStyleSheet("background-color: #104730")
        self.setWindowTitle("Graph Plotter - Oscillator x64.exe")
        self.initUI()

    def initUI(self):
        font = QFont("Helvetica", 15)
        self.Time = QLabel(self, text="t:")
        self.Time.setGeometry(220, 20, 100, 25)
        self.Time.setStyleSheet("color: white")
        self.Time.setFont(font)

        self.X = QLabel(self, text="x:")
        self.X.setGeometry(220, 60, 100, 25)
        self.X.setStyleSheet("color: white")
        self.X.setFont(font)

        self.Y = QLabel(self, text="y:")
        self.Y.setGeometry(220, 100, 100, 25)
        self.Y.setStyleSheet("color: white")
        self.Y.setFont(font)

        self.FTime = QLabel(self, text="tf:")
        self.FTime.setGeometry(220, 140, 100, 25)
        self.FTime.setStyleSheet("color: white")
        self.FTime.setFont(font)

        self.H = QLabel(self, text="h:")
        self.H.setGeometry(220, 180, 100, 25)
        self.H.setStyleSheet("color: white")
        self.H.setFont(font)

        self.A = QLabel(self, text="α:")
        self.A.setGeometry(220, 220, 100, 25)
        self.A.setStyleSheet("color: white")
        self.A.setFont(font)

        self.B = QLabel(self, text="β:")
        self.B.setGeometry(220, 260, 100, 25)
        self.B.setStyleSheet("color: white")
        self.B.setFont(font)

        self.W = QLabel(self, text="ω:")
        self.W.setGeometry(220, 300, 100, 25)
        self.W.setStyleSheet("color: white")
        self.W.setFont(font)

        self.F = QLabel(self, text="f:")
        self.F.setGeometry(220, 340, 100, 25)
        self.F.setStyleSheet("color: white")
        self.F.setFont(font)

        self.initTimeInput = QLineEdit(self)
        self.initTimeInput.setGeometry(QtCore.QRect(250, 20, 80, 25))
        self.initTimeInput.setStyleSheet("color: skyblue")

        self.initXInput = QLineEdit(self)
        self.initXInput.setGeometry(QtCore.QRect(250, 60, 80, 25))
        self.initXInput.setStyleSheet("color: skyblue")

        self.initYInput = QLineEdit(self)
        self.initYInput.setGeometry(QtCore.QRect(250, 100, 80, 25))
        self.initYInput.setStyleSheet("color: skyblue")

        self.initFTimeInput = QLineEdit(self)
        self.initFTimeInput.setGeometry(QtCore.QRect(250, 140, 80, 25))
        self.initFTimeInput.setStyleSheet("color: skyblue")

        self.initHInput = QLineEdit(self)
        self.initHInput.setGeometry(QtCore.QRect(250, 180, 80, 25))
        self.initHInput.setStyleSheet("color: skyblue")

        self.initAInput = QLineEdit(self)
        self.initAInput.setGeometry(QtCore.QRect(250, 220, 80, 25))
        self.initAInput.setStyleSheet("color: skyblue")

        self.initBInput = QLineEdit(self)
        self.initBInput.setGeometry(QtCore.QRect(250, 260, 80, 25))
        self.initBInput.setStyleSheet("color: skyblue")

        self.initWInput = QLineEdit(self)
        self.initWInput.setGeometry(QtCore.QRect(250, 300, 80, 25))
        self.initWInput.setStyleSheet("color: skyblue")

        self.initFInput = QLineEdit(self)
        self.initFInput.setGeometry(QtCore.QRect(250, 340, 80, 25))
        self.initFInput.setStyleSheet("color: skyblue")

        self.startB = QtWidgets.QPushButton(self, text="START")
        self.startB.setGeometry(QtCore.QRect(215, 380, 70, 30))
        self.startB.setStyleSheet("color: white; border: solid white; border-width: 4px")
        self.startB.clicked.connect(self.start_button)

        self.clearB = QtWidgets.QPushButton(self, text="CLEAR")
        self.clearB.setGeometry(QtCore.QRect(215, 420, 70, 30))
        self.clearB.setStyleSheet("color: white; border: solid white; border-width: 4px")
        self.clearB.clicked.connect(self.clear_button)

    def start_button(self):
        t0 = float(self.initTimeInput.text() or 0)
        x0 = float(self.initXInput.text() or 0.01)
        y0 = float(self.initYInput.text() or 0.01)
        tf = float(self.initFTimeInput.text() or 100)
        h = float(self.initHInput.text() or 0.1)
        A = float(self.initAInput.text() or 0.5)
        W = float(self.initWInput.text() or -1)
        B = float(self.initBInput.text() or 0.2)
        fp = float(self.initFInput.text() or 2)

        # graph(t0,x0,y0,tf,h,A,W,B,fp,)

        x = multiprocessing.Process(target=graph, args=(t0, x0, y0, tf, h, A, W, B, fp,))
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
    win = Window()
    win.show()
    sys.exit(app.exec())
