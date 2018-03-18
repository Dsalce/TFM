"""
Controller associated with the TreeView

"""


from Model.itv import *


class TreeViewController(object):
    
      #Constructor
      def __init__(self):
          pass
          
      #Obtain the information associated with the inspector
      def obtainInspectors(self):
          return self.itv.obtainInspectors() 
      #Obtain the Mean defects per Inspector  
      def obtainMean(self,ins):
          return self.itv.meanInspector(ins)
      #Set the itv model
      def setModel(self,itv):
          self.itv=itv