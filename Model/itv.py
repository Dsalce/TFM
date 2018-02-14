# -*- coding: utf-8 -*


import csv
import sys
import string
import numbers
import time
import statistics as stats

from Model.inspector import *


class itv(object):
   
       
    
    def __init__(self):
      self.dic={}
      self.headers=[]
      self.inspector={}



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

    def calcDefectInspector(self,header,header1):
       i=0
       defect=self.dic[header1]
       for ins in self.dic[header]:
            if( ins not in list(self.dic.keys())):
              self.inspector[ins]=Inspector(ins)
              

        
            self.inspector[ins].addDefect(defect[i])
            i=i+1

       for ins in list(self.inspector.keys()):

           self.inspector[ins].calcNumProp()

       for ins in list(self.inspector.keys()):

           print(ins)

           self.inspector[ins].toString()





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













