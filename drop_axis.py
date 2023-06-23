import pandas as pd 
films=pd.read_csv("imdb-1000.csv")
print("\n********** Filmlerin Sütunları **********\n",films.columns)


print(films.drop("content_rating",axis=1).columns)#films içerisindeki content_ratig sütununu kaldır işime yaramıyor kullanmayacağım demek
#burada axis değeri sıfır olursa (axis=0) satırı sil, bir olursa (axis=1) sütunu sil demek
print("******************")
print(films.drop("actors_list",axis=1))#actor_list sütununu sil.
print(films.drop(2,axis=0))#indexi 2 olan satırı sil

print("/////////////////////////////////////////////////////////////")

rowtoDrop=[0,1,3,5,7,9,10]

films=films.drop(rowtoDrop,axis=0)
print(films.mean())
