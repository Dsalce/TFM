import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog,QMessageBox , QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
 
class LoadFileWindow(QWidget):
    
    def __init__(self,controller):
        super().__init__()
        self.errFile=0
        self.mainController=controller
        self.title = 'LoadFileWindow'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.openFileNameDialog()
        
 
        self.show()
 
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Importar fichero ", "","All Files (*);;Python Files (*.py)", options=options)
        self.errFile=self.mainController.loadFileTxt(fileName)
       
 
   
 
    def getFileErr(self):
        return self.errFile