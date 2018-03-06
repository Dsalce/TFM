 
"""import sys
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
   
    main = Main()"""
  


import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#df = pd.read_csv("/home/dsalce92/Documents/Fichero/PITLR5.csv")
df = pd.read_excel("D:\David_inf\PITLR1.csv.xlsx")
df = df.fillna(value="")
#basket_sets = (df.groupby(["DEFEC.", "INSPECCION"]).sum().unstack().reset_index().fillna(0))#.set_index("INSPECCION"))
#
basket_sets = (df[df["GRUP"]==300].groupby(["DEFEC.", "INSPECCION"]).count().unstack(level=0).fillna(0))
#basket_sets=(df[df["GRUP"]==1000].pivot(rows="DEFEC.", columns="INSPECCION", aggfunc='count').fillna(0) )
#print(basket_sets.head())
basket_sets = basket_sets.iloc[80:]
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket_sets.applymap(encode_units)




with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
   print(basket_sets)


frequent_itemsets = apriori(basket_sets, min_support=0.05, use_colnames=True)
print(frequent_itemsets)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold="1")
print(rules)



