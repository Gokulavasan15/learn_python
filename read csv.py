from pandas import *
from numpy import  *
df = DataFrame(arange(1,21,1).reshape(5,4),index=['row1','row2','row3','row4','row5'],columns=['column1','column2','column3','column4'])
print(df)
print(df.iloc[0,2])