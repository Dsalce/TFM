

from PyQt5.QtWidgets import QApplication, QWidget,QMessageBox 

from PyQt5.QtGui import QIcon


from View.tables import *
from View.loadfilewindow import *
from View.treeview import *
from View.histogram import *
from View.rulesTables import *

class MainWindow(QMainWindow):

    

    def __init__(self, controller,app):
        super().__init__()
        self.app=app
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




        treeViewMenu = self.mainMenu.addMenu('Defectos')
        treeViewBotton=  QAction(QIcon(), 'Ver defectos', self)
        treeViewBotton.triggered.connect(self.launchTreeView)
        treeViewMenu.addAction(treeViewBotton)
        
        
        
        histoMenu = self.mainMenu.addMenu('Histogramas')
        histoCarBotton=  QAction(QIcon(), 'Histograma Vehiculos', self)
        histoCarBotton.triggered.connect(self.launchHistoView)
        histoMenu.addAction(histoCarBotton)

        

        ruleMenu = self.mainMenu.addMenu('Reglas de asociacion')
        ruleGRUPBotton=  QAction(QIcon(), 'Reglas  GRUP', self)
        ruleMARCABotton=  QAction(QIcon(), 'Reglas  MARCA Y MODELO', self)
        ruleCATBotton=  QAction(QIcon(), 'Reglas  CAT', self)
        ruleCATBotton.triggered.connect(self.launchAsocCATView)
        ruleGRUPBotton.triggered.connect(self.launchAsocGRUPView)
        ruleMARCABotton.triggered.connect(self.launchAsocMARCAView)
        ruleMenu.addAction(ruleGRUPBotton)
        ruleMenu.addAction(ruleMARCABotton)
        ruleMenu.addAction(ruleCATBotton)
        
 
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
 
    
    def launchLoadFileWindow(self):
      
       loadFile = LoadFileWindow(self.mainController)
       loadFile.close()
       msg = QMessageBox()

       msg.setIcon(QMessageBox.Warning)
       #msg.setWindowTitle("Error Fichero")
       msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
       if(0==loadFile.getFileErr()):
           pass
           
       elif(-1==loadFile.getFileErr()):
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
              
    def launchTreeView(self):
        

        self.treeview = TreeView(self.mainController.obtainControllerTree())
        
          
          
          
        
    def launchHistoView (self):
        
        self.hist=Histogram(self.mainController)


    def launchAsocGRUPView (self):
         
        self.rule=RulesTableView(self.mainController.obtainControllerRule(),"GRUP")
         

    def launchAsocMARCAView (self):
         
        self.rule=RulesTableView(self.mainController.obtainControllerRule(),"MARCA Y MODELO")

    def launchAsocCATView (self):
         
        self.rule=RulesTableView(self.mainController.obtainControllerRule(),"CAT.")
         
        
         
         
        
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
          
          
          
          