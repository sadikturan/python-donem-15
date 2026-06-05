"""
Python'da Döngüler (Loops), belirli bir kod bloğunun tekrar tekrar çalıştırılmasını sağlayan yapılardır. Örneğin, ekrana 100 defa "Merhaba" yazdırmak, bir listedeki 500 ürünün fiyatını tek tek güncellemek veya bir web sitesindeki tüm verileri çekmek (Web Crawling) için döngüleri kullanırız.

Döngüler olmasaydı, aynı kodu yüzlerce kez kopyalayıp yapıştırmak zorunda kalırdık. Python'da iki temel döngü yapısı vardır: for döngüsü ve while döngüsü.

"""

# For Döngüsü
# For döngüsü, belirli bir koleksiyonun (liste, dizi, string vb.) her bir elemanını sırayla işlemek için kullanılır.
# Örnek: Bir liste içindeki sayıları ekrana yazdırma

sayilar = [1, 2, 3, 4, 5]

for sayi in sayilar:
    print(sayi)

meyveler = ["Elma", "Armut", "Muz", "Çilek"]

for meyve in meyveler:
    print(f"Manavdaki Ürün: {meyve}")

kurs_adi = "Python"

for harf in kurs_adi:
    print(harf.upper()) # Her harfi büyük yaparak alt alta yazar

#Uygulama: Bir listede bulunan sayılardan çift olanları ekrana yazdırın.

sayilar = [1, 2, 3, 4, 5, 6]

print("--- Çift Sayılar Kontrolü ---")
for sayi in sayilar:
    if sayi % 2 == 0:
        print(f"{sayi} bir ÇİFT sayıdır.")
    else:
        print(f"{sayi} bir TEK sayıdır.")


# Uygulama: Bir listede bulunan ürün adlarında 'iphone' geçen ürünleri ekrana yazdırın.

urunler = ['iphone 8','iphone 7','iphone X','iphone XR','samsung S10']

print("--- Ürün Adlarında 'iphone' Geçiyor mu? ---")
for urun in urunler:
    if 'iphone' in urun:
        print(f"{urun} bir iPhone modelidir.")
    else:
        print(f"{urun} bir iPhone modeli değildir.")


# Uygulama: urunler listesinde içinde 'iphone' geçen kaç ürün vardır? (index,find)

print("--- 'iphone' İçeren Ürün Sayısı ---")
iphone_sayisi = 0
for urun in urunler:
    if 'iphone' in urun:
        iphone_sayisi += 1
print(f"'iphone' içeren ürün sayısı: {iphone_sayisi}")










