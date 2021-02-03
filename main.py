import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from ui_main import Ui_MainWindow
import os
from ui_functions import *
import pyttsx3
engine = pyttsx3.init()
import pyautogui
import mqttbridge as mb
from time import sleep

class soundplayingbuttons(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.text = ''
        self.soundmode = 1

    def run(self):
        engine.stop()
        if(self.soundmode):
            self.text = self.text + ' mode activated'
            engine.say(self.text)
            engine.runAndWait()

class soundplayingstatus(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.text = ''
        self.soundmode = 1

    def run(self):
        engine.stop()
        if(self.soundmode):
            engine.say(self.text)
            engine.runAndWait()

class movemouse(QThread):
    def __init__(self):
        QThread.__init__(self)
        lis = []
        self.data = ''
        self.ch = ''
        pyautogui.FAILSAFE=False
    
    def get_data(self):
        self.data = mb.message
    
    def run(self):
        while True:
            if(self.ch == '1'):
                self.get_data()
                self.lis = self.data.split()
                if(len(self.lis) != 0):
                    print(self.lis)
        
                    xi = self.lis[0]
                    yi = self.lis[1]
                    ai = self.lis[2]
                    bi = self.lis[3]
                    #bi = int(bi)
                    #bi = 1 - bi

                    x=int(xi)
                    y=int(yi)
        
                    if self.data:
                        pyautogui.moveTo(x,y)
                        if '1' in ai:
                            pyautogui.click()
                        if bi == '1':
                            pyautogui.click(button = 'right')

class openfile(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.filename = ''
    
    def run(self):
        os.system(self.filename)
        sleep(10)

class labviewmode(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.labviewon = 0
        self.message1 = ''
        
    
    def run(self):
        while(True):
            if(self.labviewon):
                f = open('test.txt','w')
                self.message1 = mb.message
                print(self.message1)
                f.write(self.message1)
                f.close()
                sleep(0.5)

class modecheckbutton(QThread):
    signal = pyqtSignal(int)
    def __init__(self):
        QThread.__init__(self)
        self.lis = []
        self.flag = 0

    def get_data(self):
        self.data = mb.message
    
    def run(self):
        while True:
            self.get_data()
            self.lis = self.data.split()
            if(len(self.lis) != 0):
                print(self.lis)
                ai = self.lis[2]
                bi = self.lis[3]
                #bi = int(bi)
                #bi = 1 - bi

                if self.data:
                    if '1' in ai and bi =='1':
                        self.flag = self.flag+1
                        #self.signal.emit(1)
                        sleep(1)
                    else:
                        self.flag = 0
                        
                if self.flag >= 5:
                    #print('Flag is actvated')
                    self.signal.emit(1)
                    self.flag = 0
                    #sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mode = 'OFF'
        self.sound = 1
        self.voice = 0
        
        self.soundplayerbtn = soundplayingbuttons()
        self.soundplayerstatus = soundplayingstatus()
        self.mouse = movemouse()
        self.openingfile = openfile()
        self.labviewfilehandling = labviewmode()
        self.modecheckbtn = modecheckbutton()
        self.modecheckbtn.signal.connect(self.modechange)
        self.modecheckbtn.start()


        def moveWindow(event):
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.titl_frame.mouseMoveEvent = moveWindow
        
        UIFunctions.uiDefinitions(self)

        self.show()

 
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def modeupdate(self):
        if(self.ui.off.isChecked()):
            self.mode = 'OFF'
            self.mouse.ch = '0'
            self.labviewfilehandling.labviewon = 0
            self.labviewfilehandling.terminate()
            self.mouse.terminate()
        if(self.ui.normal.isChecked()):
            self.mode = 'Normal'
            self.mouse.ch = '1'
            self.labviewfilehandling.labviewon = 0
            self.labviewfilehandling.terminate()
            self.mouse.start()
        if(self.ui.labview.isChecked()):
            self.mode = 'LabView'
            self.mouse.ch = '0'
            self.labviewfilehandling.labviewon = 1
            self.mouse.terminate()
            self.labviewfilehandling.start()
        self.ui.mode.setText(self.mode)
        #self.soundplayerbtn.terminate()
        self.soundplayerbtn.text = self.mode
        self.soundplayerbtn.start()
    
    def soundsettings(self):
        if(self.ui.soundon.isChecked()):
            self.sound = 1
        if(self.ui.soundoff.isChecked()):
            self.sound = 0
        self.soundplayerstatus.soundmode = self.sound
        self.soundplayerbtn.soundmode = self.sound
        print(self.sound)

    '''def voicesettings(self):
        global morf
        global voice
        if(self.ui.voicemale.isChecked()):
            morf = 0
        if(self.ui.voicefemale.isChecked()):
            morf = 1
        print(morf)
        engine.setProperty('voice', voices[morf].id)'''

    def getfiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\Users\\HariK\\Desktop\\',"Labview (*.vi *.VI)")
        self.ui.recentfile.setText(fname[0])
        command = str(fname[0])
        self.openingfile.filename = command
        self.openingfile.start()
        
    def recentfiles(self):
        recentfilepath = self.ui.recentfile.text()
        command = str(recentfilepath)
        self.openingfile.filename = command
        self.openingfile.start()
    
    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self.stop = True
            print(object.text())
            self.soundplayerstatus.text = object.text()
            self.soundplayerstatus.start()
            return True
        elif event.type() == QEvent.Leave:
            self.stop = False
        return False

    def modechange(self,result):
        if(self.ui.off.isChecked()):
            self.mode = 'Normal'
            self.mouse.ch = '1'
            self.ui.normal.setChecked(True)
            self.labviewfilehandling.labviewon = 0
            self.labviewfilehandling.terminate()
            self.mouse.start()
        else:
            if(self.ui.normal.isChecked()):
                self.mode = 'LabView'
                self.mouse.ch = '0'
                self.ui.labview.setChecked(True)
                self.labviewfilehandling.labviewon = 1
                self.mouse.terminate()
                self.labviewfilehandling.start()
            else:
                if(self.ui.labview.isChecked()):
                    self.mode = 'OFF'
                    self.mouse.ch = '0'
                    self.ui.off.setChecked(True)
                    self.labviewfilehandling.labviewon = 0
                    self.labviewfilehandling.terminate()
                    self.mouse.terminate()
        
        #self.modecheck.terminate()
        self.ui.mode.setText(self.mode)
        #self.soundplayerbtn.terminate()
        self.soundplayerbtn.text = self.mode
        self.soundplayerbtn.start()
  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
