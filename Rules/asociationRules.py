"""
Association rules 

"""

import statistics as stats
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

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


      return rules
     else:
      return pd.DataFrame()

  #Obtain association rule 
  def defectsDataSet(self,param,head):
     
     basket_sets = (self.df[self.df[head]==param].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))

     basket_sets = basket_sets.applymap(self.encode_units)
     frequent_itemsets = apriori(basket_sets,min_support=0.05, use_colnames=True)

     rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
     return rules
  
  def lenDataset(self,param,head):
     return self.df[self.df[head]==param].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count()

  def lenContainsDataset(self,param,head):
     return self.df[self.df[head].str.contains(param)].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count()

  #Set pandas
  def setPandas(self,df):

        self.df=df
