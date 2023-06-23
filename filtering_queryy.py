import pandas as pd
films=pd.read_csv("pandas/imdb-1000.csv")
print("\n********** Filmlerin Tümü **********\n",films)
print("\n********** Filmlerin Sütunları **********\n",films.columns)
print("\n********** Filmlerin İlk 5 Satırlık Veriler **********\n",films.head())
print("\n********** Filmlerin Son 5 Satırlık Veriler **********\n",films.tail())
print("\n********** Filmlerin ilk 5 Satırlık Title Sütunu Verileri **********\n",films["title"].head())
print("\n********** Filmlerin title ve star_rating Sütunlarının Verileri **********\n",films[['title','star_rating']])
print("\n********** Filmlerin ilk 10 Satırının title ve Star_rating Sütunlarının ilk 5 Verisi **********\n",films[:9][['title','star_rating']].head())
print("\n********** Filmlerin star_rating değeri 8.5 dan büyük olan verilerin title ve Star_rating Sütunları **********\n",
      films[films['star_rating']>8.5][['title','star_rating']])
print("\n********** Filmlerin star_rating'i 8.5 dan eşit ve büyük ve 9.0'dan küçük veya eşit olan title ve star_rating Sütunlarının Verileri **********\n",
      films[(films['star_rating']>=8.5)&(films['star_rating']<=9.0)][['title','star_rating']])
print("\n********** Filmlerin star_rating'i 8.5 dan eşit veya büyük ve 9.0'dan küçük veya eşit olan title ve star_rating Sütunlarının Verileri **********\n",
      films[(films['star_rating']>=8.5)|(films['star_rating']<=9.0)][['title','star_rating']])