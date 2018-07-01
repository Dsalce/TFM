"""
Association rules 

"""

import statistics as stat
from scipy import stats
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import operator

class Rules(object):





 #Constructor
  def __init__(self):
       self.df=None
       
  #Function to encode the result of pandas selects
  def encode_units(self,x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
  #Obtain the list of the header
  def obtainListHeader(self,header):

     return sorted(list(pd.unique(self.df[header.strip()])))

  

 
  #Obtain association rule with contains
  def defectsContainsDataSet(self,param,head):
     
     basket_sets = (self.df[self.df[head].str.contains(param)].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))
     if(not basket_sets.empty):
    
      basket_sets = basket_sets.applymap(self.encode_units)
      frequent_itemsets = apriori(basket_sets,min_support=0.05, use_colnames=True)
      
      rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

      return self.addNumberRules(rules,self.lenConData)
     else:
       return pd.DataFrame()

  
  #Obtain association rule 
  def defectsDataSet(self,param,head):
     
    basket_sets = (self.df[self.df[head]==param].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))
    if(not basket_sets.empty):
     basket_sets = basket_sets.applymap(self.encode_units)
     
     frequent_itemsets = apriori(basket_sets,min_support=0.05, use_colnames=True)
     

     rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
     
     return self.addNumberRules(rules,self.lenData)
    else:
       return pd.DataFrame()




  def addNumberRules(self,rules,lenD):
     
     if len(rules)!=0 :
       l=[]
       auxlist=[]
       for  k in  range(len(rules["support"])):
           l.append(lenD)
       auxlist=list(map(operator.mul, list(map(operator.mul, rules["support"], rules["confidence"])),l))
       l=[]
      
       for  rule in   auxlist:
         
          l.append(round( rule,2))

       rules["Nº de elementos"]=l

       return rules
     else:
       return pd.DataFrame()

  
  def lenDataset(self,param,head):
     self.lenData=len(self.df[self.df[head]==param].groupby([ "INSPECCION"]).nunique())
     return self.lenData

  def lenContainsDataset(self,param,head):

     self.lenConData= len(self.df[self.df[head].str.contains(param)].groupby(["INSPECCION"]).nunique())
     return self.lenConData

  #Set pandas
  def setPandas(self,df):

        self.df=df

 
  def tStudentDataSet(self,param,head,textPValue):
     rules=self.defectsDataSet(param,head)
     if(not rules.empty ):
      return self.obtainTStudent(rules,textPValue,param,head,False)
     else:return rules


  def tStudentDataSetContains(self,param,head,textPValue):
    rules=self.defectsContainsDataSet(param,head)
    if( not rules.empty ):
     return self.obtainTStudent(rules,textPValue,param,head,True)
    else: return rules
    
    

 


  def obtainTStudent(self,rules,textPValue,param,head,contains):


    lComb=self.combinatoriaInspector()
    lIns0=[]
    lIns1=[]
    lRulesX=[]
    lRulesY=[]
    lXTStudent=[]
    lXKTest=[]
    lYTStudent=[]
    lYKTest=[]
    tstudent=pd.DataFrame()
    self.pvalue=textPValue
    
    
    for ins in lComb:
      i=0
      if(contains):
        insList1 = (self.df[(self.df["INS"]==ins[1]) & (self.df[head].str.contains(param))].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))
        
        if(ins[0]=="all"):
          insList0 = (self.df[(self.df["INS"]!=ins[1])&(self.df[head].str.contains(param))].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))
        else:
          insList0 = (self.df[(self.df["INS"]==ins[0])& (self.df[head].str.contains(param)) ].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))


      else:
         insList1 = (self.df[(self.df["INS"]==ins[1]) & (self.df[head]==param)].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))
         if(ins[0]=="all"):
           insList0 = (self.df[(self.df["INS"]!=ins[1])&(self.df[head]==param)].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))
         else:
          insList0= (self.df[(self.df["INS"]==ins[0]) & (self.df[head]==param) ].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))



      insList0 = insList0.applymap(self.encode_units)
      insList1 = insList1.applymap(self.encode_units)
      
      
      for X in rules["antecedants"]:
          
          X=(list(X)[0])
          Y=(list(rules["consequents"][i])[0])
          
          if(X in insList0 and X in insList1 and Y in insList0 and Y in insList1):
           tstudentX=stats.ttest_ind(insList0[X],insList1[X],equal_var = False)
           XkTest=stats.ks_2samp(insList0[X],insList1[X])

           auxL0=self.calculoTStudentY(insList0,Y,X)
           auxL1=self.calculoTStudentY(insList1,Y,X)
           tstudentY=stats.ttest_ind(auxL0,auxL1,equal_var = False)
           YkTest=stats.ks_2samp(auxL0,auxL1)

          
           if(tstudentX[1] <float(textPValue) or tstudentY[1] <float(textPValue)):
            rat0X=0
            rat0Y=0
            rat1X=0
            rat1Y=0

            if(list(insList0[X]).count(1)!=0): rat0X=round(len(insList0[X])/list(insList0[X]).count(1),2)
            if(auxL0.count(1)!=0): rat0Y=round(list(insList0[X]).count(1)/auxL0.count(1),2)
            if(list(insList1[X]).count(1)!=0): rat1X=round(len(insList1[X])/list(insList1[X]).count(1),2)
            if(auxL1.count(1)!=0): rat1Y=round(list(insList1[X]).count(1)/auxL1.count(1),2)

            lIns0.append(ins[0]+"("+str(len(insList0[X]))+"/"+str(list(insList0[X]).count(1))+"("+str(rat0X)+")"+"/"+str(auxL0.count(1))+"("+ str(rat0Y) +")"+")")

            
            lIns1.append(ins[1]+"("+str(len(insList1[X]))+"/"+str(list(insList1[X]).count(1))+"("+str(rat1X) +")"+"/"+str(auxL1.count(1))+"("+ str(rat1Y) +")"+")")

            lRulesX.append(X)
            lRulesY.append(Y)
            lXTStudent.append(tstudentX[1])
            lXKTest.append(XkTest[1])
            lYTStudent.append(tstudentY[1])
            lYKTest.append(YkTest[1])
           
          i+=1
    
        
    tstudent["Inspector1(NTotalCoches/X(RatioX)/Y(RatioY))"]=lIns0
    tstudent["Inspector2(NTotalCoches/X(RatioX)/Y(RatioY))"]=lIns1
    tstudent["ReglaX"]=lRulesX
    tstudent["ReglaY"]=lRulesY
    tstudent["XT-Student"]=lXTStudent
    tstudent["X-Kolmogorov-Smirnov"]=lXKTest
    tstudent["YT-Student"]=lYTStudent
    tstudent["Y-Kolmogorov-Smirnov"]=lYKTest
    return tstudent

  def combinatoriaInspector(self): 

     i=1
     l=[]
     l.append("all")

     l.extend(list(pd.unique(self.df["INS"])))
     
     lComb=[]
     for ins in l:
       for j in range(i,len(l)):
         lComb.append((ins,l[j]))
       i+=1 

     return lComb

  def calculoTStudentY(self,insList,Y,X):
     j=0
     
     auxList=[]
     for val in insList[X]:
        if( val==1 and  insList[Y][j]==1):
            auxList.append(1)
            
        elif(val==1 and  insList[Y][j]==0):
            auxList.append(0)
          
        j+=1
     return auxList