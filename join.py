import pandas as pd 

data={'id':[1,2,3,4],
      'ad':["Ali","Ayşe","Bahar","Rukiye"],
       'soyad':["Kaya","Son","Koç","Turan"]}

data2={'id':[1,3,4,7],
      'ad':["Ali","Mehmet","Bahar","Mert"],
       'soyad':["Kaya","Son","Koç","Turan"]}

df1=pd.DataFrame(data)
df2=pd.DataFrame(data2)
print(df1)

print(df1)
print("////////////////////////////")
print(df2)
print("********************************")
print(pd.merge(df1,df2,on="id",how="inner")) #iki dataframe'de id si aynı olanları birleştir ve göster
print("////////////////////////////")
print(pd.merge(df1,df2,on="id",how="left")) #ilk dataframe'deki 4 kişi aynen yazdırılır. 
#birinci datafreme'de olan idi'ler 2.de de varsa sağına eklenir. yoksa nan getirir ama yine getirir.
print("////////////////////////////")
print(pd.merge(df1,df2,on="id",how="right")) #ilk dataframe'deki 4 kişi aynen yazdırılır. 
#birinci datafreme'de olan idi'ler 2.de de varsa sağına eklenir. yoksa nan getirir ama yine getirir.
print("\n*********************************\n")

print(pd.concat([df1,df2])) #Dataları alt alta birbirine ekler
print(pd.concat([df1,df2],axis=1))  #Dataları yan yana birbirine ekler