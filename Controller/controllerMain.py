"""
Main class controller of the  main window

"""


from View.mainwindow import *
from Parser.parserTXT import *
from Parser.parserCSV import *
from Parser.parser import *
from Parser.parserXLSX import *
from Model.itv import *
from Controller.controllerTreeView import *
from Controller.controllerRules import *

class MainController(object):
   
    #Constructor
    def __init__(self):

        self.file=""
        #launch the view in the application
        app = QApplication(sys.argv)
        self.itv=itv()
        self.parser=Parser()
        self.cTree=None
        self.cRules=None
        #Instance of the main window
        self.mainWindow = MainWindow(self,app)
        sys.exit(app.exec_())
        
    #Function to load the type of file that the user select
    def loadFileTxt(self,file):
        self.itv=itv()
        aux="/"
        i=file.rfind("/")
        fileName=file[ i+1:]
        try:
         
         if("TXT"in file.upper()):
         
          self.file=file
          self.parser=ParserTXT()
          self.createModel(file)
          self.mainWindow.setTitle(fileName)
         
         elif("XLSX" in file.upper()):
          self.file=file
          self.parser=ParserXLSX()
          self.createModel(file)
          self.mainWindow.setTitle(fileName)
          
         elif("CSV" in file.upper()):
          self.file=file
          self.parser=ParserCSV()
          self.createModel(file)
          self.mainWindow.setTitle(fileName)

         elif(file==""):
             return 0
         else:
          return 1
        except OSError:
          return -1

    #Call a function to export the table to a .csv file
    def exportFileCSV(self):
       try:
        if(self.file!=""):
         self.parser.exportCSV(self.file)
        else:
          return -1 
       except OSError:
        return -1
    
    #Create all the data structure after the file is load
    def createModel(self,file):
        df=self.parser.loadFile(file,self.itv)
        

        self.itv.calcDefectInspector("INS","DEFEC.","GRADO")
        self.cTree=TreeViewController()
        self.cRules=RulesController()
        self.cTree.setModel(self.itv)
        self.cRules.setRules(df)
        self.itv.setPandas(df)
        
        
    #Obtain the ControllerTreeview instance
    def obtainControllerTree(self):
        return self.cTree

    #Obtain the ControllerRule instance
    def obtainControllerRule(self):
        return self.cRules
    #Obtain the number of vehicle per number of defects
    def obtainHisto(self,grup,contains):
        return self.itv.countNumDefectVehicle(grup,contains)
    #Obtain the list of grups
    def obtainHistoHeader(self,head):
       return self.itv.obtainHistoHeader(head)

    #Gets the header
    def getHeader(self):
       return self.itv.getHeader()
    #Gets the dictionary   
    def getDic(self):
       return self.itv.getDic()
    #Gets the length header
    def lenHeader(self):
       return self.itv.lenHeader()
    #Gets the length dictionary
    def lenDic(self):
       return self.itv.lenDic()

    def updateTableCount(self,num):
        self.mainWindow.updateTableCount(num,self.itv.lenDic())