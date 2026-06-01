""" Dictionaries (dict): verileri Anahtar-Değer (Key-Value) çiftleri halinde saklamamızı sağlar.

Bir sözlüğü düşünün: Kelimeyi ararsınız (Anahtar) ve karşısında açıklamasını (Değer) bulursunuz. 
Bir telefon rehberini düşünün: Kişinin ismi "anahtar", telefon numarası ise "değer"dir.

Listelerde elemanlara 0, 1, 2 gibi indeks numaralarıyla ulaşırken, sözlüklerde elemanlara kendi belirlediğimiz anahtarlar ile ulaşırız.

** JSON veri yapısından dolayı web de hayati önem taşır.

"""

# 1. Sözlük Tanımlama

# 41 => Kocaeli
# 34 => İstanbul

sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])

# print(plakalar[sehirler.index('istanbul')])   # istanbul' un plaka kodu nedir?
# print(plakalar[sehirler.index('kocaeli')])    # kocaeli' nin plaka kodu nedir?

plakalar = {'kocaeli': 41,'istanbul':34}

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# Basit bir sözlük tanımlama (Telefon Rehberi)
rehber = {
    "Ahmet": "0555-111-2233",
    "Zeynep": "0555-222-4455",
    "Burak": "0555-333-6677"
}

# Bir ürünün detaylı bilgilerini tutan sözlük
urun = {
    "ad": "Kablosuz Kulaklık",
    "fiyat": 1500,
    "stok": 30,
    "indirimde_mi": True
}

# 2. Sözlük Elemanlarına Erişme

kullanici = {
    "kullanici_adi": "python_can",
    "eposta": "python@mail.com",
    "rol": "Admin"
}

# Eposta bilgisine ulaşalım
print(kullanici["eposta"])  # Çıktı: python@mail.com

# Rol bilgisine ulaşalım
print(kullanici["rol"])     # Çıktı: Admin

print(kullanici.get("yas")) # Çıktı: None => Güvenli Erişim: anahtar "KeyError" yerine None (Boş) döner:

# 3. Eleman Ekleme, Güncelleme ve Silme

ogrenci = {
    "isim": "Can",
    "notu": 85
}

# Değer Güncelleme (Notu değiştirelim)
ogrenci["notu"] = 95

# Yeni Eleman Ekleme (Sözlükte olmayan bir anahtar yazılır)
ogrenci["okul"] = "Atatürk Lisesi"

# Eleman Silme (pop metodu ile)
ogrenci.pop("isim")

print(ogrenci) # Çıktı: {'notu': 95, 'okul': 'Atatürk Lisesi'}


# 4- Nesned Listeler

ogrenciler = { 
    100: {
        "ad": "Çınar",
        "soyad": "Turan",
        "yas": 4,
        "notlar": [70,80,70]
    }, 
    101: {
        "ad": "Ada",
        "soyad": "Bilgi",
        "yas": 10
    } 
}

sonuc = ogrenciler[100]
sonuc = ogrenciler[101]["ad"]
sonuc = ogrenciler[101]["soyad"]

sonuc = (ogrenciler[100]["notlar"][0] + ogrenciler[100]["notlar"][1] + ogrenciler[100]["notlar"][2]) / 3

print(sonuc)