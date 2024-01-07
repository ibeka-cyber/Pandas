import seaborn as sns
import pandas as pd
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df=sns.load_dataset("car_crashes")

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
["NUM_"+col.upper() if df[col].dtype != 'O' else col.upper()  for col in df] 

# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
[col.upper()+"_FLAG" if "NO" not in col.upper() else col.upper() for col in df]

# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################
#1.yol:comprehension kullanmadan pandas ile sütun atma
new=df1.drop(df[["abbrev","no_previous"]],axis=1)
new.head()
#2.yol:list comprehension ile
rem=["abbrev","no_previous"]
[col for col in df if col not in rem]

##################################################
# Pandas Alıştırmalar
##################################################
import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################
df11=sns.load_dataset("titanic")

#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################
df11["sex"].value_counts()

#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################
df11.nunique()

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################
df11["pclass"].nunique()

#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################
df11[["pclass","parch"]].nunique()

#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################
df11["embarked"].dtype
df11["embarked"] = df11["embarked"].astype("category")
df11["embarked"].dtype
df11.info()

#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################
df11[df11["embarked"]=="C"]

#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################
df11[df11["embarked"]!="S"].head(5)
df11[df11["embarked"] != "S"]["embarked"].unique()
df11[~(df11["embarked"] == "S")]["embarked"].unique()

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################
df11[(df11["age"]<30) & (df11["sex"]=="female")]

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################
df11[(df11["fare"]>500) | (df11["age"]>70)]

#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################
df11.isnull().sum()

#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################
new2=df11.drop("who",axis=1, inplace=True)

#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################
df11["deck"].fillna(df11["deck"].mode[0],inplace=True)

#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################
df1["age"].fillna(df1["age"].median(),inplace=True)

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################
df1.groupby(["pclass","sex"]).agg({"survived": ["sum","count","mean"]})

#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################
def age_30(age):
    if age<30:
        return 1
    else:
        return 0
df1["age_flag"] = df1["age"].apply(lambda x : age_30(x))
df1["age_flag"] = df1["age"].apply(lambda x: 1 if x<30 else 0)

#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################
df1 = sns.load_dataset("tips")

#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################
df1.groupby("time").agg({"total_bill": ["sum","min","mean","max"]})


#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################
df1.groupby(["day","time"]).agg({"total_bill": ["sum","min","mean","max"]})

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################
df1[(df1["time"] == "Lunch") & (df1["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum","min","max","mean"],"tip":  ["sum","min","max","mean"],"Lunch" : lambda x:  x.nunqiue()})

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################
df1.loc[(df1["size"] < 3) & (df1["total_bill"] >10 ) , "total_bill"].mean() 

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################
df1["total_bill_tip_sum"] = df1["total_bill"] + df1["tip"]

#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################
new_df1 = df1.sort_values("total_bill_tip_sum", ascending=False)[:30]







