import pandas as pd

print("------------------")
print("Empty data frame")
df = pd.DataFrame()
print(df)

print("------------------")
print("Dataframe with list")
data = [1,2,3,4,5,'p']
df = pd.DataFrame(data)
print(df)

print("------------------")
print("Dataframe with list")
data = [['PPA',4],['LB',3],['Python',3],['Angular',3]]
df = pd.DataFrame(data,columns=['Name','Duration'])
print(df)

print("------------------")
data = {'Name':['PPA','LB','Python','Angular'],'Duration':[4,3,3,3]}
df = pd.DataFrame(data)
print(df)

print("------------------")
data = [{'Name': 'PPA','Duration': 3,'Fees':10500},{'Name':'Angular','Duration':3,'Fees':10500},{'Name':'Python','Fees':10500}]
df = pd.DataFrame(data)
print(df)

print("------------------")
d = {'one' : pd.Series([1,2,3],index=['a','b','c']),'two': pd.Series([5,6,7,8],index=['x','y','z','w'])}        #series = use as one D array
df = pd.DataFrame(d)
print(df['one'])
print(df['two'])
print(df)
