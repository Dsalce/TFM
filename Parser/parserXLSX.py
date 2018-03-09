# -*- coding: utf-8 -*


import openpyxl
import pandas as pd



from Parser.parser import *

class ParserXLSX(Parser):
    

    def __init__(self):
       Parser.__init__(self)
    
    

    def loadFile(self,file,itv):
         df = pd.read_excel(file)
         df = df.fillna(value="")
         self.dic=df.to_dict('list')
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
         


   
    





























