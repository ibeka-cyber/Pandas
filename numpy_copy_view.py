import numpy as np

a=np.array([2,5,8])
b=a
b[0]=1

print(a) #ikisinde de 0. index 1 oldu. Çünkü aynı referansa sahipler.
print(b)

print("************************************")

c=a.copy()
c[0]=10
print(a)
print(c) #sadece c değişti çünkü hafızada c dizisi için a'nın kopyalandığı yeni bir nokta oluşturuldu.

print("************************************")

d=a.view()
d.shape = 3,1
print(a)
print(d) # görüntü alındığında aynı şekilde hafızada farklı bir alan açılır. Bu sebeple yapılan değişiklik sadece d için geçerli oldu.
