#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Gezinomi yaptığı satışların bazı özelliklerini kullanarak seviye tabanlı (level based) yeni satış tanımları
# oluşturmak ve bu yeni satış tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.
# Örneğin: Antalya’dan Herşey Dahil bir otele yoğun bir dönemde gitmek isteyen bir müşterinin ortalama ne kadar kazandırabileceği belirlenmek isteniyor.
#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################

# Soru 1: miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import pandas as pd
import numpy as np
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df=pd.read_excel("C:/Users/iremb/Desktop/projeler/gezinomi_tanıtım/miuul_gezinomi.xlsx")
df.shape
df.info
df.head()

# Soru 2: Kaç unique şehir vardır? Frekansları nedir?
a=df["SaleCityName"].nunique()
b=df["SaleCityName"].value_counts()

# Soru 3: Kaç unique Concept vardır?
c=df["ConceptName"].nunique()

# Soru 4: Hangi Concept'dan kaçar tane satış gerçekleşmiş?
d=df["ConceptName"].value_counts()

# Soru 5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
e=df.groupby("SaleCityName")["Price"].sum()

# Soru 6: Concept türlerine göre göre ne kadar kazanılmış?
f=df.groupby("ConceptName")["Price"].sum()

# Soru 7: Şehirlere göre PRICE ortalamaları nedir?
g=df.groupby("SaleCityName")["Price"].mean()

# Soru 8: Conceptlere  göre PRICE ortalamaları nedir?
h=df.groupby("ConceptName")["Price"].mean()

# Soru 9: Şehir-Concept kırılımında PRICE ortalamaları nedir?
i=df.groupby(["SaleCityName","ConceptName"]).agg({"Price":"mean"}) #1.yol
j=df.groupby(["SaleCityName","ConceptName"])["Price"].mean() #2.yol

#############################################
# GÖREV 2: satis_checkin_day_diff değişkenini EB_Score adında yeni bir kategorik değişkene çeviriniz.
#############################################
df["EB_score"]= pd.cut((df["CheckInDate"]-df["SaleDate"]).dt.days,bins=[0, 7, 30, 90, float('inf')],
                               labels=["Last Minuters", "Potential Planners", "Planners", "Early Bookers"],
                               right=False)

#############################################
# GÖREV 3: Şehir,Concept, [EB_Score,Sezon,CInday] kırılımında ücret ortalamalarına ve frekanslarına bakınız
#############################################

# Şehir-Concept-EB Score kırılımında ücret ortalamaları
k=df.groupby(["SaleCityName","ConceptName","EB_score"]).agg({"Price":["mean","count"]})

# Şehir-Concept-Sezon kırılımında ücret ortalamaları
l1=df.groupby(["SaleCityName","ConceptName","Seasons"]).agg({"Price":["mean","count"]})

# Şehir-Concept-CInday kırılımında ücret ortalamaları
m=df.groupby(["SaleCityName","ConceptName","CInDay"]).agg({"Price":["mean","count"]})

#############################################
# GÖREV 4: City-Concept-Season kırılımın çıktısını PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.
agg_df=df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending=False)

#############################################
# GÖREV 5: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
agg_df.reset_index(inplace=True)

#############################################
# GÖREV 6: Yeni level based satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# sales_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
agg_df['sales_level_based'] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1) #1.yol
#agg_df["sales_level_based"]=agg_df["SaleCityName"]+"_"+agg_df["ConceptName"]+"_"+agg_df["Seasons"] #2.yol


#############################################
# GÖREV 7: Personaları segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz
# segmentleri betimleyiniz
agg_df["Segment"]=pd.qcut(agg_df["Price"], 4,labels=["D","C","B","A"])
n=agg_df.groupby("Segment").agg({"Price":["mean","max","sum"]})

#############################################
# GÖREV 8: Oluşan son df'i price değişkenine göre sıralayınız.
# "ANTALYA_HERŞEY DAHIL_HIGH" hangi segmenttedir ve ne kadar ücret beklenmektedir?
#############################################
agg_df.sort_values("Price")
z=agg_df[agg_df["sales_level_based"]=="ANTALYA_HERŞEY DAHIL_HIGH"]["Price"].mean()
x=agg_df[agg_df["sales_level_based"]=="GIRNE_YARIM PANSIYON_LOW"]["Price"].mean()
y=agg_df[agg_df["sales_level_based"]=="GIRNE_YARIM PANSIYON_LOW"]









