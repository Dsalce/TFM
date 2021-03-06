# -*- coding: utf-8 -*

"""
Class to import .txt


"""


from Parser.parser import *


class ParserTXT(Parser):
    #Constructor
    def __init__(self):
      Parser.__init__(self)
    #Method to obtain the headers count the number of dash
    def obtainHeaders (self,line,lineAnt):
      i=0
      dic_num={}

      
      ini=0
      fin=0
      num_dash=line.split()#Split the line
     
      while( i < len(num_dash)):
        fin=ini+num_dash[i].count('-')#Count dash in segment
        
        value=lineAnt[ini:fin]
        dic_num[value]=num_dash[i].count('-')#save the number of dash
        
        self.dic[value]=[]
        self.headers.append(value)
        ini=fin+1
        i=i+1
       
      return dic_num


  
    #Parser a new line
    def readFile(self,line,dic_num,listDefec):

      
        i=0
        ini=0
        fin=0
        whites=0
        #count the number of variable empty
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
        #populate the dictionary and parser the line
        while (i < len(self.headers)) :
           fin=ini+dic_num[self.headers[i]]
           value=line[ini:fin].strip()
           
           
           if(whites>5):
             if(value==""):
              
             
              self.dic[self.headers[i]].append(self.dic[self.headers[i]][len(self.dic[self.headers[i]])-1])
             else:

              self.dic[self.headers[i]].append(value)

           else:
               self.dic[self.headers[i]].append(value)

           ini=fin+1
           i=i+1
   
    # Main method to parse the file
    def loadFile(self,file,itv):
     
     j=0    
     listDefec=[]
     header_ok=False
     firstTime=True
     lineAnt=""
     
     
      
     with open(file, 'rb') as file:
      for line in file:
         
        
         
         try:
          #encode the line to utf8
          line=str(line.decode('utf-8','replace'))
    
          
          if( len(line.strip())>0):
           #Control line
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
            
            
          
          lineAnt=line
          j=j+1
         
         except Exception:
             print("Linea out:"+line)
      self.changeDefect()
        

      self.removePersonalData()
      itv.setDic(self.dic)
      itv.setHeader(self.headers)
      file.close()
      df=pd.DataFrame.from_dict(self.dic)
      df = df.fillna(value="")
      df= df.astype('str')#Change all the dataset to string
      df.columns =df.columns.str.strip()
      
      return df
  



     
    #Change the columns of defects
    def changeDefect(self): 
    
      self.headers.append("GRADO")
      self.dic["GRADO"]=[]
  
      i=0
      for d in self.dic["DEFEC."]:
          
          if(d.strip()!=""):
             grado=d[len(d)-1]
             if(grado=="G"):
                grado="grave"
             elif(grado=="L"):
                grado="leve"

             self.dic["GRADO"].append(grado)
             l = list(d)
             try: 
              p = l.index("-")
              del(l[p+1])
              del(l[p])
              self.dic["DEFEC."][i]="".join(l)
             except Exception:
                pass 
          else:
               self.dic["GRADO"].append("")

          i=i+1

       

    #Remove the columns with personal data LOPD ... very important
    def removePersonalData(self):
        
        for header in self.headers:
          
          if( "NOMBRE"  in header.upper() or "APELLIDO"  in header.upper() or "MATRICULA"  in header.upper()  or "DOMICILIO"  in header.upper()
            or "MATRICULA"  in header.upper() or "BASTIDOR"  in header.upper()
            or "DNI"  in header.upper()):
               
               self.dic.pop(header, None)


        self.headers=list(self.dic.keys())
               



    



    
         
   


    
       
    




























