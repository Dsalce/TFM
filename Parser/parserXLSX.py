# -*- coding: utf-8 -*

"""
Class to import .xlsx
"""

import openpyxl
import pandas as pd



from Parser.parser import *

class ParserXLSX(Parser):
    
    #Constructor
    def __init__(self):
       Parser.__init__(self)
    
    
    #Load .xlsx file
    def loadFile(self,file,itv):
         df = pd.read_excel(file)
         df = df.fillna(value="")#remove empty values
         df= df.astype('str')#Change all the dataset to string
         df.columns =df.columns.str.strip()
         self.dic=df.to_dict('list')#transform columns into to list
         itv.setDic(self.dic)
         itv.setHeader(list(self.dic.keys()))
         return df

         
         """book = openpyxl.load_workbook(file)
         sheet = book.active

         rows = sheet.rows
         l=[]
         first=True
         k=0
         for row in rows:
          for cell in row:
            if(first==True):
              self.dic[cell.value]=[]
              l.append(cell.value)
              
            else:
             if(cell.value==None):
                 self.dic[l[k]].append("")
             else:
              self.dic[l[k]].append(str(cell.value))
             k=k+1
         
          k=0
          first=False

        
     
         itv.setDic(self.dic)
         

         
         itv.setHeader(l)"""
         


   
    





























