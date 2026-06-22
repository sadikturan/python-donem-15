import numpy as np

# SQL Sorgusu Sonucu Gelen Ham Veri 
sql_personel_tablosu = [
    {"id": 101, "ad": "Ahmet", "satis": 45, "memnuniyet": 8},
    {"id": 102, "ad": "Zeynep", "satis": 60, "memnuniyet": 9},
    {"id": 103, "ad": "Mehmet", "satis": 30, "memnuniyet": 6},
    {"id": 104, "ad": "Can",    "satis": 75, "memnuniyet": 9},
    {"id": 105, "ad": "Ayşe",   "satis": 50, "memnuniyet": 7}
]

# SQL'den sonradan çekilen ek personel verileri
sql_yeni_gelenler = [
    {"id": 106, "ad": "Ece",    "satis": 40, "memnuniyet": 8},
    {"id": 107, "ad": "Umut",   "satis": 85, "memnuniyet": 10}
]

# Köprü Kurma (SQL Verisini NumPy Matrisine Dönüştürme)
# NumPy metinsel verileri (isimleri) matematiksel matrislerin içinde sevmez (çünkü homojendir). Bu yüzden sadece sayısal analiz yapacağımız sütunları cımbızla çekip matrisleştirmeliyiz:

# List Comprehension ile sözlüklerin içindeki sayısal değerleri söküp listeye çeviriyoruz:
ana_matris_listesi = [[p["id"], p["satis"], p["memnuniyet"]] for p in sql_personel_tablosu]
personel_verisi = np.array(ana_matris_listesi)

yeni_matris_listesi = [[p["id"], p["satis"], p["memnuniyet"]] for p in sql_yeni_gelenler]
yeni_personeller = np.array(yeni_matris_listesi)

# Not: İsimleri ileride raporlama yaparken eşleştirmek için düz bir Python listesinde tutabiliriz:
isimler = [p["ad"] for p in sql_personel_tablosu] + [p["ad"] for p in sql_yeni_gelenler]


# Soru 1: Dizi Birleştirme ve Genel İstatistikler

# Yeni katılan personellerin verilerini (yeni_personeller), ana veri matrisine (personel_verisi) dikey olarak ekleyin (np.vstack) ve yeni oluşan matrisi tum_personel değişkenine atayarak ekrana basın.

tum_personel = np.vstack((personel_verisi, yeni_personeller))
print("--- Güncellenmiş Tüm Personel Matrisi ---")
print(tum_personel)

# Soru 2: Güncellenmiş tum_personel matrisindeki toplam satır ve sütun sayısını (şeklini) shape özelliğiyle kontrol edin. Şirkette toplam kaç personel olduğunu ekrana yazdırın.

satir_sayisi, sutun_sayisi = tum_personel.shape
print(f"\nMatris Şekli: {tum_personel.shape} | Toplam Personel Sayısı: {satir_sayisi}")

# Soru 3: Tüm personelin sadece Aylık Satış Adetlerini (1. indeksli sütun) dilimleme (slicing) yöntemiyle çekip ortalamasını (.mean()) hesaplayın.

# [:, 1] -> Tüm satırları seç, sadece 1. sütunu (Satış) al
satis_sutunu = tum_personel[:, 1]
satis_ortalamasi = satis_sutunu.mean()
print(f"\n Şirket İçi Aylık Ortalama Satış Adedi: {satis_ortalamasi:.2f}")

# Soru 4: Şirkette yapılan toplam satış adedini (.sum()) bulun.
toplam_satis = satis_sutunu.sum()
print(f" Tüm Personelin Yaptığı Toplam Satış: {toplam_satis} Adet")

# Soru 5 & 6: Şirketin satış rekorunu kıran personelin satış adet değerini ve bu rekoru kıran personelin matristeki satır indeksini .argmax() yardımıyla bulunuz. Bulduğunuz indeksle bu personelin ID numarasını ve Adını ekrana yazdırın.

en_yuksek_satis = satis_sutunu.max()
sampiyon_indeks = satis_sutunu.argmax() # En yüksek satışın satır numarasını verir

# Bulduğumuz satır numarasının 0. sütunundaki ID'yi çekiyoruz
sampiyon_id = tum_personel[sampiyon_indeks, 0]
sampiyon_adi = isimler[sampiyon_indeks]

print(f"\n Günün Satış Şampiyonu: {sampiyon_adi} (ID: {sampiyon_id})")
print(f"   Rekor Satış Adedi    : {en_yuksek_satis} Adet")

# Soru 7: Memnuniyet skoru (2. indeksli sütun) 8 ve 8'den yüksek (>= 8) olan başarılı personelleri tespit etmek için bir Boolean maskesi oluşturup verileri filtreleyin.

memnuniyet_sutunu = tum_personel[:, 2]

# True / False maskesi üretiyoruz
basari_maskesi = memnuniyet_sutunu >= 8
basarili_personeller = tum_personel[basari_maskesi]

print("\n Memnuniyet Skoru 8 ve Üzeri Olan Personel ID'leri:")
print(basarili_personeller[:, 0]) # Sadece ID sütununu basıyoruz

# Soru 8: Satış adedi 50'den büyük (> 50) olan personellerin sadece isimlerini ekrana listeleyin.

satis_maskesi = tum_personel[:, 1] > 50

print("\n 50'den Fazla Satış Yapan Personel İsimleri:")
# Oluşturduğumuz maskeyi isimler listesiyle eşleştirmek için np.array'e çevirip uygulayabiliriz
np_isimler = np.array(isimler)

print(satis_maskesi)
print(np_isimler)

print(np_isimler[satis_maskesi])

# Soru 9: Döngü kullanmadan, tüm personelin prim puanlarını şu formüle göre hesaplayıp tek boyutlu bir dizi olarak ekrana basın:
# Prim Puanı = (Satış Adedi * 1.5) + (Memnuniyet Skoru * 10)

# Sütunları tamamen ayırıp doğrudan vektörel çarpım yapıyoruz
satislari_al = tum_personel[:, 1]
skorlari_al = tum_personel[:, 2]

prim_puanlari = (satislari_al * 1.5) + (skorlari_al * 10)

print("\n💰 Personellerin Hesaplanan Prim Puanları Listesi:")
for isim, puan in zip(isimler, prim_puanlari):
    print(f"   - {isim:<7}: {puan:>6.1f} Puan")
