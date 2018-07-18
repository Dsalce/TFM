


from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QMenu,QCheckBox,QWidgetAction,QDialogButtonBox,QScrollBar,QPushButton

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pandas as pd
from View.pandasModel import *
 
class RulesTableView(QWidget):

    def __init__(self,controller,header):
        super().__init__()
        self.title = 'Reglas de asociacion'
        self.left = 50
        self.top = 50
        self.width = 840
        self.height = 800
        self.head=header
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.rController=controller
        self.table = QTableView()
        self.label= QLabel();
        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(1, 120)
        self.rTextButton = QPushButton("R.Asociacion Coincidencia")
        self.rButton = QPushButton("R.Asociacion")
        self.cb = QComboBox()
        if(self.rController!=None):
         self.cb.addItems(self.rController.obtainListHeader(self.head))
         self.rButton.clicked.connect(self.populateTable)
         self.rTextButton.clicked.connect(self.populateTableButton)
        self.mainLayout = QGridLayout()
        self.mainLayout.setSpacing(10)
        
        

        self.textbox = QLineEdit(self)
        self.textbox.resize(280,40)

        self.mainLayout.addWidget(self.cb,1,0)
        self.mainLayout.addWidget(self.rButton,1,1)
        self.mainLayout.addWidget(self.textbox,2,0)
        self.mainLayout.addWidget(self.rTextButton,2,1)
        
        self.mainLayout.addWidget(self.table,3,0)
        self.mainLayout.addWidget(self.label,3,1)
        self.setLayout(self.mainLayout)
       
        self.table.setAlternatingRowColors(True)
       
        self.show()


     
    def populateTable(self):
        self.label.setText(str(self.rController.obtainTotal(self.cb.currentText().strip(),self.head)))
        df=self.rController.getDataSet( self.cb.currentText().strip(),self.head)
        
        self.pandas= PandasModel(df,None)
        
        self.table.setModel(self.pandas)
        self.table.update()

    def populateTableButton(self):

        self.label.setText("Total Nº elementos: "+str(self.rController.obtainTotalContains(self.textbox.text().upper().strip(),self.head)))
        df=self.rController.getDataSetContains( self.textbox.text().upper().strip(),self.head)
        self.pandas= PandasModel(df,None)
        
        self.table.setModel(self.pandas)
        self.table.update()





