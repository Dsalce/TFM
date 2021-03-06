
"""View class test statistic    """

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QMenu,QCheckBox,QWidgetAction,QDialogButtonBox,QScrollBar,QPushButton,QSizePolicy

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
import pandas as pd
from View.pandasModel import *
 
class TStudentView(QWidget):


    #Constructor
    def __init__(self,controller,header):
        super().__init__()
        self.title = 'Test estadisticos'
        self.left = 50
        self.top = 50
        self.width = 1200
        self.height = 800
        self.head=header
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.rController=controller
        self.table = QTableView()
        self.label= QLabel()
        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(1, 200)
        self.rTextButton = QPushButton("Test coincidencia")
        self.rButton = QPushButton("Test combobox")
        self.cb = QComboBox()
        #Populate combobox
        if(self.rController!=None):
         self.cb.addItems(self.rController.obtainListHeader(self.head))
         self.rButton.clicked.connect(self.populateTable)
         self.rTextButton.clicked.connect(self.populateTableButton)
        self.mainLayout = QGridLayout()
        self.mainLayout.setSpacing(10)
        
        

        self.textbox = QLineEdit(self)
       

        self.textPvalue= QLineEdit(self)
       
        self.textPvalue.setText("0.001")
        self.textPvalue.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed));
        self.textPvalue.setMinimumWidth(50);
        

        self.mainLayout.addWidget(self.cb,1,0)
        self.mainLayout.addWidget(self.rButton,1,1)
        self.mainLayout.addWidget(self.textbox,2,0)
        self.mainLayout.addWidget(self.rTextButton,2,1)
        self.mainLayout.addWidget(self.textPvalue,3,1)

        self.mainLayout.addWidget(self.table,4,0)
        
        self.mainLayout.addWidget(self.label,4,1)
        self.setLayout(self.mainLayout)
       
        self.table.setAlternatingRowColors(True)
       
        self.show()


    #Populate the table of test associated with the combobox
    def populateTable(self):
        self.label.setText("Total Nº elementos: "+str(self.rController.obtainTotal(self.cb.currentText().upper().strip(),self.head)))
        df=self.rController.getTStudent( self.cb.currentText().strip(),self.head,self.textPvalue.text())
        
        self.pandas= PandasModel(df,self.textPvalue.text())
        self.table.setModel(self.pandas)
     
        self.table.update()

    #Populate the table of test associated with the textfield
    def populateTableButton(self):

        self.label.setText("Total Nº elementos: "+str(self.rController.obtainTotalContains(self.textbox.text().upper().strip(),self.head)))
        df=self.rController.getTStudentContains( self.textbox.text().upper().strip(),self.head,self.textPvalue.text())
        self.pandas= PandasModel(df,self.textPvalue.text())
        
        self.table.setModel(self.pandas)

        self.table.update()



