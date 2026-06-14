# CSV Dosyasına Veri Yazma Yöntemleri

# Yeni veri üretirken veya analiz sonuçlarını kaydederken with open(..., 'w') kalıbını kullanırız. Windows'ta satır aralarında boşluk kalmaması için mutlaka newline="" parametresi eklenmelidir.

# A) Liste Olarak Yazma (csv.writer)
# Verileri listeler halinde satır satır dizeye döker. Tek satır için .writerow(), çoklu satır için .writerows() kullanılır.

import csv
veriler = [
    ["Ürün", "Kategori", "Fiyat"],
    ["Mouse", "Elektronik", 450],
    ["Klavye", "Elektronik", 1200]
]
with open("urunler.csv", "w", encoding="utf-8", newline="") as file:
    yazar = csv.writer(file)
    yazar.writerows(veriler)

# B) Sözlük Olarak Yazma (csv.DictWriter)
# Elimizde sözlüklerden oluşan bir veri seti varsa, bunu CSV'ye aktarmak için kullanılır. Alan isimlerini (fieldnames) önceden belirtmek ve ilk başta .writeheader() metoduyla başlıkları yazdırmak zorunludur.

import csv
alanlar = ["urun_adi", "stok"]
kullanicilar = [
    {"urun_adi": "Laptop", "stok": 15},
    {"urun_adi": "Monitör", "stok": 8}
]
with open("stoklar.csv", "w", encoding="utf-8", newline="") as file:
    yazar = csv.DictWriter(file, fieldnames=alanlar)
    yazar.writeheader() # Sütun isimlerini yazar
    yazar.writerows(kullanicilar)

