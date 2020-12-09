import numpy as np   
import pandas as pd   
a=pd.Series(data=[1,2,3,np.NaN])   
b=pd.Series(data=[4.9,8.2,5.6],index=['x','y','z'])
c=pd.Series(data=[1,1,1,9,9,3,None])
def func(d,f):
    return d + f
print(pd.Series.value_counts(c))  
  
