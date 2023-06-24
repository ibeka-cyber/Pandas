import numpy as np

a=np.floor(np.random.random((3,5))*10) # 3 satır 5 sütunluk random dizi oluşturur.
b=np.floor(np.random.random((3,5))*10) # 3 satır 5 sütunluk random dizi oluşturur.

c=np.vstack((a,b)) #dikey olarak dizileri birleştirir.
d=np.hstack((a,b)) #yatay olarak dizileri birleştirir.

print(c)
print("******************")
print(d)

e=[[5,3,7],[8,9,1]]
f=[[2,4,6],[7,1,8]]

g=np.vstack((e,f)) #dikey olarak dizileri birleştirir.
h=np.hstack((e,f)) #yatay olarak dizileri birleştirir.

print(g)
print("******************")
print(h)
