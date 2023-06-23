import pandas as pd 
import numpy as np
s=pd.Series()
data=np.array(["irem","bahar","ayşe"])
s=pd.Series(data,index=[1,2,3])

data2={"a":10,"b":20,"c":100}
s2=pd.Series(data2,index=["b","a","c"]) #dataların yerini değiştirmek için kullanıyoruz.
print(s2)
print("////////////////////")
print(s2[0]) #index ayarlarken b a c yaptığımız için artık 0. indexteki eleman b'nin elemanı olacak bu sebeple 10 değil 20