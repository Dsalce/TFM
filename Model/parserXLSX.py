# -*- coding: utf-8 -*


import openpyxl
import string


from Model.parser import *

class ParserXLSX(Parser):
    

    def __init__(self):
       Parser.__init__(self)
    
    

    def loadFile(self,file,itv):
         
      
         book = openpyxl.load_workbook(file)
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
             
              self.dic[l[k]].append(cell.value)
              k=k+1
         
          k=0
          first=False

        
     
         itv.setDic(self.dic)
         

         
         itv.setHeader(l)


   
    





























