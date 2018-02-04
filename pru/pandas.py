import pandas as pd
import numpy as np
 
data = {'name': ['Alice', 'Bob', 'Charles', 'David', 'Eric'],
        'year': [2017, 2017, 2017, 2017, 2017],
        'salary': [40000, 24000, 31000, 20000, 30000]}
 
df = pd.DataFrame(data, index = ['Acme', 'Acme', 'Bilbao', 'Bilbao', 'Bilbao'])
 
print(df)