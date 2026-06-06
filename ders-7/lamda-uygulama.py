# Veri tabanından gelen ham sepet verileri
sepet_analizi = [
    {"urun": "Telefon", "fiyat": 25000, "iptal_edildi_mi": False},
    {"urun": "Kılıf", "fiyat": -450, "iptal_edildi_mi": False}, # Hatalı negatif veri
    {"urun": "Şarj Aleti", "fiyat": 800, "iptal_edildi_mi": True}, # İptal edilmiş işlem
    {"urun": "Kulaklık", "fiyat": 3500, "iptal_edildi_mi": False},
    {"urun": "Ekran Koruyucu", "fiyat": 150, "iptal_edildi_mi": False}
]

# 1. ADIM: hatalı fiyatları ve iptal edilen ürünleri ayıklayalım (Temizleme)

# filter yapısının geleneksel for döngüsü karşılığı:
temiz_sepet = []

# filter() fonksiyonu işte bu döngüyü arka planda otomatik kurar:
for x in sepet_analizi: # Elemanlar TEK TEK 'x' değişkenine yüklenir
    
    # Lambda içindeki koşul kontrol edilir:
    if x["fiyat"] > 0 and not x["iptal_edildi_mi"]:
        temiz_sepet.append(x) # Sadece True çıkanlar yeni listeye alınır

print(f"\nTemizlenmiş Ürün Sayısı: {len(temiz_sepet)}")


temiz_sepet = list(filter(lambda x: x["fiyat"] > 0 and not x["iptal_edildi_mi"], sepet_analizi))
print(f"\nTemizlenmiş Ürün Sayısı: {len(temiz_sepet)}")

# 2. ADIM: map() ile sadece fiyatları içeren ayrı bir sayı listesi çıkaralım
sadece_fiyatlar = list(map(lambda x: x["fiyat"], temiz_sepet)) # [25000, 3500, 150]

# 3. ADIM: sum() ve round() kullanarak toplam ciro ve ortalama sepet tutarını bulalım
toplam_hasilat = sum(sadece_fiyatlar)
ortalama_tutar = round(toplam_hasilat / len(sadece_fiyatlar), 2)

print(f"Toplam Hasılat: {toplam_hasilat} TL")
print(f"Ortalama Sepet Tutarı: {ortalama_tutar} TL")

# 4. ADIM: max() ve min() ile en pahalı ve en ucuz temiz ürünleri bulalım
en_pahali_urun = max(temiz_sepet, key=lambda x: x["fiyat"])
print(f"En Pahalı Alışveriş: {en_pahali_urun['urun']} ({en_pahali_urun['fiyat']} TL)")

# 5. ADIM: any() ile sepetlerin içinde lüks harcama (Örn: 10.000 TL üzeri) var mı kontrol edelim
luks_harcama_var_mi = any(fiyat > 10000 for fiyat in sadece_fiyatlar)
print(f"Bu süreçte 10.000 TL üzeri harcama yapıldı mı?: {luks_harcama_var_mi}")