# 1. Basit Filtreleme: Belirli Bir Yazara Ait Kitapları Çekme

# Bu senaryoda, metinsel bir sütun üzerinde tam eşleşme kontrolü yapıyoruz. Veri setindeki tüm kitaplar arasından sadece "George R. R. Martin" tarafından yazılanları filtreleyelim.

import csv

yazar_kitaplari = []

with open("bestselling-books.csv", "r", encoding="utf-8") as file:
    okuyucu = csv.DictReader(file)
    
    for satir in okuyucu:
        # Metinsel karşılaştırma (büyük/küçük harf duyarlılığına dikkat edilmeli)
        if satir["Author"] == "George R. R. Martin":
            yazar_kitaplari.append({
                "Kitap": satir["Name"],
                "Yıl": satir["Year"],
                "Fiyat": satir["Price"]
            })

# Sonuçları Listeleme
print(f"--- George R. R. Martin Kitapları (Toplam: {len(yazar_kitaplari)}) ---")
for k in yazar_kitaplari:
    print(f"-> {k['Kitap']} ({k['Yıl']}) - {k['Fiyat']} USD")

# 2. Sayısal Filtreleme: Bedava veya Çok Ucuz Kitapları Bulma

# Veri analizinde fiyat, stok gibi sayısal kolonlarda büyüktür/küçüktür filtreleri çok sık kullanılır. Bu örnekte fiyatı 5 USD ve altında olan bütçe dostu kitapları buluyoruz.
# (Unutmayın: CSV'den gelen veriler string olduğu için sayısal filtreleme öncesi int() veya float() dönüşümü şarttır!)

import csv

ucuz_kitaplar = []

with open("bestselling-books.csv", "r", encoding="utf-8") as file:
    okuyucu = csv.DictReader(file)
    
    for satir in okuyucu:
        # Sayısal filtreleme için dönüşüm yapıyoruz
        kitap_fiyati = int(satir["Price"])
        
        if kitap_fiyati <= 5:
            ucuz_kitaplar.append({
                "Name": satir["Name"],
                "Price": kitap_fiyati,
                "Genre": satir["Genre"]
            })

print(f"--- Fiyatı 5 USD ve Altında Olan Kitaplar (Toplam: {len(ucuz_kitaplar)}) ---")
for k in ucuz_kitaplar[:5]: # Konsolu boğmamak için sadece ilk 5 tanesini gösterelim
    print(f"-> {k['Name']} | Fiyat: {k['Price']} USD | Tür: {k['Genre']}")

# list comprehension kullanarak tek adımda filtreleme ve sözlük oluşturma
with open("bestselling-books.csv", "r", encoding="utf-8") as file:
    okuyucu = csv.DictReader(file)
    
    # 🎯 List Comprehension ile tek adımda Sözlük Listesi oluşturma ve filtreleme:
    ucuz_kitaplar = [
        {
            "Name": satir["Name"],
            "Price": int(satir["Price"]),
            "Genre": satir["Genre"]
        }
        for satir in okuyucu
        if int(satir["Price"]) <= 5
    ]


# 3. Çoklu Koşul Filtrelemesi (and / or Kullanımı)

# Gerçek hayatta tek bir şart yetmez. Analiz ekibi bizden şunu isteyebilir: "Bize 2019 yılında çıkan VE türü 'Fiction' (Kurgu) olan kitapları getir." Burada iki şartın da aynı anda sağlanması için and operatörünü kullanacağız.

import csv

koşullu_liste = []

with open("bestselling-books.csv", "r", encoding="utf-8") as file:
    okuyucu = csv.DictReader(file)
    
    for satir in okuyucu:
        # ÇOKLU KOŞUL: Yıl 2019 olacak VE Türü Fiction olacak
        if satir["Year"] == "2019" and satir["Genre"] == "Fiction":
            koşullu_liste.append({
                "Name": satir["Name"],
                "Author": satir["Author"],
                "Rating": satir["User Rating"]
            })

print(f"--- 2019 Yılı Kurgu (Fiction) Kitapları (Toplam: {len(koşullu_liste)}) ---")
for k in koşullu_liste[:5]:
    print(f"-> {k['Name']} - Yazar: {k['Author']} (Puan: {k['Rating']})")

# 4. İleri Düzey Metinsel Filtreleme (İçinde Geçen Kelimeye Göre Arama)

import csv

arama_sonuclari = []
aranan_kelime = "harry potter"

with open("bestselling-books.csv", "r", encoding="utf-8") as file:
    okuyucu = csv.DictReader(file)
    
    for satir in okuyucu:
        kitap_adi = satir["Name"]
        
        # .lower() kullanarak büyük/küçük harf uyuşmazlığı riskini tamamen eliyoruz
        if aranan_kelime in kitap_adi.lower():
            arama_sonuclari.append({
                "Tam_Ad": kitap_adi,
                "Yil": satir["Year"],
                "Puan": satir["User Rating"]
            })

print(f"--- İçinde '{aranan_kelime.title()}' Geçen Kitaplar (Toplam: {len(arama_sonuclari)}) ---")
for k in arama_sonuclari:
    print(f"-> {k['Tam_Ad']} | Yayın Yılı: {k['Yil']} | Okuyucu Puanı: {k['Puan']}")