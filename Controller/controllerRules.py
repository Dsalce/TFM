

from Rules.asociationRules import *

class RulesController(object):
    
    
      def __init__(self):
          self.rules=Rules()
          
      
        

      def getGRUPDataSet(self,grupDefect):
          
          return self.rules.defectosGRUPDataSet(grupDefect)
      
      def setRules(self,rule):
          
          self.rules.setPandas(rule)