# -*- coding: utf-8 -*-import numpy as np



from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
 
 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt




class Histogram(QWidget):
    
    
    
    def __init__(self, contro,header):
        super().__init__()
        self.controller=contro
        self.title = 'Histograma'+header
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.head=header
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        
        self.cb = QComboBox()
        self.button = QPushButton("Calcula Histograma")
        self.rTextButton = QPushButton("Calcula Histograma Coincidencia")

        if(self.controller.obtainHistoHeader(self.head)!=None):
         self.cb.addItems([str(i) for i in self.controller.obtainHistoHeader(self.head)])
         self.button.clicked.connect(self.populateHisto)
         self.rTextButton.clicked.connect(self.populateContainsHisto)


        self.mainLayout = QGridLayout()
        self.mainLayout.setSpacing(10)
   
        
        self.mainLayout.addWidget(self.cb,1,0)
        self.mainLayout.addWidget(self.button,1,1)
        
        self.sc = MyStaticMplCanvas(self, width=5, height=4, dpi=100,data=None)
        self.mainLayout.addWidget(self.sc)
        self.setLayout(self.mainLayout)
       
        
        self.show()

   
    

    def populateHisto(self):
        data=self.controller.obtainHisto( self.cb.currentText().strip())
        
        self.sc.compute_initial_figure(data)
        
        self.mainLayout.update()ç

    def populateContainsHisto(self):
        data=self.controller.obtainHisto( self.cb.currentText().strip())
        
        self.sc.compute_initial_figure(data)
        
        self.mainLayout.update()

        
        
   
     
        
class MyMplCanvas(FigureCanvas):
 
    def __init__(self,parent=None,width=5, height=4, dpi=100,data=None):
        
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
       
        
        
        

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.compute_initial_figure(data)
        
    def compute_initial_figure(self):
        pass

class MyStaticMplCanvas(MyMplCanvas):
 
    def compute_initial_figure(self,data):
     if(data!=None):
        y = list(data.values())
        x=list(data.keys())
        print(x)
        print(y)
        self.axes.cla()
        self.axes.bar(x,y)
        self.axes.set_xlabel('Numero de defectos')
        self.axes.set_ylabel('Numero de vehiculos')
        
        self.draw()

        
        
       
 
 

       


"""self.controller.obtainGRUPS()
   data =self.controller.obtainHisto(grup)
   print(data)
   print(data.keys())
   print(data.values())
   y = list(data.values())
   x=list(data.keys())
   index=np.arange(len(x))
   print(index)
   print(x)
   print(y)
   plt.bar(x,y)
   plt.xlabel('Numero de defectos')
   plt.ylabel('Numero de vehiculos')
   plt.show()"""