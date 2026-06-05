# 1. range() Fonksiyonu

# r = range(10)
# r = range(5,10)
# r = range(50,100,10)
# r = range(0,-10,-2)
# sonuc = list(r)
# print(sonuc)

# 1'den 10'a kadar (10 hariç) 2'şer 2'şer sayalım
for i in range(1, 10, 2):
    print(f"Sayı: {i}") # Çıktı: 1, 3, 5, 7, 9

"""
Diyelim ki 0'dan 1 milyona kadar olan sayıları kullanmanız gerekiyor.

Eğer list(range(1000000)) yaparsanız: Bilgisayar anında RAM (hafıza) üzerinde 1 milyon tane sayılık devasa bir yer ayırır ve bilgisayarı yormaya başlar.

Eğer for i in range(1000000): yaparsanız: Bilgisayar hafızasında sadece 3 tane sayı tutar: "Başlangıç: 0, Bitiş: 1.000.000, Adım: 1". Döngü her döndüğünde sayıları sırayla üretip tükettiği için RAM'de neredeyse sıfır yer kaplar.
"""

# 2. enumerate() Fonksiyonu: Bir iterable (örneğin, liste) üzerinde dönerken, her bir öğenin indeksini de verir.
meyveler = ["Elma", "Armut", "Muz", "Çilek"]
for index, meyve in enumerate(meyveler):
    print(f"{index}: {meyve}") # Çıktı: 0: Elma, 1: Armut, 2: Muz, 3: Çilek

for index, meyve in enumerate(meyveler, start=1):
    print(f"{index}: {meyve}") # Çıktı: 1: Elma, 2: Armut, 3: Muz, 4: Çilek

print(list(enumerate(meyveler))) # Çıktı: [(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Çilek')]

# 3. zip() Fonksiyonu: Birden fazla iterable'ı aynı anda dönerken, her bir öğeyi birleştirir.
isimler = ["Ali", "Ayşe", "Mehmet"]
yaslar = [25, 30, 35]

print(list(zip(isimler, yaslar))) # Çıktı: [('Ali', 25), ('Ayşe', 30), ('Mehmet', 35)]

for isim, yas in zip(isimler, yaslar):
    print(f"{isim} {yas} yaşında") # Çıktı: Ali 25 yaşında, Ayşe 30 yaşında, Mehmet 35 yaşında

# 4. reversed() Fonksiyonu: Bir iterable'ı tersine çevirir.
sayilar = [1, 2, 3, 4, 5]
for sayi in reversed(sayilar):
    print(f"Sayı: {sayi}") # Çıktı: 5, 4, 3, 2, 1

# 5. sorted() Fonksiyonu: Bir iterable'ı sıralar.

karakterler = ["Zorro", "Batman", "Superman", "Spiderman"]
for karakter in sorted(karakterler):
    print(f"Karakter: {karakter}") # Çıktı: Batman, Spiderman, Superman, Zorro


sayilar = [0, 5, 2, 9, 1]

sonuc = list(sorted(sayilar))
sonuc = list(reversed(sonuc))   # sorted() ile sıraladıktan sonra reversed() ile tersine çevirerek büyükten küçüğe sıralama yapabiliriz.
print(sonuc) # Çıktı: [9, 5, 2, 1, 0]


# Senaryo: Elimizde e-ticaret sitemize ait 3 farklı liste olsun. Bu listeleri zip() ile birleştirip tek bir döngüde analiz edelim ve en sonunda bunları hızlıca bir Python sözlüğüne dönüştürelim.

print("====== E-TİCARET ÜRÜN VE STOK ANALİZİ ======\n")

urunler  = ["Laptop", "Telefon", "Kulaklık"]
fiyatlar = [35000, 22000, 1500]
stoklar  = [12, 45, 0] # Kulaklık stoğu bitmiş

# 1. ADIM: 3 farklı listeyi tek bir döngüde paralel olarak süzüyoruz
for urun, fiyat, stok in zip(urunler, fiyatlar, stoklar):
    print("Ürün:", urun, "| Fiyat:", fiyat, "TL")
    
    # Döngü içinde if-else analizi
    if stok == 0:
        print("KRİTİK UYARI: Bu ürünün stoğu tükenmiştir!")
    else:
        print("Stok Durumu: Güvenli (", stok, "adet )")
    print("-" * 45)


# 2. ADIM: Ürün ve Fiyat listesini anında bir Sözlüğe (Dictionary) dönüştürme
# Veri biliminde iki farklı seriyi Key-Value (Anahtar-Değer) yapmak için bu yöntem harikadır.
urun_fiyat_sozlugu = dict(zip(urunler, fiyatlar))

print("\n Oluşturulan Ürün Fiyat Kataloğu (Sözlük):")
print(urun_fiyat_sozlugu)

