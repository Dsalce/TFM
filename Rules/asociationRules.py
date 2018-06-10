"""
Association rules 

"""

import statistics as stats
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

 
  def tStudentDataSet(self,param,head):
     rules=self.defectsDataSet(param,head)
     return rules

  def tStudentDataSetContains(self,param,head):
    rules=self.defectsContainsDataSet(param,head)
     
     
    lComb=self.combinatoriaInspector()
     
     

    tstudent=pd.DataFrame()
    tstudent["Inspectores"]=[]
    tstudent["Regla"]=[]
    tstudent["XT-Student"]=[]
    tstudent["YT-Student"]=[]
     
    for ins in lComb:
      i=0
      print(ins[0])
      insList0 = (self.df[(self.df["INS"]==ins[0]) ].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))
      insList1 = (self.df[(self.df["INS"]==ins[1]) ].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))
      insList0 = insList0.applymap(self.encode_units)
      insList1 = insList1.applymap(self.encode_units)
      tstudent["Inspectores"].append(str(ins[0])+";"+str(ins[1]))
      for X in rules["antecedants"]:
          
          tstudentX=stats.ttest_ind(stats.mean(insList0[X]),stats.mean(insList1[X]))

          Y=(list(rules["consequent"][i])[0])
          
        
          tstudentY=stats.ttest_ind(stats.mean(self.calculoTStudentY(insList0,Y,X),stats.mean(self.calculoTStudentY(insList1,Y,X))))

          tstudent["Regla"].append(str(X)+"->"+str(Y))
          tstudent["XT-Student"].append(tstudentX)
          tstudent["YT-Student"].append(tstudentY)

        

    return tstudent

  def combinatoriaInspector(self): 

     i=1
     l=list(pd.unique(self.df["INS"]))
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