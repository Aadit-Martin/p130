import pandas as pd
import csv
df=pd.read_csv("total_stars.csv")
print(df.columns)
df.drop(["Star_name.1","Distance.1","Mass.1","Radius.1","Unnamed: 0","Unnamed: 6"],axis=1,inplace=True)
print(df.shape)
df.to_csv("clnd_tot_stars.csv")