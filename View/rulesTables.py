


from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QMenu,QCheckBox,QWidgetAction,QDialogButtonBox,QScrollBar,QPushButton

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pandas as pd
 
class RulesTableView(QWidget):

    def __init__(self,controller,header):
        super().__init__()
        self.title = 'Reglas de asociacion'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.head=header
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.rController=controller
        self.table = QTableView()
        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(1, 120)
        self.rTextButton = QPushButton("R.Asociacion Coincidencia")
        self.rButton = QPushButton("R.Asociacion")
        self.cb = QComboBox()
        if(self.rController!=None):
         self.cb.addItems(self.rController.obtainListHeader(self.head))
         self.rButton.clicked.connect(self.populateTable)
         self.rTextButton.clicked.connect(self.populateTableButton)
        mainLayout = QGridLayout()
        mainLayout.setSpacing(10)
   
        

        self.textbox = QLineEdit(self)
        self.textbox.resize(280,40)

        mainLayout.addWidget(self.cb,1,0)
        mainLayout.addWidget(self.rButton,1,1)
        mainLayout.addWidget(self.textbox,2,0)
        mainLayout.addWidget(self.rTextButton,2,1)

        mainLayout.addWidget(self.table)
        self.setLayout(mainLayout)
       
        self.table.setAlternatingRowColors(True)
       
        self.show()


     
    def populateTable(self):

        df=self.rController.getDataSet( self.cb.currentText().strip(),self.head)
        
        self.pandas= PandasModel(df)
        
        self.table.setModel(self.pandas)
        self.table.update()

    def populateTableButton(self):

        
        df=self.rController.getDataSetContains( self.textbox.text().upper().strip(),self.head)
        self.pandas= PandasModel(df)
        
        self.table.setModel(self.pandas)
        self.table.update()





class PandasModel(QAbstractTableModel):
    
    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
               if( isinstance(self._data.values[index.row()][index.column()], float)) :
                   return str(self._data.values[index.row()][index.column()])
               else :
                  return str(list(self._data.values[index.row()][index.column()]))
        return None
    def getData(self):
       return self._data

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None