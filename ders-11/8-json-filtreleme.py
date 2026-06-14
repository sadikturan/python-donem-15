import json

# Simüle edilmiş bir JSON veri tabanı dizesi (List of Dicts)
kitaplar_havuzu = [
    {"isim": "Wonder", "aktif_satis": True, "fiyat": 9},
    {"isim": "1984", "aktif_satis": False, "fiyat": 6},
    {"isim": "11/22/63", "aktif_satis": True, "fiyat": 22}
]

# Adım A: Önce bu veriyi bir JSON dosyasına kaydedelim
with open("magaza.json", "w", encoding="utf-8") as f:
    json.dump(kitaplar_havuzu, f, indent=4)

# Adım B: Şimdi dosyadan okuyup filtreleme uygulayalım
aktif_kitaplar = []

with open("magaza.json", "r", encoding="utf-8") as f:
    veriler = json.load(f) # 'veriler' artık bir listedir
    
    for kitap in veriler:
        # Boolean filtreleme yapıyoruz
        if kitap["aktif_satis"] == True:
            aktif_kitaplar.append(kitap["isim"])

print(f"Şu an aktif satışta olan kitaplar: {aktif_kitaplar}")
# Çıktı: ['Wonder', '11/22/63']