


from View.mainwindow import *
from Parser.parserTXT import *
from Parser.parserCSV import *
from Parser.parser import *
from Parser.parserXLSX import *
from Model.itv import *
from Controller.controllerTreeView import *


class MainController(object):
   
    def __init__(self):

        self.file=""
        app = QApplication(sys.argv)
        self.itv=itv()
        self.cTree=TreeViewController()
        self.parser=Parser()
        mainWindow = MainWindow(self,app)
        sys.exit(app.exec_())
        

    def loadFileTxt(self,file):
        self.itv=itv()
        try:
         if("TXT"in file.upper()):
         
          self.file=file
          self.parser=ParserTXT()
          self.createModel(file)
         
         elif("XLSX" in file.upper()):
          self.file=file
          self.parser=ParserXLSX()
          self.createModel(file)
          self.itv.countNumDefectVehicle()
         elif("CSV" in file.upper()):
          self.file=file
          self.parser=ParserCSV()
          self.createModel(file)
         elif(file==""):
             return 0
         else:
          return 1
        except OSError:
          return -1

    def exportFileCSV(self):
       try:
        if(self.file!=""):
         self.parser.exportCSV(self.file)
        else:
          return -1 
       except OSError:
        return -1
    
    def createModel(self,file):
        self.parser.loadFile(file,self.itv)
        self.itv.calcDefectInspector("INS","DEFEC.","GRADO")
        self.itv.calcDefectGrup("GRUP","DEFEC.","GRADO")
        self.cTree.setModel(self.itv)
        self.itv.countNumDefectVehicle()
    
    def obtainControllerTree(self):
        return self.cTree
    def obtainHisto(self):
        return self.itv.countNumDefectVehicle()

    def getHeader(self):
       return self.itv.getHeader()
    def getDic(self):
       return self.itv.getDic()
    def lenHeader(self):
       return self.itv.lenHeader()
    def lenDic(self):
       return self.itv.lenDic()
