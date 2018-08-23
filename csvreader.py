import pandas as pd
import numpy as np
import os

filepath='/home/proteus/Downloads/Python/jumlahterkumpulkenderaanjpj2015.csv'
df=pd.read_csv(filepath, error_bad_lines=False, sep=';')
data=pd.DataFrame(df)
#motorcar=data.
print(data)
