"""
Python'da kod yazma hızımızı artıran, döngü kurma ihtiyacını azaltan ve fonksiyonel programlama yapmamızı sağlayan Lambda yapısı ve en sık kullanılan Gömülü (Built-in) Fonksiyonları detaylıca inceleyelim.

Bu fonksiyonlar özellikle veri analitiğinde veri setlerini hızlıca manipüle etmek, temizlemek ve filtrelemek için hayati öneme sahiptir.
"""
# 1. Lambda Fonksiyonu (İsimsiz Fonksiyonlar)

# Normalde bir fonksiyonu def ile tanımlarız. Ancak sadece tek satırlık, basit bir işlem yapacak ve kod içinde sadece birkaç yerde kullanılacak geçici bir fonksiyona ihtiyacımız varsa Lambda (Anonymous / İsimsiz) fonksiyonları kullanırız.

# Yazım Kuralı: lambda parametreler : yapılacak_işlem

# Örnek: İki sayıyı toplayan bir lambda fonksiyonu
topla = lambda x, y: x + y
print(topla(5, 3))  # Çıktı: 8      (lambda x, y: x + y)(1, 2)  # Çıktı: 3

print((lambda x: x**2)(4))  # Çıktı: 16

# Gelen metni temizleyip baş harflerini büyüten lambda
formatla = lambda metin: metin.strip().title()

print(formatla("   python programlama dili   "))  
# Çıktı: "Python Programlama Dili"

# @ işaretinden sonrasını alan lambda fonsiyonu
domain_bul = lambda eposta: eposta.split("@")[1]

print(domain_bul("ahmet.yilmaz@sirket.com"))  
# Çıktı: "sirket.com"

durum_analizi = lambda sayi: "Pozitif" if sayi > 0 else ("Negatif" if sayi < 0 else "Sıfır")

print(durum_analizi(15))   # Çıktı: Pozitif
print(durum_analizi(-8))   # Çıktı: Negatif
print(durum_analizi(0))    # Çıktı: Sıfır

# Gömülü (Built-in) Fonksiyonlar
# Python, birçok yerleşik fonksiyon sunar. Bunlar, veri analitiğinde sıkça kullanılan fonksiyonlardır.

# 2. map() Fonksiyonu: Eldeki bir listenin tüm elemanlarına belirli bir fonksiyonu tek tek uygulamak ve sonuçlardan yeni bir liste üretmek için kullanılır. Bizi for döngüsü yazmaktan kurtarır.

sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda x: x**2, sayilar))
print(kareler)  # Çıktı: [1, 4, 9, 16, 25]

# Not: map() fonksiyonu geriye özel bir obje döner, sonucu liste olarak görmek için başına list() ekleriz.

sonuc = map(lambda x: x**2, sayilar)

print(next(sonuc))  # 1
print(next(sonuc))  # 4

# 3. filter() Fonksiyonu: Eldeki bir listenin elemanlarından, belirlediğimiz bir koşula uymayanları elemek (filtrelemek) için kullanılır. Fonksiyonun True döndüğü elemanları tutar, False dönenleri atar.

yaslar = [14, 18, 22, 16, 30, 25]

# Sadece reşit olanları (>= 18) filtreleyelim
resitler = list(filter(lambda yas: yas >= 18, yaslar))

print(resitler) # Çıktı: [18, 22, 30, 25]

# 4. any() ve all() Fonksiyonları:
# all() (Hepsi): Listenin içindeki tüm elemanlar True ise sonuç True olur. Bir tane bile False varsa False döner. (Mantıksal and gibi çalışır).

# any() (Herhangi biri): Listenin içinde en az bir tane True varsa sonuç True olur. Sadece hepsi False ise False döner. (Mantıksal or gibi çalışır).

# Örnek: Bir listede en az bir tane çift sayı var mı?
sayilar = [1, 3, 5, 7, 8]
cift_var_mi = any(map(lambda x: x % 2 == 0, sayilar))
print(cift_var_mi)  # Çıktı: True

# Örnek: Bir listede tüm sayılar pozitif mi?
sayilar = [1, 3, 5, -2, 8]  
tum_pozitif_mi = all(map(lambda x: x > 0, sayilar))
print(tum_pozitif_mi)  # Çıktı: False

# Bir öğrenci not listesindeki tüm öğrencilerin geçip geçmediğini kontrol edelim (geçme notu 50 olsun).
notlar = [55, 70, 45, 80, 60]
tum_gecip_mi = all(map(lambda notu: notu >= 50, notlar))
print(tum_gecip_mi)  # Çıktı: False (Çünkü 45 geçemedi)

# 5. sorted() Fonksiyonu: Bir listeyi orijinal halini bozmadan (küçükten büyüğe veya alfabetik olarak) sıralayıp bize yeni bir liste verir. (list.sort() metodu orijinal listeyi bozarken, sorted() bozmaz).

skorlar = [45, 90, 12, 78]

sirali_skorlar = sorted(skorlar) 
print(sirali_skorlar) # [12, 45, 78, 90]

# Tersten (Büyükten küçüğe) sıralamak için:
ters_sirali = sorted(skorlar, reverse=True) # [90, 78, 45, 12]

# Sözlükleri Belirli Bir Alana Göre Sıralama

ogrenciler = [
    {"ad": "Ali", "not": 85},
    {"ad": "Ayşe", "not": 90},
    {"ad": "Mehmet", "not": 75}
]

# Öğrencileri notlarına göre sıralayalım
sirali_ogrenciler = sorted(ogrenciler, key=lambda x: x["not"], reverse=True)
print(sirali_ogrenciler)

# 6. min() ve max() Fonksiyonları: Bir listenin veya veri grubunun içindeki en küçük (min) ve en büyük (max) değeri bulur. Tıpkı sorted gibi key parametresi alabilirler.

sayilar = [3, 7, 1, 9, 5]
en_kucuk = min(sayilar)  # 1
en_buyuk = max(sayilar)   # 9
print(f"En küçük sayı: {en_kucuk}, En büyük sayı: {en_buyuk}")

# Sözlüklerde en yüksek notu alan öğrenciyi bulalım
ogrenciler = [
    {"ad": "Ali", "not": 85},
    {"ad": "Ayşe", "not": 90},
    {"ad": "Mehmet", "not": 75}
]

en_yuksek_notlu_ogrenci = max(ogrenciler, key=lambda x: x["not"])
print(en_yuksek_notlu_ogrenci)

# 7. abs(), sum(), round() Fonksiyonları
# abs() (Absolute Value): Bir sayının mutlak değerini (işaretsiz halini) verir.
# sum(): Bir listenin içindeki tüm sayısal değerleri toplar.
# round(): Bir ondalıklı sayıyı en yakın tam sayıya veya virgülden sonra belirtilen basamak sayısına yuvarlar.

print(abs(-15.8)) # 15.8 (Pozitif çıktı verir)

sayilar = [10, 20, 30]
print(sum(sayilar)) # 60

pi = 3.14159
print(round(pi))    # 3 (En yakın tam sayı)
print(round(pi, 2)) # 3.14 (Virgülden sonra 2 basamak bırakır)