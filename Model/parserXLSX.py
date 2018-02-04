# -*- coding: utf-8 -*


import openpyxl
import string




class ParserXLSX(object):
    dic={}

    headers=[]

    def __init__(self):
      self.dic={}
      self.headers=[]
    
    

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
              self.dic[cell]=[]
              l.append(cell)
              
            else:
              self.dic[l[k]].append(v)
              k=k+1
         
          k=0
          first=False

        
     
         itv.setDic(self.dic)
         print(l)
         itv.setHeader(l)


   
    





























