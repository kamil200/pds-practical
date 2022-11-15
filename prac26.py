import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
ds=ds1+ds2
print("add two series:")
print(ds)
print("subtract two series:")
ds=ds1-ds2
print(ds)
print("multiply two series:")
ds=ds1*ds2
print(ds)
print("divide two series:")
ds=ds1/ds2
print(ds)