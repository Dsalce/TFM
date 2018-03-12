




import csv
import sys
import string
class Vehicle(object):



  def __init__(self,id):
       
       self.totalDefect=0
       self.defects={}
       self.propor={}
       self.id=id
       self.inspeccion={}

  def addInspection(self,inspec,defect):
   value=self.inspeccion.get(inspec)
   if(defect==""):
     self.inspeccion[inspec]=0
   else: 
     if( value!=None  ):
         self.inspeccion[inspec]=value+1
     else:
         self.inspeccion[inspec]=1 


      
  def obtainNumInspection(self):
     data={}
     for v in self.inspeccion.values():
        if( v not in list(data.keys())):
                data[v]=str(0)
     
        data[v]=str(int(data[v])+1)
     return data




  def addDefect(self,defect):
   value=self.defects.get(defect)
   if(defect!=""):
     if( value!=None  ):
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

