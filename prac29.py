import pandas as pd
import numpy as np

job_data={'sr.no':[1,2,3,4,5,6],
          'emp.no': [1,2,3,4,5,6],
          'name': ['james','robert','vikas','shelina','john','radhika'],
          'designation': ['manager','sr.engineer','developer','programmer','manager','programmer'],
          'salary': ['200000','300000','50000','30000','nan','nan']}

df=pd.DataFrame(job_data)
print("original rows:")
print(df)
df.sort_values(by=['name','designation'],ascending=[False,True])
print("Sort the data frame first by 'name' in descending order,then by 'score' in ascending order:")
print(df)



