
"""Main window view"""

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

    
    #Constructor
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
        #Only available minimize window or close
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint )
        self.setCentralWidget(self.label) 
        
        
        
        self.show()

   #Set title
    def setTitle(self,file):
      
      self.setWindowTitle(self.title+"---"+file)

    
     
    #Menu of the application
    def menuCreate(self):  
        self.mainMenu = self.menuBar() 
        fileMenu = self.mainMenu.addMenu('Archivo')

        #Load window menu
        loadFile=  QAction(QIcon(), 'Cargar fichero', self)
        loadFile.triggered.connect(self.launchLoadFileWindow)
        fileMenu.addAction(loadFile)

        #Export file
        exportFile=  QAction(QIcon(), 'Exportar fichero', self)
        exportFile.triggered.connect(self.launchExportFileCSV)
        fileMenu.addAction(exportFile)


 
        #Ver defectos menu
        treeViewMenu = self.mainMenu.addMenu('Defectos')
        treeViewBotton=  QAction(QIcon(), 'Ver defectos', self)
        treeViewBotton.triggered.connect(self.launchTreeView)
        treeViewMenu.addAction(treeViewBotton)
        
        
        #Histogram menu
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



        
        #Rule menu
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

        #Test Menu
        studentMenu = self.mainMenu.addMenu('Test estadísticos')
        ruleTStudentBotton=  QAction(QIcon(), 'Calcular test', self)
        ruleTStudentBotton.triggered.connect(self.launchStudentView)
        studentMenu.addAction(ruleTStudentBotton)
        
        self.status=QLabel()
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        #Exit button menu
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
    
    #Update the main count of the table elements
    def updateTableCount(self,num,total):
        self.status.setText("Total : " +str(num)+"/"+str(total))
        self.statusBar.addPermanentWidget(self.status)
 
    #Load window action
    def launchLoadFileWindow(self):
       self.setMinimumSize(1,1)
       self.setMaximumSize(QWIDGETSIZE_MAX,QWIDGETSIZE_MAX);
       self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint |Qt.WindowMaximizeButtonHint)
       self.show()

       
       loadFile = LoadFileWindow(self.mainController)
       loadFile.close()
       msg = QMessageBox()

       msg.setIcon(QMessageBox.Warning)
      
       msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

       #If it is an error in load process
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
         

    #Function to export the table data to a .csv file
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




    #Launch the view of defects          
    def launchTreeView(self):
        
        self.treeview = TreeView(self.mainController.obtainControllerTree())
        
    #Launch histogram of GRUP type      
    def launchHistoGRUPView (self):
        
        self.hist=Histogram(self.mainController,"GRUP")

    #Launch histogram of CAT type  
    def launchHistoCATView (self):
        
        self.hist=Histogram(self.mainController,"CAT.")

    #Launch histogram of Model type  
    def launchHistoMARCAView (self):
        
        self.hist=Histogram(self.mainController,"MARCA Y MODELO")

    #Launch histogram of Inspector type  
    def launchHistoINSView (self):
        
        self.hist=Histogram(self.mainController,"INS")

    #Launch rule view of Inspector   
    def launchAsocINSView (self):
        
        self.rule=RulesTableView(self.mainController.obtainControllerRule(),"INS")

    #Launch rule view of GRUP
    def launchAsocGRUPView (self):
         
        self.rule=RulesTableView(self.mainController.obtainControllerRule(),"GRUP")
         
    #Launch rule view of Model
    def launchAsocMARCAView (self):
         
        self.rule=RulesTableView(self.mainController.obtainControllerRule(),"MARCA Y MODELO")

    #Launch rule view of Category
    def launchAsocCATView (self):
         
        self.rule=RulesTableView(self.mainController.obtainControllerRule(),"CAT.")
   
    #Launch the the view
    def launchStudentView (self):
         
        self.tstu=TStudentView(self.mainController.obtainControllerRule(),"MARCA Y MODELO")

          
        
          
         
 
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
          
          
          
          