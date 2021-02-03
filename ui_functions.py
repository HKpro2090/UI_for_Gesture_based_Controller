from main import *
GLOBAL_STATE = 0

class UIFunctions(MainWindow):
    '''
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()

            GLOBAL_STATE = 1
            
            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            #self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maxmise.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            #self.ui.frame.setContentsMargins(10, 10, 10, 10)
            #self.ui.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 10px;")
            self.ui.btn_maxmise.setToolTip("Maximize")
        '''
    def uiDefinitions(self):

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #self.ui.btn_maxmise.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.btn_minimise.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.openfile.clicked.connect(self.getfiles)
        self.ui.openrecent.clicked.connect(self.recentfiles)
        self.ui.off.clicked.connect(self.modeupdate)
        self.ui.normal.clicked.connect(self.modeupdate)
        self.ui.labview.clicked.connect(self.modeupdate)
        self.ui.soundon.setChecked(True)
        self.ui.soundon.clicked.connect(self.soundsettings)
        #self.ui.voicemale.clicked.connect(self.voicesettings)
        #self.ui.voicefemale.clicked.connect(self.voicesettings)
        self.ui.soundoff.clicked.connect(self.soundsettings)
        self.ui.Pagetitle.installEventFilter(self)
        self.ui.batterypercentage.installEventFilter(self)
        self.ui.batteryhealth.installEventFilter(self)
        self.ui.Connectionid.installEventFilter(self)
        self.ui.ConnectionDataRate.installEventFilter(self)
        self.ui.ConnectionType.installEventFilter(self)
        self.ui.tabWidget.removeTab(1)

    def returnStatus():
        return GLOBAL_STATE
