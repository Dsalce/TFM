
"""
Class Model of Inspector
"""

import statistics as stats


class Inspector(object):

  
  #Constructor
  def __init__(self,id):
       
       self.totalDefect=0
       self.propor={}
       self.defects={}
       self.id=id


  #Add a new defect to the dictionary
  def addDefect(self,defect):
    value=self.defects.get(defect)
    
    if( value!=None):
         self.defects[defect]=value+1
    else:
         self.defects[defect]=1 

    self.totalDefect=self.totalDefect+1

  #Calculate the proportion of one type of defect in the total
  def  calcNumProp(self):
        for defe in list(self.defects.keys()):
        	 self.propor[defe]=self.defects[defe]/self.totalDefect

 #Print all the information of the inspector class
  def toString(self):

    print(str(self.defects))
    print(str(self.propor))
    print(self.totalDefect)

  #Obtain the total of defect
  def obtainTotalDefect(self):

     return self.totalDefect
  #Calculate the mean of the defect
  def calcMean(self):
      return stats.mean(self.defects.values())

  #Obtain the number of the defect and the proportion of the  
  # defect passed like a parameter 
  def obtainValues(self,defect):
      return (self.defects[defect],self.propor[defect])
      
  #Obtain all the list of defects
  def obtainDefects(self):
      return self.defects.keys()

