# -*- coding: utf-8 -*
"""
Class to import .csv
"""

import csv



from Parser.parser import *




class ParserCSV(Parser):
    #Constructor
    def __init__(self):
       Parser.__init__(self)
    
    
    
    #Load .csv file
    def loadFile(self,file,itv):
      df = pd.read_csv(file)
      df = df.fillna(value="")#remove empty values
      self.dic=df.to_dict('list')#transform columns into to list
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
         


   
    





























