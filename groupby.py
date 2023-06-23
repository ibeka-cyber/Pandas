import pandas as pd
films=pd.read_csv("imdb-1000.csv")
print("\n********** Filmlerin Tümü **********\n",films)
print("\n********** Filmlerin Sütunları **********\n",films.columns)
print("\n********** Filmlerin star_rating'lerinin ortalaması **********\n",films.star_rating.mean())

print("\n********** Filmlerin Her Türü İçin Ortalama **********\n",films.groupby('genre').star_rating.mean())
#buradaki genre listedeki filmlerin türlerini belirten sütunun ismi
