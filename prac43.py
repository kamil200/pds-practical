import pandas as pd
import numpy as np
df1 = pd.read_excel('emp.xlsx',sheet_name=0)
df2 = pd.read_excel('empl.xlsx',sheet_name=1)
df3 = pd.read_excel('emp.xlsx',sheet_name=2)
df = pd.concat([df1, df2, df3])

df.to_excel('output.xlsx', index=False)
