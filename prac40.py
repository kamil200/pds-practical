import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)
df=pd.DataFrame({
    'year':[1986,1986,1985,1985],
    'WHO region':['western pacific','americas','afric','south east-asia'],
    'country':['vietnam','urugauy','cte d ivoire','democratic people republic of korea'],
    'beverage types':['wine','other','wine','wine'],
    'display value':[0,0.5,1.62,0]})
print("Original orders DataFrame:")
print(df)
def color_negative_vietnam(val):
    color='vietnam'if val<0 else 'cte d ivoire'
    return 'color: %s' % color
print("\n Negative numbers vietnam and positive number cte d ivoire:")
df.style.highlight_null(null_color='vietnam')
