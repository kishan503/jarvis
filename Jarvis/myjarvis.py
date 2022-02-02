from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from JarvisUi import Ui_MainWindow
import sys
import jarvis

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.task_gui()
    
    def task_gui(self):
        jarvis.taskexicution()

startFunctions = MainThread()

class GuiStart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)
        self.jarvis_ui.startpushButton.clicked.connect(self.startFunc)
        self.jarvis_ui.stoppushButton.clicked.connect(self.close)

    def startFunc(self):

        self.jarvis_ui.movies = QtGui.QMovie("D:/jarvis material/Gif1.gif")
        self.jarvis_ui.Gif1.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()

        self.jarvis_ui.movies_2 = QtGui.QMovie("D:/jarvis material/Gif2.gif")
        self.jarvis_ui.Gif2.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_3 = QtGui.QMovie("D:/jarvis material/Gif3.gif")
        self.jarvis_ui.Gif3.setMovie(self.jarvis_ui.movies_3)
        self.jarvis_ui.movies_3.start()

        self.jarvis_ui.movies_4 = QtGui.QMovie("D:/jarvis material/Gif4.gif")
        self.jarvis_ui.Gif4.setMovie(self.jarvis_ui.movies_4)
        self.jarvis_ui.movies_4.start()

        self.jarvis_ui.movies_5 = QtGui.QMovie("D:/jarvis material/Gif5.gif")
        self.jarvis_ui.Gif5.setMovie(self.jarvis_ui.movies_5)
        self.jarvis_ui.movies_5.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)

        startFunctions.start()
    
    def showtime(self):
        
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)

        self.jarvis_ui.timetextBrowser.setText(label_time)
        self.jarvis_ui.datetextBrowser.setText(label_date)

app = QApplication(sys.argv) 

app_jarvis = GuiStart()

app_jarvis.show()

exit(app.exec_())


