# JSON Dosyasından Veri Okuma (json.load)

# Diskteki bir JSON dosyasını Python programının içine aldığımız an, o artık bir metin değil, doğrudan elemanlarına anahtarlarıyla erişebileceğimiz bir Python sözlüğüdür.

import json

try:
    with open("kitap_ozet.json", "r", encoding="utf-8") as file:
        # JSON'ı oku ve Python sözlüğüne (dict) çevir
        veri = json.load(file)
        
        # Artık standart bir dict gibi kullanabiliriz:
        print("--- JSON Dosyasından Okunanlar ---")
        print(f"Kitap Kategorisi: {veri['kategori']}")
        print(f"Kullanıcı Puanı : {veri['istatistik']['puan']}") # İç içe geçmiş veriye erişim
        print(f"İlk Etiket      : {veri['etiketler'][0]}")

except FileNotFoundError:
    print("HATA: Okunacak JSON dosyası bulunamadı.")

