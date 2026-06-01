# Uygulama Örneği: Kurs Yönetim Sistemi

kurs = {
    "id": 102,
    "baslik": "Python ile Web Scrape Eğitimi",
    "konular": ["Değişkenler", "Veri Tipleri", "Sözlükler"],
    "aktif_mi": True,
    "ogrenci_sayisi": 120
}

# Öğrenci sayısı arttı, güncelleyelim
kurs["ogrenci_sayisi"] = kurs["ogrenci_sayisi"] + 1

# Kursa yeni bir konu eklendi (Sözlük içindeki listeye append yapıyoruz!)
kurs["konular"].append("Döngüler")

print(f"Kurs Adı: {kurs['baslik']}")
print(f"Güncel Öğrenci: {kurs['ogrenci_sayisi']}")
print(f"Müfredat: {kurs['konular']}")

# Uygulama Örneği: Futbol Takımı Yönetimi

# 1. BAŞLANGIÇ: İlk sözlük yapımızı kuruyoruz
takim = {
    "10": {"isim": "Arda Güler", "pozisyon": "Orta Saha", "gol": 5},
    "7":  {"isim": "Kerem Aktürkoğlu", "pozisyon": "Forvet", "gol": 12}
}

print("1. Başlangıç Kadrosu:")
print(takim)
print("-" * 40)


# 2. EKLEME İŞLEMİ (Create): Kullanıcıdan bilgileri alıp sözlüğe ekliyoruz
yeni_forma = input("Eklenecek Futbolcu Forma No: ")
yeni_isim = input("Futbolcu Adı: ")
yeni_pozisyon = input("Pozisyonu: ")
yeni_gol = int(input("Gol Sayısı: ")) # Sayıya çevirdik

# Yeni bir anahtar (Key) oluşturup iç sözlüğü değer (Value) olarak atıyoruz
takim[yeni_forma] = {
    "isim": yeni_isim,
    "pozisyon": yeni_pozisyon,
    "gol": yeni_gol
}

print("\n2. Oyuncu Eklendikten Sonraki Kadro:")
print(takim)
print("-" * 40)


# 3. GÜNCELLEME İŞLEMİ (Update): Mevcut bir oyuncunun gol sayısını değiştirelim
# Örneğin doğrudan 10 numaralı oyuncunun (Arda) golünü input ile güncelleyelim
guncel_gol = int(input("Arda Güler'in yeni gol sayısını girin: "))

# Sözlük içinde hedef adrese gidip değeri üzerine yazıyoruz
takim["10"]["gol"] = guncel_gol

print("\n3. Güncelleme Sonrası (Arda'nın Golü Değişti):")
print(takim["10"]) # Sadece Arda'nın bilgilerine baktık
print("-" * 40)


# 4. SİLME İŞLEMİ (Delete): Bir oyuncuyu takımdan çıkaralım
silinecek_forma = input("Takımdan silinecek oyuncunun forma numarasını girin (Örn: 7): ")

# .pop() metodu belirtilen anahtarı ve içindeki bilgileri tamamen siler
silinen_oyuncu = takim.pop(silinecek_forma)

print(f"\n4. Başarıyla Silinen Oyuncu: {silinen_oyuncu['isim']}")
print("Kalan Takım Kadrosu:")
print(takim)