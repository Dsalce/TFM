


from View.mainwindow import *
from Model.parserTXT import *
from Model.parserCSV import *
from Model.parser import *
#from Model.parserXLSX import *
from Model.itv import *
import string

class MainController(object):
   
    def __init__(self):

        self.file=""
        app = QApplication(sys.argv)
        self.itv=itv()
        self.parser=Parser()
        mainWindow = MainWindow(self)
        sys.exit(app.exec_())
        

    def loadFileTxt(self,file):
        
        try:
         if("TXT"in file.upper()):
          self.file=file
          self.parser=ParserTXT()
          self.parser.loadFile(file,self.itv)
          self.itv.calcDefectInspector("INS","DEFEC.")
          self.itv.calcDefectGrup("GRUP","DEFEC.")
         elif("CSV" in file.upper()):
          self.file=file
          self.parser=ParserCSV()
          self.parser.loadFile(file,self.itv)

         
         elif("XLSX" in file.upper()):
          self.file=file
          #self.parser=ParserXLSX()
          #self.parser.loadFile(file,self.itv)
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





    def getHeader(self):
       return self.itv.getHeader()
    def getDic(self):
       return self.itv.getDic()
    def lenHeader(self):
       return self.itv.lenHeader()
    def lenDic(self):
       return self.itv.lenDic()
