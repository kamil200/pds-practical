import pandas as pd
import numpy as np
df = pd.read_excel('emp.xlsx')
result = df.sort_values('hire_date')
result
