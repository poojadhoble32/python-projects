import numpy as np   
import pandas as pd   
a=pd.Series(data=[1,2,3,np.NaN])   #instead of np.NaN can use None
b=pd.Series(data=[4.9,8.2,5.6],index=['x','y','z'])   
c=pd.Series()   
print(a.empty,b.empty,c.empty)   
print(a.hasnans,b.hasnans,c.hasnans)   
print(len(a),len(b))   
print(a.count( ),b.count( ))  
