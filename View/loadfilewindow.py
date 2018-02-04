import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
 
class LoadFileWindow(QWidget):
    mainController=None
    def __init__(self,controller):
        super().__init__()
        self.mainController=controller
        self.title = 'LoadFileWindow'
        self.left = 10
        self.top = 10
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
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        self.mainController.loadFileTxt(fileName)
 
   
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoadFileWindow()
    sys.exit(app.exec_())