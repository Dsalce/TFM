

from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtGui import QIcon


from View.tables import *
from View.loadfilewindow import *

class MainWindow(QMainWindow):

    tableView=None
    mainMenu=None
    mainController=None
    loadFile=None

    def __init__(self, controller):
        super().__init__()
        self.mainController=controller
        self.title = 'MainWindow'
        self.left = 10
        self.top = 10
        self.width = 1920
        self.height = 1080
        self.initUI()
        
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.tableView=TableView(self.mainController)
        
        
        self.menuCreate()
        self.setCentralWidget(self.tableView) 
        
       
        
        self.show()



    def menuCreate(self):  
        self.mainMenu = self.menuBar() 
        fileMenu = self.mainMenu.addMenu('Archivo')

        loadFile=  QAction(QIcon(), 'Cargar fichero', self)
        loadFile.triggered.connect(self.lauchLoadFileWindow)
        fileMenu.addAction(loadFile)




        viewMenu = self.mainMenu.addMenu('View')
        searchMenu = self.mainMenu.addMenu('Search')
        toolsMenu = self.mainMenu.addMenu('Tools')
        helpMenu = self.mainMenu.addMenu('Help')
 
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
 
    
    def lauchLoadFileWindow(self):
      
       loadFile = LoadFileWindow(self.mainController)
       loadFile.close()
       self.tableView.createTable()
