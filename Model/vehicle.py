"""
Class Model of vehicle
"""




import csv
import sys
import string
class Vehicle(object):


  #Constructor
  def __init__(self,id):
       
       self.totalDefect=0
       self.defects={}
       self.id=id
       self.inspeccion={}


  #Add a new inspection
  def addInspection(self,inspec,defect):
   value=self.inspeccion.get(inspec)
   if(defect==""):
     self.inspeccion[inspec]=0
   else: 
     if( value!=None  ):
         self.inspeccion[inspec]=value+1
     else:
         self.inspeccion[inspec]=1 


  #Obtain the number of defect per inspection
  def obtainNumInspection(self):
     data={}
     for v in self.inspeccion.values():
        if( v not in list(data.keys())):
                data[v]=0
     
        data[v]=int(data[v])+1
     return data



  #Add a new defect to the dictionary
  def addDefect(self,defect):
   value=self.defects.get(defect)
   if(defect!=""):
     if( value!=None  ):
         self.defects[defect]=value+1
     else:
         self.defects[defect]=1 

     self.totalDefect=self.totalDefect+1

 
  #Obtain the total of  defect
  def obtainTotalDefect(self):

     return self.totalDefect

