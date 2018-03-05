# -*- coding: utf-8 -*


import csv

import pandas as pd

from Parser.parser import *

import pandas as pd


class ParserCSV(Parser):
    
    def __init__(self):
       Parser.__init__(self)
    
    
    

    def loadFile(self,file,itv):
      df = pd.read_csv(file)
      df = df.fillna(value="")
      self.dic=df.to_dict('list')
      itv.setDic(self.dic)
      itv.setHeader(list(self.dic.keys()))
      return df
      """i=0
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

         itv.setHeader(list(self.dic.keys()))"""
         


   
    





























