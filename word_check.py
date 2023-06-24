
import pandas as pd
data=pd.read_csv("data.csv")

word="white".upper()
print(data.head())
print("********************************")
for x in range((len(data.head()))):
    a = data.loc[x,"Description"].split()
    for i in range(len(a)):
        if a[i]== word:
            print("")    
            print(x,". Veride {0} kelimesi mevcuttur. ".format(word),(data.loc[x,["CustomerID","Description","Country"]]))
        