


import statistics as stats


class Inspector(object):



  def __init__(self,id):
       
       self.totalDefect=0
       self.propor={}
       self.defects={}
       self.id=id



  def addDefect(self,defect):
    value=self.defects.get(defect)
    
    if( value!=None):
         self.defects[defect]=value+1
    else:
         self.defects[defect]=1 

    self.totalDefect=self.totalDefect+1


  def  calcNumProp(self):
        for defe in list(self.defects.keys()):
        	 self.propor[defe]=self.defects[defe]/self.totalDefect


  def toString(self):

    print(str(self.defects))
    print(str(self.propor))
    print(self.totalDefect)

  def obtainTotalDefect(self):

     return self.totalDefect
 
  def calcMean(self):
      return stats.mean(self.defects.values())
  
  def obtainValues(self,defect):
      return (self.defects[defect],self.propor[defect])
  
  def obtainDefects(self):
      return self.defects.keys()

