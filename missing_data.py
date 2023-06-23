import pandas as pd 
url="http://bit.ly/uforeports"  #Ufonun görüldüğü iller, rengi.şekli.. veriler 

data=pd.read_csv(url)
print(data[["City","Colors Reported","Shape Reported","State","Time"]].head()) # ilk 5 veriyi gösterdik

print("Datanın sütunları: ",data.columns)
print(data.isnull().head(100)) # ilk 100 satırdaki verilere bakar. Veri varsa False, Veri yoksa True yazar
print(data.notnull().head(100))# üsttekinin tam tersi
print(data.isnull().sum())# boş olan verilerin toplam sayısını verir.
print("*************************")
print(data[data.City.isnull()]) #şehir bilgisi boş olan alanları getirir.

