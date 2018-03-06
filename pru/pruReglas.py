 
import sys
import os
import csv
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


class Main(object):


    def __init__(self):
        
         df = pd.read_csv("/home/dsalce92/Documents/Fichero/PITLR5.csv")
         df = df.fillna(value="")
         basket2 = (df.groupby(["DEFEC.", "INSPECCION"]))
         #.sum().unstack().reset_index().fillna(0)
         #.set_index("INSPECCION"))
         print(basket2)
    

if __name__ == '__main__':
   
    main = Main()
  


import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_csv("/home/dsalce92/Documents/Fichero/PITLR5.csv")
df = df.fillna(value="")
#basket_sets = (df.groupby(["DEFEC.", "INSPECCION"]).sum().unstack().reset_index().fillna(0))#.set_index("INSPECCION"))
#
basket_sets = (df.groupby(["DEFEC.", "INSPECCION"]).count().unstack(level=0).fillna(0))

print(basket_sets.head())
#basket_sets = basket2.applymap(encode_units)
basket_sets.drop('INSPECCION', inplace=True, axis=1)
frequent_itemsets = apriori(basket_sets, min_support=0.05, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold="1")
print(rules)



