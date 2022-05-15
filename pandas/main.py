import pandas as pd
a={"name":["dave","john",'mike','ronaldo'],"last":['sing','ming','jing','ting'],
   "age":[25,26,24,28]}
df=pd.DataFrame(a)
print(df)
print(df[['age','name']])