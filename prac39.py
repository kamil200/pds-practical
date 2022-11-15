import pandas as pd
pd.set_option('display.max_rows',None)
df=pd.DataFrame({
    'year':[1986,1986,1985,1985],
    'WHO region':['western pacific','americas','afric','south east-asia'],
    'country':['viet nam','urugauy','cte d ivoire','democratic people republic of korea'],
    'beverage types':['wine','other','wine','wine'],
    'display value':[0,0.5,1.62,0]})
print("Original orders DataFrame:")
print(df)
print("\n Group by with multiple aggregations:")
result=df.groupby(['year','display value']).agg({'display value':['max','mean'],
                                                 'year':['sum','min','count']})
print(result)

