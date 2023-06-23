import pandas as pd
data=[13,20,30,40,50]
df=pd.DataFrame()
data2=[["İrem Bahar",23,"Kocaeli"],["Hatice",22,"Erzurum"],["Didem",22,"Diyarbakır"]]
df2=pd.DataFrame(data2,columns=["İsim","Yaş","Şehir"],index=[1,2,3])
print(df2)

print("**************************************************")
data3={"İsim":["İrem Bahar","Hatice","Didem"],
       "Yaş":[23,22,22],
       "Şehir":["Kocaeli","Erzurum","Diyarbakır"]}

df3=pd.DataFrame(data3, columns=["İsim","Yaş","Şehir"],index=[1,2,3])
print(df3)

print("**************************************************")

del df3["Şehir"] #şehir kolonunu siler. df3.pop("Şehirler") de aynı işlemi yapar
print(df3)
print("**************************************************")

print(df3.loc[2]) #2.nin verilerini söyler yani Hatice 22 
print(df3.iloc[1]) #1. indexteki verileri verir yani Hatice 22 
# şehir kolonu silindiği için getirmedi ama silinmeseydi erzurum olarak onu da getirecekti.

print("**************************************************")
df4=df3.append(df2) #dataları birbirine ekler. df3 e df2 yi ekledi.
print(df4.head()) #df4'ün ilk 5 verisini getirir.
print("///////////")
print(df4.tail()) #df4'ün son 5 verisini getirir.
