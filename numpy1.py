import numpy as np

a = np.arange(15) #0'dan 14 e kadar 15 elemanlı dizi döndürür.
print(a)
print("////////")
print(type(a)) #dizinin tipi ndarray olarak döndürülür. yani bir numpy dizisi

b=np.arange(15).reshape(3,5) #3 satır 5 sütunlu bir numpy dizisine çevirir.
print(b) 

print(a.shape) # (15,) 15 elemanlı tek boyutlu bir dizi olduğu anlamına geliyor
print(b.shape)
print("***********************")
print(a.ndim) #1 boyutlu dizi
print(b.ndim) #2 boyutlu dizi

#kendimiz dizi oluşturmak istersek
c=np.array([1,5,7,8,9])
print(c.dtype) #c içerisindeki verilerin int32 türünde olduğunu belirtiyor.


d=np.array([1,"5",7,8,9]) # numpy dizi içerisindeki bütün elemanların aynı tür olmasını ister. Bunların hepsini string olarak algılar.
print(d.dtype)

e=np.array([1,5.2,7,8,9]) #bunların hepsi float64 olarak algılanır.
print(e.dtype)

