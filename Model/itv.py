# -*- coding: utf-8 -*



import statistics as stats

from Model.inspector import *
from Model.vehicle import *

import collections



class itv(object):
    
       
    
    def __init__(self):
      self.dic={}
      self.headers=[]
      self.inspector={}
      self.vehicle={}
      self.rule=None


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

    def calcDefectInspector(self,headerIns,headerDefect,headerGrade):
       i=0
       self.lMean=[]
       #Array de defectos
       defect=self.dic[headerDefect]
       grado=self.dic[headerGrade]
       for ins in self.dic[headerIns]:

            if( ins not in list(self.inspector.keys())):
             
              self.inspector[ins]=Inspector(ins)
              

            
            self.inspector[ins].addDefect(str(defect[i])+"-"+str(grado[i]))
            
            i=i+1

       for ins in list(self.inspector.keys()):

           self.inspector[ins].calcNumProp()
           self.lMean.append(self.inspector[ins].obtainTotalDefect())

       

    def meanInspector(self,ins):
      
      return  self.inspector[ins].calcMean()


            
    def calcDefectGrup(self,headerGrup,headerDefect,headerGrade):
       i=0
      
       defect=self.dic[headerDefect]
       grado=self.dic[headerGrade]
       for car in self.dic[headerGrup]:

            if( car not in list(self.vehicle.keys())):
             
              self.vehicle[car]=Vehicle(car)
              

            
            self.vehicle[car].addDefect(str(defect[i])+"-"+str(grado[i]))
            
            i=i+1

       
    
    def countNumDefectVehicle(self):
        data={}
        aux={}
        for k,car in self.vehicle.items():
            
            if( car.obtainTotalDefect() not in list(data.keys())):
                           data[car.obtainTotalDefect()]=1
                           
            else:
                data[car.obtainTotalDefect()]=data[car.obtainTotalDefect()]+1

            if( car.obtainTotalDefect() not in list(aux.keys())):
                           aux[car.obtainTotalDefect()]=[]
                           aux[car.obtainTotalDefect()].append(k)
                           
            else:
                aux[car.obtainTotalDefect()].append(k)

    
        print(aux)
        print("\n")
        print(data)
        print("\n")
        od = collections.OrderedDict(sorted(data.items()))
        return od
        





    def obtainInspectors(self):
       return self.inspector

    

    def setDic(self,dic):
      self.dic=dic

    def setHeader(self,header):
      self.headers=header


    def getHeader(self):
       return self.headers

    def getDic(self):
       return self.dic

    def lenDic(self):
       return len(self.dic[self.headers[0]])

    def lenHeader(self):
       return len(self.headers)
    
    def setPandas(self,pd):
        self.rule=pd












