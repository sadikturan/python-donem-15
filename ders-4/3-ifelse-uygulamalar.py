# 1. Uygulama Örneği: E-Ticaret Sepet Kontrolü
# Şart: Sepet 500'den büyükse VEYA kullanıcı Premium ise kargo bedava

sepet_tutari = 450
premium_uye_mi = False

if sepet_tutari >= 500 or premium_uye_mi == True:
    kargo_ucreti = 0
    print("Tebrikler! Kargo ücretsiz.")
else:
    kargo_ucreti = 40
    print("Kargo ücreti 40 TL sepetinize eklenmiştir.")

# Toplam ödenecek tutarı güncelleyelim
toplam_tutar = sepet_tutari + kargo_ucreti
print(f"Toplam Ödenecek: {toplam_tutar} TL")


# 3. Uygulama: Fintech Kredi Risk Puanlama (Çoklu Mantıksal Operatörler)
# Veri analizinde birden fazla şartın aynı anda kontrol edilmesi (ve/veya mantığı) sıklıkla kullanılır.
# Senaryo: Bir bankanın risk analitiği departmanı için tek bir müşterinin başvuru parametrelerini (Kredi Skoru ve Aylık Gelir) 
# inceleyen mikro bir karar destek mekanizması kuralım.

print("====== RİSK ANALİZİ KARAR DESTEK SİSTEMİ ======\n")

# Analiz edilecek tekil müşteri kartı bilgileri
kredi_skoru = 1150
aylik_gelir = 45000
aktif_yasal_takip_var_mi = False

# Mantıksal Filtreleme Başlıyor
if aktif_yasal_takip_var_mi == True:
    # Yasal takibi olan profil direkt elenir, gelire bakılmaz
    karar = "RED - Yasal Takip Mevcut"

elif kredi_skoru >= 1300 and aylik_gelir >= 40000:
    # Hem skoru hem geliri mükemmel olan grup
    karar = "ONAY - Düşük Riskli VIP Profil"

elif kredi_skoru >= 900 or aylik_gelir >= 60000:
    # Skoru sınırda olsa bile geliri çok yüksek olan veya tam tersi durumlar için şartlı kabul
    karar = "ŞARTLI ONAY - İnceleme Gerekli"

else:
    # Hiçbir şartı kurtarmayan grup
    karar = "RED - Yetersiz Skor ve Gelir"

print("Müşteri Analiz Sonucu:", karar)


# 3- Uygulama Örneği: Akıllı Ev Termostat Otomasyonu
print("=== AKILLI EV TERMOSTAT SİSTEMİ ===")

# --- 1. SENSÖR VERİLERİNİ ALMA (Giriş) ---
ortam_sicakligi = float(input("Mevcut oda sıcaklığını giriniz (°C): "))
evde_kimse_var_mi_metin = input("Evde birisi var mı? (evet/hayir): ").lower().strip()

# Kullanıcının yazdığı metni True/False (Boolean) değerine çeviriyoruz
evde_kimse_var_mi = evde_kimse_var_mi_metin == "evet"

# --- 2. KOŞULLU DURUMLAR VE KARAR MEKANİZMASI ---

# ANA KOŞUL 1: Eğer evde kimse YOKSA, enerji tasarrufu için her şeyi kapat
if not evde_kimse_var_mi: # evde_kimse_var_mi == False anlamına gelir
    print("\n[EKO MOD] Evde kimse tespit edilmedi. Sistem enerji tasarrufu modunda: Isıtıcı/Soğutucu KAPATILDI.")

# ANA KOŞUL 2: Evde birisi VARSA, sıcaklığa göre iklimlendirmeyi çalıştır
else:
    print("\n[KONFOR MODU] Evde hareket tespit edildi. Sıcaklık kontrol ediliyor...")
    print("-" * 45)
    
    # İç içe (Nested) If yapısı ile sıcaklık aralıklarını kontrol ediyoruz
    if ortam_sicakligi < 18.0:
        print("Durum: Oda çok soğuk! 🥶")
        print("Aksiyon: Kombi YÜKSEK derecede çalıştırılıyor.")
        
    elif 18.0 <= ortam_sicakligi <= 22.0:
        print("Durum: Oda serin. 🍃")
        print("Aksiyon: Kombi DÜŞÜK derecede çalıştırılıyor.")
        
    elif 22.1 <= ortam_sicakligi <= 26.0:
        print("Durum: Sıcaklık ideal.  ")
        print("Aksiyon: Tüm sistemler beklemede (Stand-by).")
        
    else: # Sıcaklık 26 dereceden büyükse
        print("Durum: Oda çok sıcak! 🥵")
        print("Aksiyon: Klima SOĞUTMA modunda çalıştırılıyor.")

print("=" * 45)