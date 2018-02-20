from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
 
# ---------------------------------------------------------------------
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
 
        self.resize(520,300)
        self.setWindowTitle("Treeview Example")
 
        self.treeview = QTreeView(self)

 
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(0, Qt.Horizontal, "Inspector")
        model.setHeaderData(1, Qt.Horizontal, "Subject")
        model.setHeaderData(2, Qt.Horizontal, "Num. Defectos")
        model.setHeaderData(3, Qt.Horizontal, "Proporción")
        rootNode = model.invisibleRootItem()
        for ins in range(10):


          branch = QStandardItem("Branch 1")
          for d  in range(10):
              branch.appendRow([QStandardItem(""),QStandardItem("Child A"), None,None]) 
          
          rootNode.appendRow([ branch,None, None,None ])
        
         
        self.treeview.setModel(model)
        self.treeview.setColumnWidth(0, 150)
 
        self.setCentralWidget(self.treeview)
 
        self.treeview.setAlternatingRowColors(True)
         
# ---------------------------------------------------------------------
 
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())