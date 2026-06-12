# Kapsamlı Uygulama: Dinamik CSV/Metin Veritabanı Simülasyonu

print("====== MÜŞTERİ KAYIT OTOMASYONU ======")
print("(Kayıtları bitirmek için herhangi bir aşamada 'çıkış' yazabilirsiniz)\n")

# Dosya başlığı daha önce atılmamışsa, sistem ilk açılışta bir başlık bıraksın
try:
    with open("musteri_veritabani.csv", "r", encoding="utf-8") as f:
        pass
except FileNotFoundError:
    # Dosya yoksa İLK KEZ oluşturup başlıkları yazıyoruz
    with open("musteri_veritabani.csv", "w", encoding="utf-8") as f:
        f.write("MÜŞTERİ ADI | ŞEHİR | HARCAMA TUTARI\n")
        f.write("-" * 40 + "\n")

# Dinamik Veri Giriş Döngüsü
while True:
    # 1. Adım: İsim Alma ve Çıkış Kontrolü
    isim = input("Müşteri Adı: ").strip().title()
    if isim.lower() == "çıkış":
        print("\n[BİLGİ] Çıkış yapılıyor...")
        break
        
    # 2. Adım: Şehir Alma ve Çıkış Kontrolü
    sehir = input("Yaşadığı Şehir: ").strip().upper()
    if sehir.lower() == "çıkış":
        print("\n[BİLGİ] Çıkış yapılıyor...")
        break
        
    # 3. Adım: Harcama Alma ve Çıkış Kontrolü
    harcama = input("Yıllık Harcama Tutarı (TL): ").strip()
    if harcama.lower() == "çıkış":
        print("\n[BİLGİ] Çıkış yapılıyor...")
        break
    
    # 🎯 Alınan verileri formatlayarak dosyanın sonuna ('a') ekliyoruz
    # 'a' modu sayesinde eski kayıtlar asla silinmez, altına eklenir
    with open("musteri_veritabani.csv", "a", encoding="utf-8") as veritabani:
        veritabani.write(f"{isim} | {sehir} | {harcama} TL\n")
        print(f"✔️ {isim} isimli müşteri başarıyla diske kaydedildi.\n")

# --- RAPORLAMA ---
print("\n--- GÜNCEL MÜŞTERİ VERİTABANI DOSYASI ---")
with open("musteri_veritabani.csv", "r", encoding="utf-8") as oku:
    print(oku.read())