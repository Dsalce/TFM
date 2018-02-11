
import csv
import sys
import string
class Parser(object):

 def __init__(self):
  self.dic={}
  self.headers=[]



 def loadFile(self,file,itv):
   pass


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

             writer.writerow(dicAux)
             
            
             i=i+1
           
