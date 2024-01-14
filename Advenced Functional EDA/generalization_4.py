import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df=sns.load_dataset("titanic")

def grab_col_names(df,cat_th=10,car_th=20):
    
    """
    Veri setindeki kategorik, nümerik ve kategorik görünümlü kardinal değişkenlerin isimlerini verir

    Parameters
    ----------
    df : dataframe
        Değişken isimleri almak istenen dataFrame'dir.
    cat_th : int, float
        Nümerik fakat kategorik değişkenler için sınıf eşik değeri. The default is 10.
    car_th : int, float
        Kategorik fakat kardinal değişkenler için sınıf eşik değeri . The default is 20.

    Returns
    -------
    cat_cols : list
        Kategorik değişken listesi
    num_cols : list
        Numeik değişken listesi
    cat_but_car : list
        Kategorik görünümlü kardinal değişken listesi
        
    Notes
    ------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.
    """
    cat_cols=[col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]
    num_but_cat=[col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64","float64"]]
    cat_but_car=[col for col in cat_cols if df[col].nunique()>10]
    cat_cols += num_but_cat
    cat_cols= [col for col in cat_cols if col not in cat_but_car]
    
    num_cols = [col for col in df.columns if df[col].dtypes in ["int64","float64"]]
    num_cols=[col for col in num_cols if col not in cat_cols]
      
    print("\nKategorik değişkenler: ",cat_cols)
    print("\n**************************************************************\nNümerik değişkenler: ",num_cols)
    print("\n**************************************************************\nKategorik görünen fakat çok fazla sınıfı olmasından dolayı gereksiz olan kategoriler: ",cat_but_car)
    print("***************************************************************************")
    print(f"Observations: {df.shape[0]}")
    print(f"Veriables: {df.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}\n*****************************************************************")
    return cat_cols,num_cols,cat_but_car
    

cat_cols,num_cols,cat_but_car = grab_col_names(df)