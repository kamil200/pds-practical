
import pandas as pd

data = {'Name': ['okay', 'mk', 'shoban', 'kamil'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['btech', 'BE', 'BE', 'Btech']}
  

df = pd.DataFrame(data)
  

address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
  

df['Address'] = address

print(df)