# -*- coding: utf-8 -*

"""
Principal model that interact with the MainController class


"""

import statistics as stats

from Model.inspector import *
from Model.vehicle import *

import collections
import pandas as pd



class itv(object):
    
       
    #Constructor
    def __init__(self):
      self.dic={}
      self.headers=[]
      self.inspector={}
      self.histo={}
      self.rule=None

    #Mean per year
    def meanYear(self,hMAtric,hDefec,atrib):
      l=[]
      lVal=[]
      i=0

      for año in  self.dic[hMAtric]:
          
          if(año[-4:]==atrib):
            l.append(i)
          i=i+1
      i=0
      for lDefect in self.dic[hDefec]:
          print(lDefect)
          if(i in l):
            lVal.append(len(lDefect))

          i=i+1
      
      return stats.mean(lVal)

    #Calculate and populate the defect of the class  inspector
    def calcDefectInspector(self,headerIns,headerDefect,headerGrade):
       i=0
       self.lMean=[]
       defect=self.dic[headerDefect]
       grado=self.dic[headerGrade]
       #Populate inspector class
       for ins in self.dic[headerIns]:

            if( ins not in list(self.inspector.keys())):
             
              self.inspector[ins]=Inspector(ins)
              

            
            self.inspector[ins].addDefect(str(defect[i])+"-"+str(grado[i]))
            
            i=i+1
       #Calculate mean and proportion
       for ins in list(self.inspector.keys()):

           self.inspector[ins].calcNumProp()
           self.lMean.append(self.inspector[ins].obtainTotalDefect())

       
    #Return mean of the inspector passed by parameter
    def meanInspector(self,ins):
      
      return  self.inspector[ins].calcMean()


    #Calculate and populate the defect of the class  vehicle
    def calcDefect(self,headerInspection,headerGrup,headerDefect,headerGrade):
       i=0
       defect=self.dic[headerDefect]
       grado=self.dic[headerGrade]
       inspec=self.dic[headerInspection]
       for car in self.dic[headerGrup]:

            if( car not in list(self.histo.keys()) ):
             
              self.histo[car]=Vehicle(car)

            

            
            self.histo[car].addDefect(str(defect[i])+"-"+str(grado[i]))
            self.histo[car].addInspection(str(inspec[i]),str(defect[i]))
            i=i+1

    



       
    #Return an ordered dictionary by number of defect per number of vehicles
    def countNumDefectVehicle(self,typeHeader,contains):
        data=[]
        auxDic={}
        if(contains):
              aux=[s for s in list(self.histo.keys()) if typeHeader in s]
              for key in aux:
                data.append(self.histo[key].obtainNumInspection())
              
              for d in data:
                 for k,v in d.items():
                   if( k not in list(auxDic.keys())):
                      auxDic[k]=v
                   else:  
                      auxDic[k]=v+auxDic[k]
 
              return collections.OrderedDict(sorted(auxDic.items())) 
        else:
              return collections.OrderedDict(sorted(self.histo[typeHeader].obtainNumInspection().items()))
        
        
         
    #Obtain the list of GRUP    
    def obtainHistoHeader(self,head):

      if(len(self.dic)==0):
       return None
      else:
       self.calcDefect("INSPECCION",head,"DEFEC.","GRADO") 
       return sorted(list(set(self.dic[head])))

  


    #Obtain the dictionary of inspectors
    def obtainInspectors(self):
       return self.inspector

    
    #set dictionary
    def setDic(self,dic):
      self.dic=dic
    #Set  the headers
    def setHeader(self,header):
      self.headers=header

    #Get the headers
    def getHeader(self):
       return self.headers
    #get dictionary
    def getDic(self):
       return self.dic
    #get length dictionary
    def lenDic(self):
       return len(self.dic[self.headers[0]])
    #get length header
    def lenHeader(self):
       return len(self.headers)
    #set dataset
    def setPandas(self,pd):
        self.df=pd












