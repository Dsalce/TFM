# -*- coding: utf-8 -*


import csv
import sys
import string
import numbers
import time


from Model.parser import *
class ParserCSV(Parser):
    
    def __init__(self):
       Parser.__init__(self)
    
    
    

    def loadFile(self,file,itv):
     

      i=0
      first=True
      
     
      with open(file, newline='') as csvfile:
         reader = csv.DictReader(csvfile)
       
         for row in reader:
           for k,v in row.items():
            if(first==True):
              self.dic[k]=[]
              self.dic[k].append(v)
              
            else:
              self.dic[k].append(v)
           first=False

        
     
         itv.setDic(self.dic)

         itv.setHeader(list(self.dic.keys()))


   
    





























