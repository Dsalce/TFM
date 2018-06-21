

from PyQt5.QtWidgets import QApplication, QWidget,QMessageBox 

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


from View.tables import *
from View.loadfilewindow import *
from View.treeview import *
from View.histogram import *
from View.rulesTables import *
from View.tStudentView import *


class MainWindow(QMainWindow):

    

    def __init__(self, controller,app):
        super().__init__()
        self.app=app
        self.mainController=controller
        self.title = 'Detección de anomalias ITV'
        self.left = 50
        self.top = 50
        self.width = 1080
        self.height = 720
        
        
        self.initUI()


        
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.tableView=TableView(self.mainController)
        
         
        self.menuCreate()
        
        self.label = QLabel(self)

        self.pixmap = QPixmap('Image/itv.png')

        self.pixmap=self.pixmap.scaled(self.width, self.height)
        self.label.setPixmap(self.pixmap)
        
        self.setFixedSize(self.width, self.height)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint )
        self.setCentralWidget(self.label) 
        
        
        
        self.show()


    def setTitle(self,file):
      
      self.setWindowTitle(self.title+"---"+file)

    
     

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
        histoMARCABotton=  QAction(QIcon(), 'Histograma MARCA Y MODELO', self)
        histoGRUPBotton=  QAction(QIcon(), 'Histograma GRUP', self)
        histoCATBotton=  QAction(QIcon(), 'Histograma CAT', self)
        histoINSBotton=  QAction(QIcon(), 'Histograma INSPECTOR', self)
        histoCATBotton.triggered.connect(self.launchHistoCATView)
        histoGRUPBotton.triggered.connect(self.launchHistoGRUPView)
        histoMARCABotton.triggered.connect(self.launchHistoMARCAView)
        histoINSBotton.triggered.connect(self.launchHistoINSView)
        histoMenu.addAction(histoMARCABotton)
        histoMenu.addAction(histoGRUPBotton)
        histoMenu.addAction(histoCATBotton)
        histoMenu.addAction(histoINSBotton)



        

        ruleMenu = self.mainMenu.addMenu('Reglas de asociacion')
        ruleGRUPBotton=  QAction(QIcon(), 'Reglas  GRUP', self)
        ruleMARCABotton=  QAction(QIcon(), 'Reglas  MARCA Y MODELO', self)
        ruleCATBotton=  QAction(QIcon(), 'Reglas  CAT', self)
        ruleINSBotton=  QAction(QIcon(), 'Reglas  INSPECTOR', self)
        ruleCATBotton.triggered.connect(self.launchAsocCATView)
        ruleGRUPBotton.triggered.connect(self.launchAsocGRUPView)
        ruleMARCABotton.triggered.connect(self.launchAsocMARCAView)
        ruleINSBotton.triggered.connect(self.launchAsocINSView)
        ruleMenu.addAction(ruleGRUPBotton)
        ruleMenu.addAction(ruleMARCABotton)
        ruleMenu.addAction(ruleCATBotton)
        ruleMenu.addAction(ruleINSBotton)


        studentMenu = self.mainMenu.addMenu('T-Student')
        ruleTStudentBotton=  QAction(QIcon(), 'Calcular T-Student', self)
        ruleTStudentBotton.triggered.connect(self.launchStudentView)
        studentMenu.addAction(ruleTStudentBotton)
        
        self.status=QLabel()
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
 
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

    def updateTableCount(self,num,total):
        self.status.setText("Total : " +str(num)+"/"+str(total))
        self.statusBar.addPermanentWidget(self.status)

    
    def launchLoadFileWindow(self):
       self.setMinimumSize(1,1)
       self.setMaximumSize(QWIDGETSIZE_MAX,QWIDGETSIZE_MAX);
       self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint |Qt.WindowMaximizeButtonHint)
       self.show()

       
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


         
         
         self.setCentralWidget(self.tableView) 
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
        
          
          
          
        
    def launchHistoGRUPView (self):
        
        self.hist=Histogram(self.mainController,"GRUP")

    def launchHistoCATView (self):
        
        self.hist=Histogram(self.mainController,"CAT.")

    def launchHistoMARCAView (self):
        
        self.hist=Histogram(self.mainController,"MARCA Y MODELO")

    def launchHistoMARCAView (self):
        
        self.hist=Histogram(self.mainController,"MARCA Y MODELO")

    def launchHistoINSView (self):
        
        self.hist=Histogram(self.mainController,"INS")



    def launchAsocINSView (self):
        
        self.rule=RulesTableView(self.mainController.obtainControllerRule(),"INS")


    def launchAsocGRUPView (self):
         
        self.rule=RulesTableView(self.mainController.obtainControllerRule(),"GRUP")
         

    def launchAsocMARCAView (self):
         
        self.rule=RulesTableView(self.mainController.obtainControllerRule(),"MARCA Y MODELO")

    def launchAsocCATView (self):
         
        self.rule=RulesTableView(self.mainController.obtainControllerRule(),"CAT.")

    def launchStudentView (self):
         
        self.tstu=TStudentView(self.mainController.obtainControllerRule(),"MARCA Y MODELO")

          
        
          
         
 
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
          
          
          
          