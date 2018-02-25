


from Model.itv import *


class TreeViewController(object):
    
    
      def __init__(self):
          pass
          
          
      def obtainInspectors(self):
          return self.itv.obtainInspectors() 
      
      def obtainMean(self,ins):
          return self.itv.meanInspector(ins)
      
      def setModel(self,itv):
          self.itv=itv