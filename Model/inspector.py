




import csv
import sys
import string
class Inspector(object):



  def __init__(self,id):

       self.totalDefect=0
       self.propor={}
       self.defects={}
       self.id=id



  def addDefect(self,defect):
    if(defect!=""):
     if( defect not in list(self.defects.keys())):
         self.defects[defect]=1
     else:
        self.defects[defect]=self.defects[defect]+1

     self.totalDefect=self.totalDefect+1


  def  calcNumProp(self):
        

        for defe in list(self.defects.keys()):
        	self.propor[defe]=self.defects[defe]/self.totalDefect


  def toString(self):

    print(self.defects)
    print(self.propor)




