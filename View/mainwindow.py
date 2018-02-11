

from PyQt5.QtWidgets import QApplication, QWidget,QMessageBox 

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
        self.width = 920
        self.height = 780
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
        loadFile.triggered.connect(self.launchLoadFileWindow)
        fileMenu.addAction(loadFile)

        exportFile=  QAction(QIcon(), 'Exportar fichero', self)
        exportFile.triggered.connect(self.launchExportFileCSV)
        fileMenu.addAction(exportFile)




        viewMenu = self.mainMenu.addMenu('View')
        searchMenu = self.mainMenu.addMenu('Search')
        toolsMenu = self.mainMenu.addMenu('Tools')
        helpMenu = self.mainMenu.addMenu('Help')
 
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
 
    
    def launchLoadFileWindow(self):
      
       loadFile = LoadFileWindow(self.mainController)
       loadFile.close()
       msg = QMessageBox()

       msg.setIcon(QMessageBox.Warning)
       msg.setWindowTitle("Error Fichero")
       msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

       if(-1==loadFile.getFileErr()):
            msg.setText("No es posible leer el fichero asegurese de que los datos son correctos")
            msg.exec_()
       elif(1==loadFile.getFileErr()):
             msg.setText("Fichero con formato erroneo \n" +
              "  introduzca un fichero con formato: .csv,.txt,.xlsx")
             
             msg.exec_()
       else:
         self.tableView.createTable()


    def launchExportFileCSV(self):
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Warning)
          msg.setWindowTitle("Error Fichero")
          msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
          exp=self.mainController.exportFileCSV()
          if(exp==-1):
              msg.setText("Error al exportar en CSV")
              msg.exec_()

          else:
              msg.setText("Fichero exportado correctamente")
              msg.exec_()
    
    
