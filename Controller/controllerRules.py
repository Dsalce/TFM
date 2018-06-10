"""
Controller of the view related with the association rules


"""

from Rules.asociationRules import *

class RulesController(object):
    
      #Constructor
      def __init__(self):
          self.rules=Rules()
          
      
        
      #Gets the rules filtered by the header and the parameter
      def getDataSet(self,param,header):
        
          return self.rules.defectsDataSet(param,header)

      #Gets the rules filtered by the header and the contains parameter
      def getDataSetContains(self,param,header):
        
          return self.rules.defectsContainsDataSet(param,header)

      #Set the dataset
      def setRules(self,rule):
          
          self.rules.setPandas(rule)
      #Obtain the list of GRUP
      def obtainListHeader(self,header):
      	return self.rules.obtainListHeader(header)


      def obtainTotal(self,param,head):
          return self.rules.lenDataset(param,head)

      def obtainTotalContains(self,param,head):
          return self.rules.lenContainsDataset(param,head)


      #Gets the rules filtered by the header and the parameter
      def getTStudent(self,param,header):
        
          return self.rules.tStudentDataSet(param,header)

      #Gets the rules filtered by the header and the contains parameter
      def getTStudentContains(self,param,header):
        
          return self.rules.tStudentDataSetContains(param,header)

