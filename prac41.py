import pandas as pd
import numpy as np

df = pd.read_excel('emp.xlsx')
df[df['hire_date'] >='01-01-05']
