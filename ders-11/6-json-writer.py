# JSON Dosyasına Veri Yazma (json.dump)

import json

# Python Sözlük Yapısı (Dict)
kitap_detay = {
    "trend_mi": True,
    "kategori": "Fiction",
    "istatistik": {
        "toplam_inceleme": 21625,
        "puan": 4.8
    },
    "etiketler": ["Bestseller", "Edebiyat", "Palacio"]
}

# Veriyi JSON dosyasına yazma
with open("kitap_ozet.json", "w", encoding="utf-8") as file:
    json.dump(kitap_detay, file, indent=4, ensure_ascii=False)

print("Sözlük yapısı başarıyla JSON dosyasına dönüştürüldü.")

# indent=4: Veriyi tek satıra sıkıştırmak yerine 4 karakter girintili (Pretty Print) yazarak insan gözünün okuyabileceği harika bir düzene sokar.

# ensure_ascii=False: Türkçe karakterlerin (ş, ç, ğ, ı vb.) bozulmasını engeller.

