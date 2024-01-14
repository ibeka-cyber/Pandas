#****************************************************************
#Kategorik Değişken Analizi (Analysis of Categorical Veriables)
#****************************************************************
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df=sns.load_dataset("titanic")
#veri tipi category, object veya bool olanların içerisinde category değişken olanları bulmak
cat_cols=[col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]

#numeerik değişkenler arasında gizlenmiş kategorik değişkenleri bulmak
#unique değer sayısı 10 dan küçükse 10dan az sınıfı var demektir bunu kategorik sayabiliriz.
num_but_cat=[col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64","float64"]]

#kategorik değişkenler içerisinde çok fazla sınıfı olan değişken çok yüksek ihtimalde onun bilgi 
#taşımadığını gösterir. Bu sebeple kategorik gözüken ama kategorik olmayan verileri de yakalıyoruz. iki yolla
cat=[col for col in cat_cols if df[col].nunique()>10 and str(df[col].dtypes) in ["category","object"]] # 1.yol
cat2=[col for col in cat_cols if df[col].nunique()>10] #2. yol 

#tüm kategorik sütunları bir araya toplayalım
cat_cols += num_but_cat

#eğer kategorik değişkenlerin içerisinde kategorik olmayanlar olaydı onları çıkarmamız gerekirdi.
cat_cols=[col for col in cat_cols if col not in cat] 

#bütün kategorik verilere bakalım
df[cat_cols]

#peki bulduğumuz değişkenler tutarlı mı? bunun için sınıf sayılarına bakalım
df[cat_cols].nunique() #hepsi 10 dan küçük 

# sayısal değişkenleri seçelim
num=[col for col in df.columns if col not in cat_cols]


#Datayı verdiğimizde bize sütunlarının sınıf sayısını ve sınıfın oranını veren bir fonksiyon yazalım
def cat_summary(dataframe,col_name,plot=False):
    """print(pd.DataFrame({col_name:dataframe[col_name].value_counts(),
                        "Ratio":100* dataframe[col_name].value_counts()/ len(dataframe)}))
    print("*********************************************")"""
    if plot:
        sns.countplot(x=dataframe[col_name],data= dataframe)
        plt.show(block=True)
for col in df:
    cat_summary(df, col)


#şimdi yukarıda yaptığımız kategorik değişken yakalama işini bir fonksiyona atalım
def catch_cat(df,plot=False):
    cat_cols=[col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]
    num_but_cat=[col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64","float64"]]
    cat2=[col for col in cat_cols if df[col].nunique()>10]
    cat_cols += num_but_cat
    print(cat_cols)
    if plot:
        for col in cat_cols:
            plt.figure()
            sns.countplot(x=df[col],data= df)
            plt.show(block=True)
            
    return cat_cols

catch_cat(df,plot=True)