satis_verisi: list[dict] = [
    {"id": 1, "kategori": "Elektronik", "urun": "Kablosuz Kulaklık", "adet": 2, "fiyat": 1200, "musteri": "Premium"},
    {"id": 2, "kategori": "Moda", "urun": "Kışlık Mont", "adet": 1, "fiyat": 3500, "musteri": "Standart"},
    {"id": 3, "kategori": "Ev & Yaşam", "urun": "Kahve Makinesi", "adet": 1, "fiyat": 4500, "musteri": "Premium"},
    {"id": 4, "kategori": "Elektronik", "urun": "Akıllı Saat", "adet": 3, "fiyat": 2500, "musteri": "Standart"},
    {"id": 5, "kategori": "Moda", "urun": "Spor Ayakkabı", "adet": 2, "fiyat": 1800, "musteri": "Premium"},
    {"id": 6, "kategori": "Ev & Yaşam", "urun": "Nevresim Takımı", "adet": 1, "fiyat": 950, "musteri": "Standart"},
    {"id": 7, "kategori": "Kitap", "urun": "Yazılım Bilimi Tarihi", "adet": 5, "fiyat": 150, "musteri": "Premium"},
    {"id": 8, "kategori": "Elektronik", "urun": "Bluetooth Hoparlör", "adet": 1, "fiyat": 850, "musteri": "Standart"},
    {"id": 9, "kategori": "Moda", "urun": "Deri Ceket", "adet": 1, "fiyat": 5000, "musteri": "Premium"},
    {"id": 10, "kategori": "Ev & Yaşam", "urun": "Dikey Süpürge", "adet": 1, "fiyat": 8900, "musteri": "Premium"},
    {"id": 11, "kategori": "Kitap", "urun": "Python ile Veri Analizi", "adet": 3, "fiyat": 220, "musteri": "Standart"},
    {"id": 12, "kategori": "Elektronik", "urun": "Oyuncu Mouse", "adet": 2, "fiyat": 650, "premium": "Premium"}, 
    {"id": 13, "kategori": "Moda", "urun": "Sırt Çantası", "adet": 1, "fiyat": 450, "musteri": "Standart"},
    {"id": 14, "kategori": "Ev & Yaşam", "urun": "Çelik Tencere Seti", "adet": 1, "fiyat": 2300, "musteri": "Standart"},
    {"id": 15, "kategori": "Kitap", "urun": "Algoritmalar 101", "adet": 2, "fiyat": 180, "musteri": "Premium"},
    {"id": 16, "kategori": "Elektronik", "urun": "27' Oyuncu Monitörü", "adet": 1, "fiyat": 7200, "musteri": "Premium"},
    {"id": 17, "kategori": "Moda", "urun": "Güneş Gözlüğü", "adet": 1, "fiyat": 1200, "musteri": "Standart"},
    {"id": 18, "kategori": "Ev & Yaşam", "urun": "Hava Temizleyici", "adet": 1, "fiyat": 5400, "musteri": "Premium"},
    {"id": 19, "kategori": "Kitap", "urun": "Yapay Zeka Felsefesi", "adet": 1, "fiyat": 200, "musteri": "Standart"},
    {"id": 20, "kategori": "Elektronik", "urun": "Mekanik Klavye", "adet": 2, "fiyat": 1100, "musteri": "Standart"},
    {"id": 21, "kategori": "Moda", "urun": "Klasik Takım Elbise", "adet": 1, "fiyat": 6000, "musteri": "Premium"},
    {"id": 22, "kategori": "Ev & Yaşam", "urun": "Akıllı Ampul", "adet": 4, "fiyat": 350, "musteri": "Standart"},
    {"id": 23, "kategori": "Kitap", "urun": "İstatistik Mantığı", "adet": 1, "fiyat": 250, "musteri": "Premium"},
    {"id": 24, "kategori": "Elektronik", "urun": "USB-C Çoklayıcı", "adet": 3, "fiyat": 400, "musteri": "Standart"},
    {"id": 25, "kategori": "Moda", "urun": "Pamuklu Tişört", "adet": 5, "fiyat": 300, "musteri": "Premium"}
]

# Soru 1: Toplam Ciro ve Toplam Satılan Ürün Adedini Bulma
# Her işlemin cirosu (adet * fiyat) formülüyle bulunur. List Comprehension ve sum() kullanarak mağazanın toplam ciro ve satılan toplam ürün adedini hesaplayınız.
# Cevap:

# toplam_ciro = 0
# toplam_adet = 0

# for veri in satis_verisi:
#     toplam_ciro += veri["adet"] * veri["fiyat"]
#     toplam_adet += veri["adet"]

toplam_ciro = sum([urun["adet"] * urun["fiyat"] for urun in satis_verisi])
toplam_adet = sum([urun["adet"] for urun in satis_verisi])

print(f"Toplam Ciro: {toplam_ciro} TL") # 69570 TL
print(f"Toplam Satılan Ürün Adedi: {toplam_adet} adet") # 47 adet


# Soru 2: En Çok Ürün Satın Alan Müşteri Tipini Bulma 
# Pazarlama ekibi için Premium müşterilerin mi toplamda daha fazla adet ürün satın aldığını, yoksa Standart müşterilerin mi daha fazla aldığını sum() yardımıyla adet bazında karşılaştırınız.
# Cevap:

premium_toplam_adet = 0
standart_toplam_adet = 0

for satis in satis_verisi:
    #satis["musteri"] musteri key i 1 kayıtta olmadığından KeyError gelir. get() kullan güvenli.
    if satis.get("musteri") == "Premium":   
        premium_toplam_adet += satis["adet"]
    elif satis.get("musteri") == "Standart":
        standart_toplam_adet += satis["adet"]

premium_toplam_adet = sum([satis.get("adet") for satis in satis_verisi if satis.get("musteri") == "Premium"])
standart_toplam_adet = sum([satis.get("adet") for satis in satis_verisi if satis.get("musteri") == "Standart"])

if premium_toplam_adet > standart_toplam_adet:
    print(f"Premium müşteriler toplamda daha fazla ürün satın aldı: {premium_toplam_adet} adet")
else:
    print(f"Standart müşteriler toplamda daha fazla ürün satın aldı: {standart_toplam_adet} adet")


# Soru 3: En Ucuz Tekil Ürünü Bulma (min)
# Mağazanın en düşük birim fiyatlı (adet gözetmeksizin, sadece 'fiyat' özelliğine göre) ürününün hangisi olduğunu ve hangi kategoride yer aldığını min() fonksiyonu ve lambda ile bulunuz.
# Cevap:

en_ucuz_urun = satis_verisi[0]

for satis in satis_verisi:
    if satis["fiyat"] < en_ucuz_urun["fiyat"]:
        en_ucuz_urun = satis


en_ucuz_urun = min(satis_verisi, key=lambda s: s["fiyat"])

print(f"En Ucuz Ürün: {en_ucuz_urun['urun']}, Kategori: {en_ucuz_urun['kategori']}, Fiyat: {en_ucuz_urun['fiyat']} TL")


# Soru 4: En Yüksek Ciro Yapan Tekil Satışı Bulma (max)
# Gün içinde tek seferde en büyük ciroyu (adet * fiyat) bırakan faturayı ve ürünü max() fonksiyonu ve lambda yardımıyla filtreleyiniz.
# Cevap:

en_yuksek_ciro_satis = satis_verisi[0]

for satis in satis_verisi:
    if en_yuksek_ciro_satis["adet"] * en_yuksek_ciro_satis["fiyat"] < satis["adet"] * satis["fiyat"]:
        en_yuksek_ciro_satis = satis

en_yuksek_ciro = en_yuksek_ciro_satis["adet"] * en_yuksek_ciro_satis["fiyat"]


en_yuksek_ciro_satis = max(satis_verisi, key=lambda s: s["adet"] * s["fiyat"])
en_yuksek_ciro = en_yuksek_ciro_satis["adet"] * en_yuksek_ciro_satis["fiyat"]

print(f"En Yüksek Ciro Yapan Satış: {en_yuksek_ciro_satis['urun']}, Ciro: {en_yuksek_ciro} TL")


# Soru 5: Ürünleri Kazandırdığı Ciroya Göre Küçükten Büyüğe Sıralama (sorted)
# Gün sonu raporunda listelenmek üzere, tüm satış işlemlerini kazandırdığı ciroya göre küçükten büyüğe doğru sıralanmış yeni bir liste haline sorted() ve lambda kullanarak getiriniz.
# Cevap:
ciroya_gore_sirali = sorted(satis_verisi, key=lambda x: x["adet"] * x["fiyat"])

print("Satışlar Ciroya Göre Küçükten Büyüğe Sıralanmış:")

for satis in ciroya_gore_sirali:
    ciro = satis["adet"] * satis["fiyat"]
    print(f"Ürün: {satis['urun']}, Ciro: {ciro} TL")

    
# Soru 6: Yüksek Değerli Satışları Ayıklama (filter)
# Cirosu (adet * fiyat) tek seferde 5.000 TL ve üzerinde olan "büyük satışları" filter() ve lambda mimarisini kullanarak ayıklayıp listeleyiniz.
# Cevap:
buyuk_satislar = list(filter(lambda s: s["adet"] * s["fiyat"] >= 5000, satis_verisi))
print("Cirosu 5.000 TL ve Üzeri Olan Satışlar:")

for satis in buyuk_satislar:
    ciro = satis["adet"] * satis["fiyat"]
    print(f"Ürün: {satis['urun']}, Ciro: {ciro} TL")


# Soru 7: Kitap Kategorisindeki Ortalama Sepet Tutarını Bulma
# Kitap satışlarının performansını ölçmek için filter() ve map() (veya list comprehension) kullanarak sadece "Kitap" kategorisindeki satışların cirolarını ayıklayın ve bu kategorinin ortalama satış tutarını hesaplayınız.
# Cevap:

kitap_satislari = list(filter(lambda s: s["kategori"] == "Kitap", satis_verisi))
kitap_cirolari = list(map(lambda s: s["adet"] * s["fiyat"], kitap_satislari))

ortalama_kitap_tutari = sum(kitap_cirolari) / len(kitap_cirolari) if kitap_cirolari else 0
print(f"Kitap Kategorisindeki Ortalama Sepet Tutarı: {ortalama_kitap_tutari:.2f} TL")   


# Soru 8: Müşteri Segmentasyonu Doğrulama Analizi (map & all/any)
# Premium müşterilerin harcamalarını analiz ediniz. Mağazadaki tüm Premium müşterilerin tek seferde en az 1000 TL ve üzerinde harcama yapıp yapmadığını all() veya any() ile kontrol ediniz.
# Cevap:

# Sadece Premium müşterileri ayıklıyoruz
premium_satislar = [s for s in satis_verisi if s["musteri"] == "Premium"]

# Premiumların harcamalarının hepsi 1000 TL'den büyük mü?
hepsi_yuksek_mi = all(map(lambda x: (x["adet"] * x["fiyat"]) >= 1000, premium_satislar))

print(f"\n Tüm Premium harcamalar 1.000 TL üzerinde mi?: {'Evet' if hepsi_yuksek_mi else 'Hayır'}")


# Soru 9: Müşteri Tipi ve Kategoriye Göre Pivot Analizi
# Çift filtreleme mantığı kullanarak, hem "Premium" müşteri tipi olan hem de "Elektronik" kategorisinden yapılan alışverişlerin kümülatif toplam cirosunu bulunuz.
# Cevap:

premium_elektronik_cirosu = sum(s["adet"] * s["fiyat"] for s in satis_verisi 
                                if s["musteri"] == "Premium" and s["kategori"] == "Elektronik")

print(f"Premium Üyelerin Elektronik Kategorisindeki Toplam Cirosu: {premium_elektronik_cirosu:,.2f} TL")
# Çıktı: 10,900.00 TL


# Soru 10: Kategori Bazlı Kümülatif Ciro Dağılımı (Sözlük Optimizasyonu)
# Döngü ve sözlük (dict) metotlarını (.get(), items()) harmanlayarak, hangi kategoriden toplamda ne kadar ciro kazanıldığını gösteren dinamik bir özet tablo (sözlük) üretiniz.
# Cevap:

kategori_ciro = {}

for satis in satis_verisi:
    ciro = satis["adet"] * satis["fiyat"]
    kategori_ciro[satis["kategori"]] = kategori_ciro.get(satis["kategori"], 0) + ciro

print("\n📊 Kategori Bazlı Kümülatif Ciro Dağılımı:")

for kategori, ciro in kategori_ciro.items():
    print(f"{kategori}: {ciro:,.2f} TL")

# 2. yol
# kategori_ciro = {
#     kat: sum(s["adet"] * s["fiyat"] for s in satis_verisi if s["kategori"] == kat) 
#     for kat in set(s["kategori"] for s in satis_verisi)
# }

# print(kategori_ciro)