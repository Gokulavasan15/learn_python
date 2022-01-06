from pandas import *
from numpy import *
df = DataFrame(arange(1,21).reshape(5,4),index=['row1','row2','row3','row4','row5'],columns=['1','2','3','4',])
print(df)
print(df.loc['row3','3'])
print(df['1'].value_counts())
