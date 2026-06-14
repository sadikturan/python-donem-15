# main.py

# Kendi yazdığımız dosyayı modül olarak içeri alıyoruz
import muhasebe

print(f"--- {muhasebe.sirket_adi} Maaş Bordro Sistemi ---")

# Modülün içindeki fonksiyonları canlı canlı çalıştırıyoruz
ahmet_maas = muhasebe.maas_hesapla(45000, 10)
kesinti = muhasebe.vergi_kesintisi(ahmet_maas)
net_maas = ahmet_maas - kesinti

print(f"Ahmet'in Brüt Maaşı : {ahmet_maas} TL")
print(f"Vergi Kesintisi    : {kesinti} TL")
print(f"Banka Hesabına Yatan: {net_maas} TL")