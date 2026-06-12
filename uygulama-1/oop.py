ham_stok_verisi: list[dict] = [
    {"id": 1, "urun": "Laptop", "kategori": "Bilgisayar", "stok": 15, "fiyat": 35000, "garanti_yili": 2},
    {"id": 2, "urun": "Akıllı Telefon", "kategori": "Mobil", "stok": 40, "fiyat": 22000, "garanti_yili": 2},
    {"id": 3, "urun": "Oyuncu Mouse", "kategori": "Aksesuar", "stok": 120, "fiyat": 1200, "garanti_yili": 1},
    {"id": 4, "urun": "Mekanik Klavye", "kategori": "Aksesuar", "stok": 85, "fiyat": 2500, "garanti_yili": 2},
    {"id": 5, "urun": "27' Monitör", "kategori": "Ekran", "stok": 8, "fiyat": 8500, "garanti_yili": 3},
    {"id": 6, "urun": "Kablosuz Kulaklık", "kategori": "Ses", "stok": 65, "fiyat": 1800, "garanti_yili": 1},
    {"id": 7, "urun": "Bluetooth Hoparlör", "kategori": "Ses", "stok": 0, "fiyat": 3200, "garanti_yili": 2}, 
    {"id": 8, "urun": "Grafik Tablet", "kategori": "Bilgisayar", "stok": 12, "fiyat": 6400, "garanti_yili": 2},
    {"id": 9, "urun": "Type-C Çoklayıcı", "kategori": "Aksesuar", "stok": 200, "fiyat": 450, "garanti_yili": 1},
    {"id": 10, "urun": "Akıllı Saat", "kategori": "Mobil", "stok": 25, "fiyat": 7500, "garanti_yili": 3}
]

class Urun:
    def __init__(self, urun_id: int, urun_adi: str, kategori: str, stok: int, fiyat: float | int, garanti: int):
        self.id = urun_id
        self.ad = urun_adi
        self.kategori = kategori
        self.stok = stok
        self.fiyat = fiyat
        self.garanti = garanti

    def toplam_stok_degeri(self) -> float | int:
        """Ürünün depodaki toplam parasal değerini hesaplar (Maliyet/Varlık Analizi)."""
        return self.stok * self.fiyat

    def stok_durumu_kontrol(self) -> str:
        """Lojistik ekipleri için kritik stok uyarı mesajı üretir."""
        if self.stok == 0:
            return "❌ TÜKENDİ (Acil Tedarik!)"
        elif self.stok < 10:
            return f"⚠️ KRİTİK SEVİYE (Kalan: {self.stok})"
        else:
            return f"✔️ Güvenli (Stok: {self.stok})"

    def indirim_uygula(self, indirim_orani: int) -> float:
        """Kampanya dönemlerinde ürünün indirimli yeni fiyatını hesaplar."""
        fiyat_dususu = self.fiyat * (indirim_orani / 100)
        return self.fiyat - fiyat_dususu

    def rapor_satiri(self) -> str:
        """Veri analisti için ürünü tek satırda şık bir şekilde özetler."""
        return f"ID: {self.id:<2} | [{self.kategori:<10}] {self.ad:<18} | Fiyat: {self.fiyat:>6} TL | Durum: {self.stok_durumu_kontrol()}"
    

# 1. Adım: Nesneleri dolduracağımız boş bir liste oluşturuyoruz
stok_listesi: list[Urun] = []

# 2. Adım: Ham sözlük listesi üzerinde for döngüsü başlatıyoruz
for u in ham_stok_verisi:
    # 3. Adım: Her bir sözlükteki (u) verileri sökerek yeni bir Urun nesnesi (instance) üretiyoruz
    yeni_urun_nesnesi = Urun(
        urun_id=u["id"], 
        urun_adi=u["urun"], 
        kategori=u["kategori"], 
        stok=u["stok"], 
        fiyat=u["fiyat"], 
        garanti=u["garanti_yili"]
    )
    
    # 4. Adım: Ürettiğimiz bu canlı nesneyi ana listemize ekliyoruz (append)
    stok_listesi.append(yeni_urun_nesnesi)
    

stok_listesi: list[Urun] = [
    Urun(u["id"], u["urun"], u["kategori"], u["stok"], u["fiyat"], u["garanti_yili"])
    for u in ham_stok_verisi
]

print("=== 🏬 TEKNOLOJİ MAĞAZASI GÜNCEL STOK RAPORU ===")
print("-" * 75)

for urun_objesi in stok_listesi:
    print(urun_objesi.rapor_satiri())
print("-" * 75)

# Analiz 1: Depodaki Toplam Varlık Değeri (Tüm ürünlerin stok değerlerinin toplamı)
toplam_envanter_değeri = sum(urun.toplam_stok_degeri() for urun in stok_listesi)
print(f"💰 Depodaki Toplam Ürün Varlık Değeri: {toplam_envanter_değeri:,.2f} TL")

# Analiz 2: Kara Cuma (%15) İndirim Simülasyonu (Sadece Mobil Kategorisi İçin)
print("\n🔥 KAMPANYA: Mobil Kategorisinde %15 İndirimli Fiyatlar:")
mobil_urunler = filter(lambda x: x.kategori == "Mobil", stok_listesi)
for m in mobil_urunler:
    print(f"   - {m.ad:<14} -> Eski Fiyat: {m.fiyat} TL | Yeni Kampanya Fiyatı: {m.indirim_uygula(15):.2f} TL")

# Analiz 3: En Yüksek Maliyetli Stok Ürününü Bulma (max)
# .toplam_stok_degeri() metoduna göre en yüksek olanı buluyoruz
en_degerli_stok = max(stok_listesi, key=lambda x: x.toplam_stok_degeri())
print(f"\n🏆 Depoda En Çok Para Bağlanan Ürün: {en_degerli_stok.ad} (Toplam Değer: {en_degerli_stok.toplam_stok_degeri():,} TL)")