


from View.mainwindow import *
from Model.parserTXT import *
from Model.parserCSV import *
from Model.parserXLSX import *
from Model.itv import *
import string

class MainController(object):
   
    def __init__(self):


        app = QApplication(sys.argv)
        self.itv=itv()
        self.loadCSV= ParserCSV()
        self.loadTxt = ParserTXT()
        self.loadXLSX = ParserXLSX()
        mainWindow = MainWindow(self)
        sys.exit(app.exec_())
        

    def loadFileTxt(self,file):
        
        try:
         if("TXT"in file.upper()):
          self.loadTxt.loadFile(file,self.itv)
         elif("CSV" in file.upper()):
          self.loadCSV.loadFile(file,self.itv)
         elif("XLSX" in file.upper()):
          
          self.loadXLSX.loadFile(file,self.itv)
         else:
          return 1
        except OSError:
          return -1

    def ExportFileCsv(self,file):
       try:
        self.loadTxt.exportCSV("PITLRIDV[3392]")
       except OSError:
        print("Error en la carga del fichero")

    def getHeader(self):
       return self.itv.getHeader()
    def getDic(self):
       return self.itv.getDic()
    def lenHeader(self):
       return self.itv.lenHeader()
    def lenDic(self):
       return self.itv.lenDic()
