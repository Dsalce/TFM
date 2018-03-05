

import statistics as stats
import pandas as pd

class Rules(object):


# =============================================================================
# 
# =============================================================================
  def __init__(self):
       pass
       
  def defectosDataSet(self):
  	 basket2 = (self.df['GRUP']
          .groupby(['DEFEC.', 'INSPECCION'])
          .sum().unstack().reset_index().fillna(0)
          .set_index('INSPECCION'))

  	 basket_sets2 = basket2.applymap(encode_units)
  	 basket_sets2.drop('POSTAGE', inplace=True, axis=1)
  	 frequent_itemsets2 = apriori(basket_sets2, min_support=0.05, use_colnames=True)
  	 rules2 = association_rules(frequent_itemsets2, metric="lift", min_threshold=1)
  	 return rules2
       
  def setPandas(self,df):
        self.df=df