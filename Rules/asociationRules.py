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

  

  #Obtain association rule to grup
  def defectosGRUPDataSet(self,  typeCar):
     
     basket_sets = (self.df[self.df["GRUP"]==str(typeCar)].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))
     
     basket_sets = basket_sets.applymap(self.encode_units)
     frequent_itemsets = apriori(basket_sets,min_support=0.05, use_colnames=True)
     
     rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
     return rules
       
  #Obtain association rule to model 
  def defectosModelDataSet(self,modelCar):
     
     basket_sets = (self.df[self.df["MARCA Y MODELO"]==modelCar].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))

     basket_sets = basket_sets.applymap(self.encode_units)
     frequent_itemsets = apriori(basket_sets,min_support=0.05, use_colnames=True)

     rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
     return rules
  #Obtain association rule to model 
  def defectosCATDataSet(self,modelCar):
     
     basket_sets = (self.df[self.df["CAT."]==modelCar].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))

     basket_sets = basket_sets.applymap(self.encode_units)
     frequent_itemsets = apriori(basket_sets,min_support=0.05, use_colnames=True)

     rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
     return rules


  #Set pandas
  def setPandas(self,df):

        self.df=df
