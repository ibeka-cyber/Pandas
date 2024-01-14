import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from generalization_4 import grab_col_names

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df=sns.load_dataset("titanic")

######################################################
#Hedef Değişkeni Kategorik Verilere Göre Analiz Etmek
######################################################

#Burada hedef değişkenimiz survived yani hayatta kalıp kalmama durumu olacak.

cat_cols,num_cols,cat_but_car = grab_col_names(df)
df["survived"].value_counts()

#bakalım yaşın hayatta kalma durumuna etkisi var mı
df.groupby("sex")["survived"].mean()
# %74 ile kadınların hayatta kalma oranı erkeklere göre daha yüksek.
# bütün kategorik değişkenlere göre analiz etsek

def target_summary_with_cat(df,target,categorical_col):
    print(df.groupby(categorical_col)[target].mean())
    print("********************************************************")
    
for col in cat_cols:
    target_summary_with_cat(df, "survived", col)
    

#buradan oranlara bakılarak hayatta kalma durumunun üzerindeki etkiler tartışılabilir...

#############################################################
#Hedef Değişkeni Sayısal(Numerik) Verilere Göre Analiz Etmek
#############################################################

df.groupby("survived").agg({"fare":"mean","age":"mean"})

def target_summary_with_num(df,target,numerical_col):
    print(df.groupby(target).agg({numerical_col:"mean"}))
    print("********************************************************")
    
for col in num_cols:
    target_summary_with_num(df, "survived", col)    
    
    
    
    
    
    
    