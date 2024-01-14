from analysisOfCategoricVeriables_2 import catch_cat
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")

def numeric_cols(df,plot=False):
        cat_cols = catch_cat(df)
        num_cols = [col for col in df.columns if df[col].dtypes in ["int64","float64"]]
        num_cols=[col for col in num_cols if col not in cat_cols]
        if plot:
            for col in num_cols:
                plt.figure()
                df[col].hist()
                plt.xlabel(col)
                plt.title(col)
                plt.show()
        return num_cols
            
numeric_cols(df,plot=True)