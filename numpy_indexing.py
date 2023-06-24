import numpy as np

sayilar=np.array([[0,10,20],[25,30,40]])
print(sayilar[:,2]) #bütün satırların 2. sütununu getirir.
print(sayilar[:,0:2]) #bütün satırların 0 ile 2. sütun arasındaki sütunlarını getirir.

sayilar2=np.array([[0,5,10,15,20,25,30,35,40]])
print(sayilar2[::-1]) #diziyi tersten yazdırır.

print(sayilar2[-1,:]) #en sondaki satırın bütün sütunlarını verir.
print(sayilar2[:,-1]) #bütun satırların en sondaki sütunlarını verir.

print(sayilar.ravel()) # çok boyutlu diziyi tek boyutlu hale getirir.
 
print(sayilar.reshape(2,-1)) #2 satırlık bir dizi yap sütun sayısını kendin belirle diyoruz bilgisayarımıza







