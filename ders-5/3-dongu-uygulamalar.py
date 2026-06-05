"""
Senaryo (İş Problemi): Bir finans ve e-ticaret şirketinde Veri Analisti olarak işe başladınız. Şirketin log sisteminden gelen harcama verileri oldukça kirli; içinde girilmeyen eksik veriler (None) ve sistemsel hatalardan kaynaklanan negatif sayılar var.

Sizden Beklenenler:

1- Kullanıcının sistem kapanana kadar ("bitti" yazana kadar) klavyeden anlık harcama verisi ekleyebileceği dinamik bir ara yüz sunmanız.

2- Girilen tüm verileri tek bir havuzda toplayıp; None ve negatif olan kirli verileri otomatik olarak ayıklamanız (Veri Temizleme).

3- Temizlenen veriler üzerinden Toplam Ciro, Ortalama Harcama ve VIP İşlemler (1000 TL üzeri) gibi kritik metrikleri hesaplayan bir analiz raporu basmanız.

"""

import time

ham_harcamalar = [120.50, 2500.00, None, -50.00, 450.00, 1800.75, None, 95.00]

print("(Sisteme eklemek istediğiniz harcamaları girin. Bitirmek için 'bitti' yazın.)")
print("-" * 50)

# ==============================================================================
# --- AŞAMA 1: DİNAMİK VERİ TOPLAMA ---
# ==============================================================================
while True:
    girdi = input("Harcama tutarı giriniz (veya 'bitti'): ").strip().lower()
    
    if girdi == "bitti":
        break  # Kullanıcı bitti yazarsa döngüyü anında sonlandırıyoruz
        
    # Sadece 'if-else' kullanarak ondalıklı sayı kontrolü yapıyoruz (try-except yok)
    elif girdi.replace(".", "", 1).isdigit():
        harcama_tutari = float(girdi)
        ham_harcamalar.append(harcama_tutari)
        print("Veri başarıyla listeye eklendi.")
    else:
        print("Geçersiz giriş! Lütfen sadece sayı veya 'bitti' yazın.")

print("\nVeri toplama tamamlandı. Analiz aşamasına geçiliyor...")
print("=" * 50)


# ==============================================================================
# --- AŞAMA 2: FOR DÖNGÜSÜ İLE VERİ TEMİZLEME VE ANALİZ ---
# ==============================================================================
temiz_harcamalar = []
vip_harcamalar = []
toplam_ciro = 0.0

for harcama in ham_harcamalar:
    # KOŞUL 1: Veri eksik mi (None) veya hatalı mı (negatif sayı)?
    if harcama is None or harcama <= 0:
        continue  # Kirli veriyi pas geç, döngünün başına dön (Data Cleaning)
        
    # Veri temizse bu satırlara ulaşır
    temiz_harcamalar.append(harcama)
    toplam_ciro = toplam_ciro + harcama  # Kümülatif toplam
    
    # KOŞUL 2: VIP Müşteri Analizi (1000 TL ve üzeri - Feature Engineering)
    if harcama >= 1000.0:
        vip_harcamalar.append(harcama)


# ==============================================================================
# --- AŞAMA 3: METRİKLERİN HESAPLANMASI (ANALİZ) ---
# ==============================================================================
toplam_islem = len(temiz_harcamalar)

# Sıfıra bölünme (ZeroDivisionError) hatasını engellemek için if-else kontrolü
if toplam_islem > 0:
    ortalama_harcama = toplam_ciro / toplam_islem
else:
    ortalama_harcama = 0.0


# ==============================================================================
# --- AŞAMA 4: VERİ ANALİZİ RAPORU ---
# ==============================================================================
print("               VERİ ANALİZ RAPORU               ")
print("=" * 50)
print("Sistemdeki Toplam Ham Veri Sayısı :", len(ham_harcamalar))
print("Temizlenen Analiz Edilebilir İşlem:", toplam_islem)
# f-string formatlaması yerine yuvarlama fonksiyonu (round) ve virgülle birleştirme kullandık
print("Toplam Ciro (Hasılat)            :", round(toplam_ciro, 2), "TL")
print("Müşteri Başına Ortalama Harcama  :", round(ortalama_harcama, 2), "TL")
print("-" * 50)
print("VIP İşlem Sayısı (1000 TL üzeri) :", len(vip_harcamalar))
print("VIP Harcama Listesi              :", vip_harcamalar)
print("=" * 50)

