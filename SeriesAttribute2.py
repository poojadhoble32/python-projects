import numpy as np   
import pandas as pd   
a=pd.Series(data=[1,2,3,4])   
b=pd.Series(data=[4.9,8.2,5.6],  
index=['x','y','z'])   
print(a.ndim, b.ndim)   
print(a.size, b.size)   
print(a.nbytes, b.nbytes)  
