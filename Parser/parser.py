
"""

Parser father class 


"""

import csv
import pandas as pd


class Parser(object):
 #Constructor
 def __init__(self):
  self.dic={}
  self.headers=[]


 #Not implemented method
 def loadFile(self,file,itv):
   pass

 #Export the table in .csv 
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
               #encode the file in utf8 it is necessary to generate a good .csv file  
               dicAux[h]=str(self.dic[h][i].encode("utf-8")).replace("b'", "").replace("'", "")

             writer.writerow(dicAux)
             
            
             i=i+1
           
