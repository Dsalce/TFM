"""
Controller of the view related with the association rules


"""

from Rules.asociationRules import *

class RulesController(object):
    
      #Constructor
      def __init__(self):
          self.rules=Rules()
          
      
        
      #Gets the dataset filtered by GRUP
      def getDataSet(self,grupDefect,header):
         if(header=="GRUP") :
          return self.rules.defectosGRUPDataSet(grupDefect)
         elif(header=="MARCA Y MODELO"):
          return self.rules.defectosModelDataSet(grupDefect)

      #Set the dataset
      def setRules(self,rule):
          
          self.rules.setPandas(rule)
      #Obtain the list of GRUP
      def obtainListHeader(self,header):
      	return self.rules.obtainListHeader(header)