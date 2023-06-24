import numpy as np
from numpy import pi

a = np.linspace(1,10) #default olarak 1 ile 10 arasında 50 tane sayı üretir. 1 ve 10 dahil
print(a)
 
b = np.linspace(1,10,10) #1 ile 10 arasına eşit aralıklarla artan 10 sayı yerleştirir
print(b)

c = np.linspace(1,10,5) #1 ile 10 arasına eşit aralıklarla artan 5 sayı yerleştirir
print(c)

# Matematiksel ve istatistiksel alanlarda kullanılır.
l=np.linspace(0,2*pi,100) #0 ile 360 derece arasındaki sayıların sinüslerini hesaplamış olduk
print(l)
print(np.sin(l))

print( "***********************************************")
x=np.array([2,4,6,8,10])
y=np.array([1,2,3,4,5])

print(x@y)
print(x.dot(y)) #ikisi de matris çarpımını verir.

f=np.zeros((2,4)) # sıfırlardan oluşan 2 satır 4 sütunluk dizi oluşturur.
g=np.ones((2,4))  # birlerden oluşan 2 satır 4 sütunluk dizi oluşturur.
i=np.sum(y) #y'deki sayıların toplamını verir. Sayı olmaları gerekir!
j=np.min(y) #y'deki min değeri yazırır.
k=np.max(y) #y'deki max değeri yazırır.
m=np.sqrt(y) #y'deki sayıların karekökünü alır değeri yazırır.

print("F:",f)
print("g:",g)
print("i:",i)
print("j:",j)
print("k:",k)
print("m",m)
