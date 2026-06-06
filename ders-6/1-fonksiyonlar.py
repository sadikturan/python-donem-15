"""
Fonksiyon Nedir ve Neden İhtiyaç Duyarız?

Yazılım mimarisinde en büyük düşmanımız kod tekrarıdır (DRY - Don't Repeat Yourself). Aynı işlemi yapan 5 satırlık bir kodu projenin 20 farklı yerinde kopyalayıp yapıştırırsak, yarın bir gün o işlemde bir değişiklik yapmamız gerektiğinde 20 farklı yeri tek tek düzeltmek zorunda kalırız. (Yapay Zeka bunu yapıyor)

İşte fonksiyonlar; belirli bir görevi yerine getiren kod bloklarını bir isim altında paketleme mekanizmasıdır. Bir kez yazarız, projenin istediğimiz yerinde sadece adını söyleyerek çağırırız.

"""


# 1: Fonksiyonların Temel Anahatları (Tanımlama vs. Çağırma)

# Bir fonksiyon iki hayati aşamadan oluşur. Tanımlama yapma tarifi deftere yazmaktır (kek pişmez), Çağırma ise o tarife bakarak keki fırına vermektir.

# a- TANIMLAMA (Definition)
# 'def' (define) kelimesiyle Python'a yeni bir paket yapacağımızı söylüyoruz.

def selamla():
    print("Merhaba, Python dünyasına hoş geldiniz!")
    print("Bugün fonksiyonları öğreniyoruz.")

print(selamla)

# DİKKAT: Kod buraya kadar çalıştırılırsa ekrana hiçbir şey basılmaz! 
# Çünkü fonksiyon sadece hafızaya alındı, henüz tetiklenmedi.

# b- ÇAĞIRMA (Calling / Invoking)
# Fonksiyonun adını ve parantezlerini yazarak onu canlandırıyoruz:
selamla()
selamla()  # İstediğimiz kadar çağırıp kodu tekrar kullanabiliriz.

# 2: Parametre ve Argüman Kavramı (Dinamik Fonksiyonlar)

# Yukarıdaki selamla() fonksiyonu her çağrıldığında sabit bir metin basar. Ancak gerçek dünyada fonksiyonların dışarıdan veri alıp esnek çalışmasını isteriz.

# Parametre (Parameter): Fonksiyon tanımlanırken parantez içine yazılan, dışarıdan gelecek veriyi bekleyen boş kutulardır (değişkenlerdir).
# Argüman (Argument): Fonksiyon çağrıldığı an o boş kutuların içine fırlatılan gerçek değerlerdir.

# 'isim' burada bir PARAMETREDİR (Kutunun adı)
def kisiye_ozel_selamla(isim):
    print(f"Merhaba {isim}, nasılsın?")

# "Ahmet" ve "Zeynep" birer ARGÜMANDIR (Kutunun içine düşen gerçek veri)
kisiye_ozel_selamla("Ahmet")
kisiye_ozel_selamla("Zeynep")


# Çoklu Parametre Kullanımı:
def toplama_yap(sayi1, sayi2):
    sonuc = sayi1 + sayi2
    print(f"Sayıların Toplamı: {sonuc}")

toplama_yap(15, 25) # Çıktı: 40

# 3: En Kritik Bölüm - return İfadesi (Değer Döndürme)

# print() sonucu sadece ekrana (konsola) yansıtır, havaya üfler. Kod o veriyi bir daha yakalayamaz.
# return ise fonksiyonun ürettiği sonucu cebe koyar, fonksiyonu o noktada bitirir ve çağrıldığı yere bir çıktı olarak fırlatır. Böylece biz o çıktıyı alıp başka hesaplamalarda kullanabiliriz.

def kare_al(sayi):
    return sayi ** 2 # Hesapla ve fonksiyonun dışına fırlat.

# Fonksiyondan dönen değeri 'besin_karesi' isimli bir değişkende saklıyoruz
besin_karesi = kare_al(5) 
print(besin_karesi) # Çıktı: 25

# return sayesinde bu veriyi başka bir işlemde kullanabiliyoruz:
yeni_hesap = besin_karesi + 10
print(yeni_hesap) # Çıktı: 35

# 4: Fonksiyon Parametre Tipleri 

# A) Default (Varsayılan) Parametreler
# Kullanıcı bir parametreye değer göndermediğinde programın çökmemesi için önceden atanan "varsayılan" değerlerdir.

# 'mesaj' parametresi girilmezse otomatik olarak sağdaki metin kabul edilir.
def log_yaz(kullanici, mesaj="Sisteme giriş yapıldı."):
    print(f"LOG -> [{kullanici}]: {mesaj}")

log_yaz("Ahmet")                             # Çıktı: LOG -> [Ahmet]: Sisteme giriş yapıldı.
log_yaz("Zeynep", "Profilini güncelledi.")   # Çıktı: LOG -> [Zeynep]: Profilini güncelledi.

# B) Keyword (Anahtar Kelimeli) Argümanlar
# Çok parametreli fonksiyonlarda argümanların sırasını karıştırmamak için doğrudan parametre adını belirterek değer gönderebiliriz.

def kayit_ol(isim, soyisim, sehir):
    print(f"Kayıt: {isim} {soyisim} - Şehir: {sehir}")

# Sıralamayı tamamen değiştirsek bile anahtar isimleri belirttiğimiz için kod doğru çalışır:
kayit_ol(sehir="Hatay", soyisim="Yılmaz", isim="Can")

# C) Esnek / Bilinmeyen Sayıda Parametreler (*args ve kwargs)
# Bazen fonksiyona kaç tane veri geleceğini önceden kestiremeyiz.

# *args (Arbitrary Arguments): Fonksiyona sınırsız sayıda düz değer göndermemizi sağlar. İçeride verileri bir Tuple olarak paketler.
# kwargs (Keyword Arguments): Fonksiyona sınırsız sayıda isimli (anahtar=değer) veri göndermemizi sağlar. İçeride verileri bir Sözlük (Dictionary) olarak paketler.

# Kaç sayı geleceği belli değilse (*args):
def tumunu_topla(*sayilar):
    # sayilar arka planda bir tuple'dır: (10, 20, 30, 40)
    return sum(sayilar)

print(tumunu_topla(10, 20, 30, 40)) # Çıktı: 100


# Kaç tane etiket/özellik geleceği belli değilse (**kwargs):
def profili_goster(**bilgiler):
    # bilgiler arka planda bir dict'tir: {'ad': 'Ali', 'meslek': 'Veri Bilimci'}
    for anahtar, deger in bilgiler.items():
        print(f"{anahtar}: {deger}")

profili_goster(ad="Ali", meslek="Veri Bilimci", tecrube="5 Yıl")