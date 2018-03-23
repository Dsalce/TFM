



from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QMenu,QCheckBox,QWidgetAction,QDialogButtonBox,QScrollBar,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot,Qt,QPoint
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


 
class TableView(QTableWidget):

    mainController=None
    def __init__(self,controller):
        super().__init__()
        self.mainController=controller
        
        self.horizontalHeader().sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)
        
 

    def createTable(self):
       # Create table
      
        headers=self.mainController.getHeader()
        dic=self.mainController.getDic()
        self.columns =headers
        
        self.setRowCount(self.mainController.lenDic())
        self.setColumnCount(self.mainController.lenHeader())
        k=0
        for h in headers:
          
            self.setHorizontalHeaderItem(k,  QTableWidgetItem(h));
            k=k +1


        i=0
        j=0
        while(i < self.mainController.lenDic()):
            for h in headers:
             
              self.setItem(i,j, QTableWidgetItem(str(dic[h][i])))
              j=j+1
            i=i+1
            j=0

        self.keywords = dict([(i, []) for i in range(self.columnCount())])


        
       
    
        
    def clearFilter(self):
        for i in range(self.rowCount()):
            self.setRowHidden(i, False)

        self.menu.close()

        


    def filterdata(self):

        columnsShow = dict([(i, True) for i in range(self.rowCount())])

        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                item = self.item(i, j)
                if self.keywords[j]:
                    if item.text() not in self.keywords[j]:
                        columnsShow[i] = False
        for key, value in columnsShow.items():
            self.setRowHidden(key, not value)

    def slotSelect(self, state):

        for checkbox in self.checkBoxs:
            checkbox.setCheckState(Qt.Checked == state)

    def menuClose(self):
        self.keywords[self.col] = []
        for element in self.checkBoxs:
            #if element.isChecked():
            if element.checkState() == Qt.Checked:
                self.keywords[self.col].append(element.text())
        self.filterdata()
        self.menu.close()


    def createCheckBoxes(self):
         #Create checkbox
        data_unique = []
        
        self.table=QTableWidget()

        self.table.setColumnCount(1)
        self.table.verticalHeader().hide()
        self.table.horizontalHeader().hide()
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setRowCount(self.rowCount())
       
       

        self.checkBoxs = []
        checkBox = QCheckBox("Select all", self.menu)
        
        checkableAction = QWidgetAction(self.menu)
        checkableAction.setDefaultWidget(checkBox)
        self.menu.addAction(checkableAction)
        checkBox.setChecked(True)
        checkBox.stateChanged.connect(self.slotSelect)
        j=0
        for i in range(self.rowCount()):
           # if not self.isRowHidden(i):
                item = self.item(i, self.col )
                if item.text() not in data_unique:
                    data_unique.append(item.text())
                    
                    it = QTableWidgetItem(item.text())
                    it.setFlags(Qt.ItemIsUserCheckable |Qt.ItemIsEnabled)
                    it.setCheckState(Qt.Checked)
                    #self.table.setItem(j,0, it)
                    self.checkBoxs.append(it)
                    j=j+1


  
        
        for i in range(len(self.checkBoxs)):
                print()
                self.table.setItem(j,0,  self.checkBoxs[i]
                



        self.table.setRowCount(len(self.checkBoxs))
        checkableAction = QWidgetAction(self.menu)
        checkableAction.setDefaultWidget(self.table)
        self.menu.addAction(checkableAction)

    def on_view_horizontalHeader_sectionClicked(self, index):
        
        self.menu = QMenu(self)
       
        self.col = index
        


       
        self.createCheckBoxes()

        
        #Accept and cancel button
        btn = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                                     Qt.Horizontal, self.menu)
        btn.accepted.connect(self.menuClose)
        btn.rejected.connect(self.menu.close)
        checkableAction = QWidgetAction(self.menu)
        checkableAction.setDefaultWidget(btn)
        self.menu.addAction(checkableAction)

        ##Clear Button
        btnClr = QPushButton(QIcon(),"Limpiar Filtro", self.menu)
        btnClr.clicked.connect(self.clearFilter)
        checkableAction = QWidgetAction(self.menu)
        checkableAction.setDefaultWidget(btnClr)
        self.menu.addAction(checkableAction)







        headerPos = self.mapToGlobal(self.horizontalHeader().pos())

        posY = headerPos.y() + self.horizontalHeader().height()
        posX = headerPos.x() + self.horizontalHeader().sectionPosition(index)
        self.menu.exec_(QPoint(posX, posY))
       
        
 
    def sort(self,l):
      i=0
      for i in range( len(l)):
        j = i-1 
        key = l[i]
        while (l[j].text() > key.text()) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
 

