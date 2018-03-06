

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
       
  def defectosDataSet(self):
  	 
     basket2 = (self.df.groupby(["DEFEC.", "INSPECCION"]))
     #.sum().unstack().reset_index().fillna(0)
     #.set_index("INSPECCION"))
     print(basket2)
  """basket_sets = basket2.applymap(encode_units)
  	 basket_sets.drop('POSTAGE', inplace=True, axis=1)
  	 frequent_itemsets = apriori(basket_sets, min_support=0.05, use_colnames=True)
  	 rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)"""
  	 #return basket2
       
  def setPandas(self,df):
        self.df=df