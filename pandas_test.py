import pandas as pd


data=pd.read_csv("data.csv")
print(data.head())
print(data.columns)

print(data["Country"].head())
print(data.loc[:,:].tail())
print("**************************")
a= data.loc[:7,"StockCode":"UnitPrice"]
print(a)
print("**************************")
print(data[data["Quantity"]<=6][['Description','CustomerID']]) #miktarı 6 dan küçük olan siparişlerin açıklamaları ve müşteri id'leri gelsin.
print("**************************")
print(data[data["Country"]=="France"][['Description','CustomerID']]) #ülkesi France olan müşterilerin id'leri ve sipariş açıklamaları
print("**************************")
print(data[(data["Country"]=="United Kingdom")][['Description','CustomerID','Country']])
print("**************************")
print("String veri: ",data.loc[1,"Description"])










