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
 
        
        data =self.controller.obtainHisto()
        
        print(list(data.values()))
        print(list(data.keys()))
        mu, sigma = 100, 15
        
        x = np.asarray(list(data.values()))
        y=np.asarray(list(data.keys()))
        
        
        n, bins, patches = plt.hist(np.asarray(list(data.values())), np.asarray(list(data.keys())),  facecolor='green')
          # y = mlab.normpdf( bins, mu, sigma)
          #l = plt.plot(bins, y, 'r--', linewidth=1)
        plt.bar(x, height= x)
        plt.xticks(x+.5, y);

        plt.xlabel('Numero de defectos')
        plt.ylabel('Numero de vehiculos')
        plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
        #plt.axis([0, 10000, 0, 30])
        plt.grid(True)
        plt.show()


        #m = PlotCanvas(None, 5, 4, 100,contro)
        #self.show()
 
        
        
   
     
        
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
 
 

       