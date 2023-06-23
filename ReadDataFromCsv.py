import pandas as pd
notlar= pd.read_csv("pandas/grades.csv")
notlar.columns=["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuç"]

print("\n********** Notların Tümü **********\n",notlar)
print("\n********** Notlar'ın Veri Tipi **********\n",type(notlar))
print("\n********** Notlar'ın ilk 5 Verisi **********\n",notlar.head())
print("\n********** Notlar'ın son 5 Verisi **********\n",notlar.tail())
print("\n********** Notlar'ın Final Sütunu **********\n",notlar["Final"])
print("\n********** Notlar'ın 2. İndex'indeki Veri **********\n",notlar.iloc[2])
print("\n********** Notlar'ın 0 ile 9. Satır Arasındaki Veriler **********\n",notlar[0:10])
print("\n********** Notlar'ın Bütün Satırların İsim Sütunu **********\n",notlar.loc[:,"İsim"])
print("\n********** Notlar'ın 5.Satırına Kadar İsim Sütunu Verileri **********\n",notlar.loc[:5,"İsim"])
print("\n********** Notlar'ın 5.Satırına kadar İsim ile Test4 Arası Bütün Sütunların Verileri **********\n",notlar.loc[:5,"İsim":"Test4"])
print("\n********** Notlar'ın 5.Satırına Kadar İsim ve Test4 Sütunu Verileri **********\n",notlar.loc[:5,["İsim","Test4"]])
print("\n********** Notlar'ın 5.Satırına kadar, Baştan Test2 Sütununa dek Olan Veriler **********\n",notlar.loc[:5,:"Test2"])
print("\n********** Notlar'ın Bütun Satırlarının Tersten Yazılmış İsmin Sütunu Verileri **********\n",notlar.loc[::-1,"İsim"])