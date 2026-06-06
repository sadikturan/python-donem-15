# Uygulama 1: Yaş Hesaplayıcı ve Filtreleme

# Senaryo: Bir veri analisti olarak, veri tabanından gelen kullanıcı doğum yıllarını incelemeniz, güncel yıla (2026) göre yaşlarını hesaplamanız ve sadece reşit olan (>= 18) kullanıcıların yaşlarını analiz için filtrelemeniz gerekiyor.

# 'dogum_yillari' bir tam sayı listesidir, fonksiyon geriye yine bir tam sayı listesi döner.
def yas_hesapla_ve_filtrele(dogum_yillari: list[int]) -> list[int]:
    guncel_yil: int = 2026  # local değişken
    resit_olanlar: list[int] = []
    
    for yil in dogum_yillari:
        yas = guncel_yil - yil
        if yas >= 18:
            resit_olanlar.append(yas)
            
    return resit_olanlar

# --- TEST VE ANALİZ ---
dogum_tarihleri: list[int] = [2012, 1998, 2005, 2015, 1990]
sonuc = yas_hesapla_ve_filtrele(dogum_tarihleri)

print("=== VERİ ANALİZİ FİLTRELEME SONUCU ===")
print(f"Reşit Olan Kullanıcıların Yaşları: {sonuc}")
# Çıktı: [28, 21, 36]


# Uygulama 2: E-Ticaret - Dinamik İndirimli Fiyat Hesaplayıcı

# Senaryo: Bir e-ticaret sitesinin sepet modülünü inşa ediyorsunuz. Ürünün ham fiyatına Türkiye şartlarına uygun KDV oranını ekleyecek, eğer kullanıcı geçerli bir indirim kuponu girdiyse fiyatı düşecek modüler bir yapı kurmalıyız.

# Fiyatlar ondalıklı (float) olabilir. kupon_kodu metindir veya girilmeyebilir (None)
# 'kdv_orani' girilmezse varsayılan (Default) olarak %20 kabul edilir.

def sepet_hesapla(ham_fiyat: float | int, kdv_orani: int = 20, kupon_kodu: str | None = None) -> float:
    # 1. Adım: KDV'li fiyatı hesaplayalım
    kdv_miktari = ham_fiyat * (kdv_orani / 100)
    toplam_fiyat = ham_fiyat + kdv_miktari
    
    # 2. Adım: Kupon kodu kontrolü (Eğer kupon girildiyse)
    if kupon_kodu == "PYTHON20":
        print("💡 [SİSTEM]: Tebrikler! %20 indirim kuponu başarıyla uygulandı.")
        toplam_fiyat = toplam_fiyat * 0.80  # Fiyatı %20 düşürdük
        
    return toplam_fiyat

# --- TEST SENARYOLARI ---
print("\n=== E-TİCARET SEPET HESAPLAMA ===")

# Senaryo A: Kuponsuz alışveriş (Sadece fiyat gönderiyoruz, KDV varsayılan %20 uygulanıyor)
fiyat1 = sepet_hesapla(1000)
print(f"1. Sepet Toplamı (Kuponsuz): {fiyat1} TL") # 1000 + %20 KDV = 1200 TL

# Senaryo B: Kuponlu alışveriş (Keyword kullanarak kupon kodunu gönderiyoruz)
fiyat2 = sepet_hesapla(1000, kupon_kodu="PYTHON20")
print(f"2. Sepet Toplamı (Kuponlu) : {fiyat2} TL")  # 1200'ün %20 indirimlisi = 960 TL



# Uygulama 3: Bankacılık - ATM Para Çekme ve Limit Algoritması

# Senaryo: Bir bankanın ATM yazılımı için para çekme fonksiyonu yazacaksınız. Kullanıcının bir Ana Hesabı (Bakiye) bir de acil durumlar için tanımlanmış Kredili Mevduat Hesabı (Ek Hesap) vardır. Para çekilirken önce ana hesap tüketilmeli, yetmezse ek hesaba başvurulmalı, ikisinin toplamı da yetmiyorsa işlem reddedilmelidir.

# --- BANKA VERİ TABANI SİMÜLASYONU (SÖZLÜK) ---
# Gerçek projelerde bu veriler veri tabanından sözlük formatında gelir.
AhmetHesap: dict[str, any] = {
    "ad": "Ahmet Yılmaz",
    "hesap_no": "123456",
    "bakiye": 3000,
    "ek_hesap": 2000
}

# --- FONKSİYON TANIMLAMALARI ---

def bakiye_sorgula(hesap: dict) -> None:
    """Kullanıcının mevcut hesap durumunu ekrana yazdırır."""
    print("\n--- GÜNCEL HESAP DURUMU ---")
    print(f"Müşteri             : {hesap['ad']}")
    print(f"Ana Hesap Bakiye    : {hesap['bakiye']} TL")
    print(f"Ek Hesap Limit      : {hesap['ek_hesap']} TL")
    print(f"Toplam Kullanılabilir: {hesap['bakiye'] + hesap['ek_hesap']} TL")
    print("-" * 30)


def para_cek(hesap: dict, miktar: int | float) -> None:
    """Hesaptan para çekme işlemini koşullara göre kontrol eder ve gerçekleştirir."""
    print(f"\n✈️ [İŞLEM]: {hesap['ad']} hesabından {miktar} TL çekilmek isteniyor...")
    
    # Koşul 1: Ana hesapta yeterli para var mı?
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("✔️ [BAŞARILI]: İşlem onaylandı. Paranızı ana hesabınızdan alabilirsiniz.")
        
    # Koşul 2: Ana hesap yetmiyor ama ek hesapla birlikte toplam limit kurtarıyor mu?
    elif (hesap["bakiye"] + hesap["ek_hesap"]) >= miktar:
        ek_hesap_kullanimi = miktar - hesap["bakiye"]
        
        # Önce ana hesabı tamamen sıfırlıyoruz
        hesap["bakiye"] = 0
        # Kalan borç miktarını ek hesaptan düşüyoruz
        hesap["ek_hesap"] -= ek_hesap_kullanimi
        
        print("✔️ [BAŞARILI]: Ana hesabınız yetersiz olduğundan ek hesap limiti kullanıldı.")
        
    # Koşul 3: İki hesapta duran para da çekilmek istenen miktara yetmiyor
    else:
        print("❌ [HATA]: Yetersiz bakiye! Çekilmek istenen tutar toplam limitinizi aşmaktadır.")


# --- UYGULAMA AKIŞI (ANA PROGRAM) ---

# 1. Adım: İlk mevcut durumu ekrana basalım
bakiye_sorgula(AhmetHesap)

# 2. Adım: Ana hesaptaki paradan daha azını çekelim (Sorunsuz çekmeli)
para_cek(AhmetHesap, 2000)
bakiye_sorgula(AhmetHesap) # Ana hesapta 1000 TL kalmalı

# 3. Adım: Kalan ana hesaptan fazlasını çekelim (Ek hesap otomatik devreye girmeli)
para_cek(AhmetHesap, 2500) # 1000 TL ana hesaptan çekilecek, kalan 1500 TL ek hesaptan düşecek
bakiye_sorgula(AhmetHesap) # Ana hesap: 0 TL, Ek hesap: 500 TL kalmalı

# 4. Adım: Kalan limiti tamamen aşan bir tutar çekmeyi deneyelim (Bloke etmeli)
para_cek(AhmetHesap, 4000) # Toplam limit 500 TL olduğu için HATA vermeli