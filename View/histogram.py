# -*- coding: utf-8 -*-import numpy as np



from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
 
 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt



class Histogram(QWidget):
    
    
    
    def __init__(self, contro):
        super().__init__()
        self.controller=contro
        self.title = 'Histograma Defectos Vehiculo'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        
        data =self.controller.obtainHisto("1000")
        
        print(list(data.values()))
        print(list(data.keys()))
        
        
        x = list(data.values())
        y=list(data.keys())
        
    
        n, bins, patches = plt.hist(x[0:10],color="green")
         
        plt.xlabel('Numero de defectos')
        plt.ylabel('Numero de vehiculos')
        
        plt.xticks(range(0,10))
        plt.yticks(range(0,15))
      
        plt.show()


   
 
        
        
   
     
        
class PlotCanvas(FigureCanvas):
 
    def __init__(self,parent=None,width=5, height=4, dpi=100,controller=None):
        self.controller=controller
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
 
 
    def plot(self):
        data =self.controller.obtainHisto()
        ax = self.figure.add_subplot(111)
        ax.plot(list(data.values()), 'r-')
        
        self.draw()
        
        
        """print(list(data.values()))
        print(list(data.keys()))
        plt.hist(list(data.values()),bins='auto')"""
       # plt.show()
 
 

       