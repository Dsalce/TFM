
"""View class of the tree of defects"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class TreeView(QWidget):

    #Constructor
    def __init__(self,cTree):
        super().__init__()
        self.cTree=cTree
        self.title = 'TreeView Defects'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
 
        
        self.initUI()
        
    #Create the tree of defects
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        self.treeview = QTreeView()
        
 
        model = QStandardItemModel(0, 4,None)
        model.setHeaderData(0, Qt.Horizontal, "Inspector | Media")
        model.setHeaderData(1, Qt.Horizontal, "Defecto")
        model.setHeaderData(2, Qt.Horizontal, "Num. Defecto")
        model.setHeaderData(3, Qt.Horizontal, "Proporción")
        rootNode = model.invisibleRootItem()
        if(self.cTree!=None):
         inspectors=self.cTree.obtainInspectors()
         for ins in inspectors.keys():


          branch = QStandardItem(str(ins)+ " | "+str(self.cTree.obtainMean(ins) ))
          for k  in inspectors[ins].obtainDefects():
              auxDefect=inspectors[ins].obtainValues(k)
              
              branch.appendRow([QStandardItem(""),QStandardItem(k), QStandardItem(str(auxDefect[0])),QStandardItem(str(auxDefect[1]))]) 
          
          rootNode.appendRow([ branch,None, None,None ])
        
          
        self.treeview.setModel(model)
        self.treeview.setColumnWidth(0, 150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.treeview)
        self.setLayout(mainLayout)
       
        self.treeview.setAlternatingRowColors(True)
        
        self.show()

 
