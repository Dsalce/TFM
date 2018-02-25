


from View.mainwindow import *
from Model.parserTXT import *
from Model.parserCSV import *
from Model.parser import *
#from Model.parserXLSX import *
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
          self.parser.loadFile(file,self.itv)
          self.itv.calcDefectInspector("INS","DEFEC.")
          self.itv.calcDefectGrup("GRUP","DEFEC.")
          
          self.cTree.setModel(self.itv)
          self.itv.countNumDefectVehicle()
         elif("CSV" in file.upper()):
          self.file=file
          self.parser=ParserCSV()
          self.parser.loadFile(file,self.itv)
          self.itv.calcDefectInspector("INS","DEFEC.")
          self.itv.calcDefectGrup("GRUP","DEFEC.")
          self.cTree.setModel(self.itv)
          self.itv.countNumDefectVehicle()
         elif("XLSX" in file.upper()):
          self.file=file
          #self.parser=ParserXLSX()
          #self.parser.loadFile(file,self.itv)
          self.cTree.setModel(self.itv)
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
