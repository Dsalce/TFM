# -*- coding: utf-8 -*-import numpy as np



from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
 
 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
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
 
        # m = PlotCanvas(None, 5, 4, 100,contro)
        data =self.controller.obtainHisto()
        
        print(list(data.values()))
        print(list(data.keys()))
        num_bins = 15
        n, bins, patches = plt.hist(list(data.values()), num_bins, facecolor='red', alpha=0.5)
        plt.show()
 
        self.show()
 
        
        
   
     
        
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
        print(list(data.values()))
        print(list(data.keys()))
        num_bins = 15
        n, bins, patches = plt.hist(list(data.values()), num_bins, facecolor='red', alpha=1)
        plt.show()
        self.draw()
        
        
        """print(list(data.values()))
        print(list(data.keys()))
        plt.hist(list(data.values()),bins='auto')"""
       # plt.show()
 
 

       