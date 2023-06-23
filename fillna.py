import pandas as pd 
url="http://bit.ly/uforeports"  #Ufonun görüldüğü iller, rengi.şekli.. veriler 

data=pd.read_csv(url)
print(data["Shape Reported"].value_counts(dropna=False))
print("************************************")
print(data["Shape Reported"].fillna(value="belirsiz", inplace=True))