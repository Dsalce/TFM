

import statistics as stats
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

class Rules(object):


# =============================================================================
# 
# =============================================================================
  def __init__(self):
       self.df=None
       

  def encode_units(self,x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1


  def defectosGRUPDataSet(self,  typeCar):
     self.df= self.df.astype('str')
     basket_sets = (self.df[self.df["GRUP"]==str(typeCar)].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))
     
     basket_sets = basket_sets.applymap(self.encode_units)
     frequent_itemsets = apriori(basket_sets,min_support=0.05, use_colnames=True)
     
     rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
     return rules
       

  def defectosModelDataSet(self,modelCar):
     
     basket_sets = (self.df[self.df["MARCA Y MODELO"]==modelCar].groupby(["DEFEC.", "INSPECCION"])["DEFEC."].count().unstack(level=0).fillna(0))

     basket_sets = basket_sets.applymap(encode_units)
     frequent_itemsets = apriori(basket_sets,min_support=0.05, use_colnames=True)

     rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
     return rules




  def setPandas(self,df):

        self.df=df
