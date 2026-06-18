import json 
import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

urun_listesi = []

arama_sonuclari = soup.find(class_="searchResults")

if arama_sonuclari:
    urunler = arama_sonuclari.find_all("a")

    for urun in urunler:
        text_alani = urun.find(class_="product-text-area")
        urun_adi = text_alani.h2.string if text_alani and text_alani.h2 else "Ürün Adı Bulunamadı"

        sepet_alani = urun.find(class_="basket-price")
        
        if sepet_alani:
            fiyat_alani = sepet_alani.find(class_="price-area")
            urun_fiyat = fiyat_alani.h3.string if fiyat_alani and fiyat_alani.h3 else "Fiyat Bulunamadı"
        else:
            urun_fiyat = "Fiyat Alanı Yok"

        urun_listesi.append({
            "urun_adi": urun_adi.strip() if urun_adi else urun_adi,
            "fiyat": urun_fiyat.strip() if urun_fiyat else urun_fiyat
        })

#  2. ADIM: Verileri temiz bir JSON dosyasına aktarma operasyonu
# "w" parametresi yazma (write) modunu temsil eder.
with open("n11_urunler.json", "w", encoding="utf-8") as json_dosyası:
    # json.dump() fonksiyonu Python listesini alıp diske fiziksel dosya olarak yazar
    json.dump(urun_listesi, json_dosyası, ensure_ascii=False, indent=4)

print("🎉 Kazıma işlemi tamamlandı! Tüm veriler 'n11_urunler.json' dosyasına kaydedildi.")