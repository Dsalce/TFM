# -*- coding: utf-8 -*


import csv
import sys
import string
import numbers
import time


class ParserTXT(object):
    dic={}
    headers=[]

    
    def obtainHeaders (self,lines,indice):
      i=0
      dic_num={}

      line=lines[indice-1]
      ini=0
      fin=0
      num_dash=lines[indice].split()
      while( i < len(num_dash)):
        fin=ini+num_dash[i].count('-')
        value=line[ini:fin].strip()
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
        if(len(line.strip())>20 ):


              while (i < len(self.headers)) :

               fin=ini+dic_num[self.headers[i]]
               value=line[ini:fin].strip()
               if(self.headers[i]=="DEFEC."):
                   listDefec.append([value])


                   self.dic[self.headers[i]]=listDefec
               else:
                   self.dic[self.headers[i]].append(value)
               ini=fin+1
               i=i+1

        else:


               k=len(self.dic["DEFEC."])-1

               listDefec=self.dic["DEFEC."]
               listDefec[k].append(line.strip())
               self.dic["DEFEC."]=listDefec

    def loadFile(self,file,itv):

     with open(file) as file:
      fileName=file.name



      lines=file.read().splitlines()




      ini=0
      j=0
      listDefec=[]
      header_ok=False
      firstTime=True
      while ( j  < len(lines)) :
         

         line=lines[j]

         if( len(line)>0):
           if("FECHA EMISION" in line):
                  header_ok=False
           elif("---" in line and firstTime==False ):

             header_ok=True
           elif("---" in line and firstTime==True ):

             dic_num= self.obtainHeaders(lines,j)
             header_ok=True
             firstTime=False

           elif( header_ok == True):
              self.readFile(line,dic_num,listDefec)
            


         j=j+1
      itv.setDic(self.dic)
      itv.setHeader(self.headers)
       




     file.close()

    

    def exportCSV(self,file):
        f=file.split(".")
        aux=f[0]+ ".csv"
        
        with open( aux, 'w') as csvfile:
           writer=csv.DictWriter(csvfile,self.headers)
           dicAux={}
           i=0
           writer.writeheader()

           while(i < len(self.dic[self.headers[0]])):
            for h in self.headers:
             dicAux[h]=self.dic[h][i];

            writer.writerow(aux)
            dicAux={}
            i=i+1



    def __init__(self):
      self.dic={}
      self.headers=[]
         
   


    
       
    




























