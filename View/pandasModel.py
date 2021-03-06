
""" Pandas model class"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QMenu,QCheckBox,QWidgetAction,QDialogButtonBox,QScrollBar,QPushButton

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pandas as pd


class PandasModel(QAbstractTableModel):

    #Constructor  
    def __init__(self, data,pvalue, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data
        self.pvalue=pvalue
        self.paint=True
        self.insf="all"

    #Row size
    def rowCount(self, parent=None):
        return len(self._data.values)

    #Column size
    def columnCount(self, parent=None):
        return self._data.columns.size
    
    #This methold is use to color some of the table cells and rows when the inspector change
    def data(self, index, role=Qt.DisplayRole):

        if index.isValid():
            if role == Qt.DisplayRole:
               if( isinstance(self._data.values[index.row()][index.column()], float)) :
                   return str(self._data.values[index.row()][index.column()])
               elif (isinstance(self._data.values[index.row()][index.column()], str)):
                  return str(self._data.values[index.row()][index.column()])
               else:
                  return str(list(self._data.values[index.row()][index.column()]))
            if role==Qt.BackgroundColorRole and self.pvalue!=None:
              #Red cells
              if(index.column()!=0 and index.column()!=1   and (float(self.pvalue)>float(self._data.values[index.row()][index.column()])) ):	
             
                   return QVariant(QColor(Qt.red))
              elif(index.column()==0 ):
                 
                  ins=str(self._data.values[index.row()][index.column()]).split("(")
                  
                  if(self.insf!=ins[0]):
                      self.paint=not(self.paint)
                  self.insf=ins[0]

              if(self.paint==True):
                 return QVariant(QColor(0, 255, 255,127))

              
                      
              
        return None
    #Get the data    
    def getData(self):
       return self._data

    #Get the header of the table
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None