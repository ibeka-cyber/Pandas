
def kaderSayisi(name):
    list_1=["A","J","S","Ş"]
    list_2=["B","K","T"]
    list_3=["C","Ç","L","U","Ü"]
    list_4=["D","M","V"]
    list_5=["E","N","W"]
    list_6=["F","O","Ö","X"]
    list_7=["G","Ğ","P","Y"]
    list_8=["H","Q","Z"]
    list_9=["I","İ","R"]
    
    toplam=0
    yeni_toplam=0
    for i in range(len(name)):
        if name[i] in list_1:
            toplam +=1
        elif name[i] in list_2:
            toplam +=2
        elif name[i] in list_3:
            toplam +=3
        elif name[i] in list_4:
            toplam +=4
        elif name[i] in list_5:
            toplam +=5
        elif name[i] in list_6:
            toplam +=6
        elif name[i] in list_7:
            toplam +=7
        elif name[i] in list_8:
            toplam +=8
        elif name[i] in list_9:
            toplam +=9
        else:
            pass
    if toplam>=10:
        for rakam in str(toplam):
            yeni_toplam +=int(rakam)
            toplam=yeni_toplam
            if toplam>=10:
                yeni_toplam=0
                for rakam in str(toplam):
                    yeni_toplam +=int(rakam)
                    toplam=yeni_toplam
        return toplam
        
    else:
        return toplam
        
    

def SayiAnlami(sayi):
    sayi_1="""Kader sayısı 1 olan bireyler toplumda öncü kişilerdir. 
    Mutlu ve enerjik olduğu durumlarda etrafında olan kişileri motive edip empati kurabilirler. 
    1, enerjisini keşfettiği müddetçe “öz” kavramını ortaya çıkarır. Özgüven, özsaygı ve özsevgi bunlardandır. 
    Kendini keşfeden 1, yeteneklerini de tanıyarak kendine duyduğu saygı, sevgi ve güven de artar."""
    
    sayi_2="""Kader sayısı 2 olan bireylerin gözlem yeteneği ve empati özelliği gelişmiş demektir.
    Etrafındaki insanların dilinden kolayca anlarlar. 
    Deyim yerinde ise tüm sevgisi ve ilgisi ile toplumun ilacı olurlar . 
    Dargınlıkları ve kavgaları hiç sevmezler."""
    
    sayi_3="""Sanat kabiliyeti, sosyal kişilik, dostluk meyli, yüzeysellik, ziyankarlık. 
    Bu insan dışa dönüktür. Hayatı ve eğlenceyi sever. Yaratıcı ve duyarlıdır. Rutinden hoşlanmaz. 
    Kendine disiplin uygulamayı öğrenmelidir.
    
    Meslekler: Öğretim üyesi, avukat, yargıç, büyükelçi, asistan, polis, felsefeci, bankacı, reklamcı."""
    
    sayi_4="""Pratiklik, uygulayıcılık, güvenilirlik, bükülmezlik, Sağlamlık. Sıkı bir çalışandır. 
    Her şeyin başarılmasını ister. İyi bir arkadaş ve candan olmayı öğrenmelidir. 
    Güvenlik duygusunun aşırılığından sakınmalıdır.
    
    Meslekler: Pilot, madenci, tekniker, modacı, mühendis, astrolog, öğretim görevlisi"""
    
    sayi_5="""Özgürlük, uyum kabiliyeti, gezginlik, değişkenlik. 
    Cesur, yürekli ve ikna edici bir kişiliktir. Güzel şeylerden ve bunlara sahip olmaktan hoşlanır. 
    Can sıkıntısından fazla etkilenir. Bunun aşırılığından sakınmalıdır.
    
    Meslekler: Mühendis, satış & pazarlamacı, muhasebeci, gazeteci, radyocu, televizyoncu, broker, emlak komisyonculuğu."""
    
    sayi_6="""Aşk, sorumluluk, anlayış, her işe karışmak, kıskançlık. Sıcak, koruyucu ve mutlu kişiliktir.
    Güvenilir ve sağlam yapıdır. Sevdiği insan için her türlü fedakarlığı yapar. 
    Kendini aşırı kötümser hissetmekten ve başkaları tarafından istismar edilmiş duygusundan arınmalıdır.
    
    Meslekler: Kuyumcu, mühendis, mimarlık, gıda müfettişi, roman yazarı, bürokrat, sanatçı."""

    sayi_7="""Ruhsallık, zihni analizcilik, zeka, eleştiricilik, sır saklama ve baskıcılık.
    Derin bir düşünürdür. Ruhsal meyillidir. Eksantrik ve değişkendir. Soğuk ve mesafeli durmaktan kaçınmalıdır. 
    Yalnızlıktan ve iyi şeylere sahip olamama duygusundan arınmalıdır.
    
    Meslekler: Film sinema sektörü, seyahat acentesi, hostes, doktor, kimyager."""

    sayi_8="""Yöneticilik yetenekleri, organizasyon yeteneği, güçlülük, maddi ve adil.
    Güçlü, kararlı ve sonuca giden kişiliktir. Para ve maddi konularda başarılıdır.
    Amacının karşısında gördüğü insanlar için duygusuz davranma meylinden arınmalıdır.
    
    Meslekler: Oyuncu, mühendis, polis, belediye başkanı, siyasetçi müzisyen."""
    
    sayi_9="""Sanatkar, hümanist, romantik, duygusallık, konfor, sezgili, duyarlı ve yaratıcı kişiliktir.
    Dünyaya kendini kanıtlamak için savaşır. 
    Kötü alışkanlıklarından kurtulmak ve hayatın küçük detaylarından fazla etkilenmemek için çalışmalıdır.

    Meslekler: Ceo, lider, polis, komutan, itfaiyeci, çocuk doktoru, bankacı, uçak mühendisi."""
    
    if sayi==1:
            print(sayi_1)
    elif sayi==2:
             print(sayi_2)
    elif sayi==3:
            print(sayi_3)
    elif sayi==4:
            print(sayi_4)
    elif sayi==5:
            print(sayi_5)
    elif sayi==6:
            print(sayi_6)
    elif sayi==7:
            print(sayi_7)
    elif sayi==8:
            print(sayi_8)
    elif sayi==9:
            print(sayi_9)
    else:
            pass
            
name=[]
sayi=[0,1,2,3,4,5,6,7,8,9]
nam=input("Adınızı giriniz: ")
nam= nam.upper()
nam=nam.replace(" ","")
for x in range(len(nam)):
    name.append(nam[x])
if nam.isalpha()==False:
    print("Geçersiz karakter Girildi!")
else:
    print("Kader sayınız: ",kaderSayisi(name))
    print(kaderSayisi(name),"sayısının anlamı: ")
    SayiAnlami(kaderSayisi(name))   