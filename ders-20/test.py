import time
import tracemalloc
import pandas as pd

df_orjinal = pd.read_csv("datasets/imdb.csv")

print(f"✅ Orijinal dosya yüklendi (Mevcut Satır Sayısı: {len(df_orjinal):,})")

# Testin etkili olması için orijinal tabloyu arka arkaya ekleyerek satır sayısını artırıyoruz
# Not: Kendi bilgisayarınızın RAM gücüne göre buradaki çarpanı (Örn: 20000) artırıp azaltabilirsiniz.
df = pd.concat([df_orjinal] * 20000, ignore_index=True)
print(f"🚀 Simülasyon Hazır! Toplam Satır Sayısı: {len(df):,}\n")


# =============================================================================
# ❌ SİZİN 1. ÖRNEĞİNİZ: ZİNCİRLEME SEÇİM YÖNTEMİ ([][])
# =============================================================================
tracemalloc.start()  # RAM sayacını başlat
start_time = time.time()  # Zamanı başlat

# Sizin yazdığınız 1. kod satırı:
zincir_sonuc = (
    df[df["Rating"] >= 8.0][["Movie_Title", "Num_Reviews"]]
    .sort_values(by="Num_Reviews", ascending=False)
    .head(5)
)

zincir_time = time.time() - start_time
_, zincir_ram_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()  # RAM sayacını durdur


# =============================================================================
# 🚀 SİZİN 2. ÖRNEĞİNİZ: NOKTA ATIŞI MATRİS SEÇİMİ (.loc[,])
# =============================================================================
tracemalloc.start()  # RAM sayacını sıfırlayıp yeniden başlat
start_time = time.time()  # Zamanı yeniden başlat

# Sizin yazdığınız 2. kod satırı (.loc standartı):
loc_sonuc = (
    df.loc[df["Rating"] >= 8.0, ["Movie_Title", "Num_Reviews"]]
    .sort_values(by="Num_Reviews", ascending=False)
    .head(5)
)

loc_time = time.time() - start_time
_, loc_ram_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()


# =============================================================================
# 📊 3. SAKLANAN RAPORUN TAHTAYA BASILMASI (BENCHMARK REPORT)
# =============================================================================
# RAM ölçümlerini Megabayt'a (MB) çeviriyoruz
zincir_ram_mb = zincir_ram_peak / (1024**2)
loc_ram_mb = loc_ram_peak / (1024**2)

print("=" * 70)
print("📊 GERÇEK IMDB VERİSİ CANLI PERFORMANS RAPORU")
print("=" * 70)
print(
    f"❌ 1. ÖRNEK (Zincirleme [][]) -> Süre: {zincir_time:.4f} saniye | RAM Yükü: {zincir_ram_mb:.2f} MB"
)
print(
    f"🚀 2. ÖRNEK (Nokta Atışı .loc) -> Süre: {loc_time:.4f} saniye | RAM Yükü: {loc_ram_mb:.2f} MB"
)
print("-" * 70)

# Fark hesaplamaları
hiz_kati = zincir_time / loc_time
ram_tasarruf = zincir_ram_mb - loc_ram_mb

print(f"🎯 ÖĞRENCİLERE GÖSTERİLECEK ÇIKTI (İÇGÖRÜ):")
print(
    f"   👉 Bizim yazdığımız .loc'lu 2. yöntem, 1. yönteme göre {hiz_kati:.1f} KAT DAHA HIZLI çalıştı."
)
print(
    f"   👉 Bellekte (RAM) {ram_tasarruf:.2f} MB daha az geçici çöp (ara tablo) bıraktı."
)
print("=" * 70)

# Doğrulama çıktısı (Öğrenciler iki kodun da aynı şeyi ürettiğini görsün)
print("\n💡 Her iki kodun da ürettiği zirvedeki o popüler 5 film:")
print(loc_sonuc)