#coding:utf8
import pandas as pd
import datetime

df = pd.read_csv("E:\\data\\30AGL9min5copy.csv")


df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S', errors='raise')

print(df)
for i in range(len(df)):
    print(i)
    if df['date'].loc[i].hour > 20 :
        df.loc[i,"l"] = df['date'].loc[i]+ datetime.timedelta(days=-1)
        
        df.loc[i,'date'] = df.loc[i,"l"]
    print(df.loc[i,'date'])
    
df.to_csv("E:\\data\\30AGL9min5test.csv")
