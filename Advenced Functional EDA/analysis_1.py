import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df=sns.load_dataset("titanic")

#Veri setine ilk uygulanacak fonksiyonlar

df.head()
df.tail()
df.shape
df.info
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

def checkDf(df,head=5):
    print(f"""############################## Shape ############################## \n{df.shape}\n
############################## Head ############################### \n{df.head(head)}\n
############################## Tail ############################### \n{df.tail(head)}\n
############################## İnfo ############################### \n{df.info}
############################## Describe ############################### \n{df.describe([0,0.05,0.95,0.99,1]).T}\n
############################## İndex ############################### \n{df.index}\n
############################## Boş değer var mı? ############################### \n{df.isnull().values.any()}\n
############################## Boş değerlerin toplamı ############################### \n{df.isnull().sum()}\n
""")

df1=sns.load_dataset("tips")
checkDf(df1, 5)