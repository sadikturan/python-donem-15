"""
List Comprehensions (Tek Satırda Liste Oluşturma)
Normalde 3-4 satır süren for döngülerini ve liste ekleme (.append()) işlemlerini tek bir satırda yapmamızı sağlar. Kodun çok daha hızlı çalışmasını sağlar.
"""

# Normal Yöntem
squares = []
for i in range(10):
    squares.append(i**2)

# List Comprehension Yöntemi
squares = [i for i in range(10)]
squares = (i for i in range(10))    # generator

print(next(squares))
print(next(squares))

print("*" * 10)

for i in squares:
    print(i)

# Normal Yöntem
even_numbers = []   
for i in range(20):
    if i % 2 == 0:
        even_numbers.append(i)

# List Comprehension Yöntemi
even_numbers = [i for i in range(20) if i % 2 == 0]

# Normal Yöntem
fruits = ['apple', 'banana', 'cherry', 'date']
uppercase_fruits = []
for fruit in fruits:
    uppercase_fruits.append(fruit.upper())

# List Comprehension Yöntemi
uppercase_fruits = [fruit.upper() for fruit in fruits]

# Normal Yöntem
numbers = [1, 2, 3, 4, 5]
squared_even_numbers = []
for num in numbers:
    if num % 2 == 0:
        squared_even_numbers.append(num**2)

# List Comprehension Yöntemi
squared_even_numbers = [num**2 for num in numbers if num % 2 == 0]

# Normal Yöntem
sayilar = [1, 2, 3, 4, 5, 6]
durumlar = []

for i in sayilar:
    if i % 2 == 0:
        durumlar.append("Çift")
    else:
        durumlar.append("Tek")

print(durumlar)

# List Comprehension Yöntemi
# Formül: [ if Doğruysa | if Koşulu | else Yanlışsa | Döngü ]
durumlar = ["Çift" if i % 2 == 0 else "Tek" for i in sayilar]

"""
Uygulama: Maaş ve Performans Analizi
Öğrendiğimiz tüm bu metotları (range, enumerate, zip ve List Comprehensions) bir arada kullanan profesyonel bir veri analitiği senaryosu yazalım.

Senaryo: Elimizde çalışanların isimleri, mevcut maaşları ve yıl sonu performans puanları var. Performansı 80 ve üzeri olan kişilere %30 zam yapılacak, diğerlerine zam yapılmayacaktır.
"""

# Girdi Verileri
calisanlar = ["Aslı", "Berk", "Cem", "Deniz"]
maaslar = [30000, 45000, 35000, 50000]
performanslar = [85, 60, 90, 70] # 100 üzerinden puanlar

print("=== YIL SONU ZAM RAPORU ===")
print("-" * 35)

# 1. UYGULAMA: zip() ve enumerate() kullanımı
# Tüm listeleri paralel işleyip çalışanı numaralandırıyoruz
for sira, (isim, maas, skor) in enumerate(zip(calisanlar, maaslar, performanslar), start=1):
    
    if skor >= 80:
        yeni_maas = maas * 1.30
        durum = f"Tebrikler! %30 Zam Aldı -> Yeni Maaş: {yeni_maas:.2f} TL"
    else:
        yeni_maas = maas
        durum = "Zam Alamadı."
        
    print(f"{sira}. Personel: {isim} | Performans: {skor} | Durum: {durum}")

print("-" * 35)

# 2. UYGULAMA: List Comprehension kullanımı
# Sadece zam almaya hak kazanan (performansı >= 80 olan) çalışanların isimlerini filtreleyelim
odul_alacaklar = [isim for isim, skor in zip(calisanlar, performanslar) if skor >= 80]

print(f"Başarı Ödülü Alacak Personel Listesi: {odul_alacaklar}")


# 🎯 3. UYGULAMA: List Comprehension (Zam Alamayanlar)
# Performansı 80'den KÜÇÜK olanların isimlerini filtreliyoruz
zam_durumlari = [f"{isim}: Zam Aldı" if skor >= 80 else f"{isim}: Zam Alamadı" for isim, skor in enumerate(zip(calisanlar, performanslar))]
