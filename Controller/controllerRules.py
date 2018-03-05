

from Rules.asociationRules import *

class RulesController(object):
    
    
      def __init__(self):
          self.rules=Rules()
          
      
        

      def getDataSet(self):

          return self.rules.defectosDataSet()
      
      def setRules(self,rule):
          self.rules.setPandas(rule)