import pandas as pd 
import numpy as np


filepath = r"C:\Users\T02574\Documents\usecase.csv"


df = pd.read_csv(filepath)

df1=df["code"]==1
df1=df[df1]

df2=df["code"]==2
df2=df[df2]

df3=df["code"]==3
df3=df[df3]

df4=df["code"]==4
df4=df[df4]

df5=df["code"]==5
df5=df[df5]

df6=df["code"]==6
df6=df[df6]




data1=df1.issue_desc

a1=pd.Series(data1).values

sent=""
for i in a1:
    sent=sent+i

import re

result = re.sub(r'\d+', '', sent)
result=re.sub(r'\b\w{1,3}\b','',result)


words = re.split(r'\W+',result) 

lwords=[t.lower() for t in words]

dis=[]
for i in lwords:
    if i not in dis:
        dis.append(i)
