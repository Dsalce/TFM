# -*- coding: utf-8 -*


import csv
import sys
import string
import numbers
import time
import codecs
import os

from Model.parser import *


class ParserTXT(Parser):
    dic={}
    headers=[]

    
    def obtainHeaders (self,line,lineAnt):
      i=0
      dic_num={}

      
      ini=0
      fin=0
      num_dash=line.split()
     
      while( i < len(num_dash)):
        fin=ini+num_dash[i].count('-')
        
        value=lineAnt[ini:fin]
        dic_num[value]=num_dash[i].count('-')
        
        self.dic[value]=[]
        self.headers.append(value)
        ini=fin+1
        i=i+1
       
      return dic_num


  

    def readFile(self,line,dic_num,listDefec):

      
        i=0
        ini=0
        fin=0
        whites=0
        while (i < len(self.headers)) :
           fin=ini+dic_num[self.headers[i]]
           value=line[ini:fin].strip()
           
           if(value==""):
              whites=whites+1
           
           ini=fin+1
           i=i+1
        
        i=0
        ini=0
        fin=0
       
        while (i < len(self.headers)) :
           fin=ini+dic_num[self.headers[i]]
           value=line[ini:fin].strip()
           #print("Inicio:"+str(ini)+"  Fin:"+str(fin ))
           #print(value)

           if(whites>5):
             if(value==""):
              self.dic[self.headers[i]].append(self.dic[self.headers[i]][len(self.dic[self.headers[i]])-1])
             else:

              self.dic[self.headers[i]].append(value)

           else:
               self.dic[self.headers[i]].append(value)

           ini=fin+1
           i=i+1

    def loadFile(self,file,itv):
     
     j=0    
     listDefec=[]
     header_ok=False
     firstTime=True
     lineAnt=""
     lineH=""
     
      
     with open(file, 'rb') as file:
      for line in file:
         
        
         
         try:
          line=str(line.decode('utf-8','replace').encode("utf-8"),"utf-8")
    
          
          if( len(line.strip())>0):

           if("FECHA EMISION" in line.upper() or "ESTACION" in line.upper()):
                  header_ok=False
           elif("------" in line and firstTime==False ):

             header_ok=True
            
           elif("------" in line and firstTime==True ):

             dic_num= self.obtainHeaders(line,lineAnt)
             header_ok=True
             firstTime=False

           elif( header_ok == True):
              self.readFile(line,dic_num,listDefec)
              bl=0
            
          
          lineAnt=line
          j=j+1
         
         except Exception:
             print(line)
        

      self.removePersonalData()
      itv.setDic(self.dic)
      itv.setHeader(self.headers)
       




     file.close()

    def removePersonalData(self):
        
        for header in self.headers:
          
          if( "NOMBRE"  in header.upper() or "APELLIDO"  in header.upper() or "MATRICULA"  in header.upper()  or "DOMICILIO"  in header.upper()
            or "MATRICULA"  in header.upper() or "BASTIDOR"  in header.upper()
            or "DNI"  in header.upper()):
               
               self.dic.pop(header, None)


        self.headers=list(self.dic.keys())
               



    



    def __init__(self):
      Parser.__init__(self)
         
   


    
       
    




























