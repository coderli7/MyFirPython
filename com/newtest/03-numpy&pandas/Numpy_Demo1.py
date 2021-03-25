import numpy as np
import pandas as pd


# s = pd.Series([1,2,3,np.nan,44,1])
# print(s)
# print(type(s))


dates = pd.date_range('20160101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)
print(111)
# print (type(df))

