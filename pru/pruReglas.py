
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




basket_sets = (df[df['GRUP']==2011].groupby([ "INSPECCION","DEFEC."])["DEFEC."].count().unstack().fillna(0))

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket_sets.applymap(encode_units)
print(basket_sets)
frequent_itemsets = apriori(basket_sets,min_support=0.05, use_colnames=True)
print(frequent_itemsets)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print(rules)



#df = pd.read_excel("/home/dsalce92/Documents/Fichero/OnlineRetail.xlsx")
"""df = pd.read_excel("D:\David_inf\OnlineRetail.xlsx")

df['Description'] = df['Description'].str.strip()
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
df['InvoiceNo'] = df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains('C')]

basket2 = (df[df['Country'] =="France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets2 = basket2.applymap(encode_units)
print(basket_sets2)
basket_sets2.drop('POSTAGE', inplace=True, axis=1)
frequent_itemsets2 = apriori(basket_sets2, min_support=0.05, use_colnames=True)
print(frequent_itemsets2)
rules2 = association_rules(frequent_itemsets2, metric="lift", min_threshold=1)

print("Rules")
print(rules2.head())"""


