# Kapsamlı Uygulama: Veri Temizleme ve Log Otomasyonu

# Büyük veri setleriyle uğraşırken (özellikle veri analitiği projelerinde) ham verilerin içindeki hataları ayıklayıp, çöken satırları bir rapora loglamak çok yaygın bir pratik yöntemdir.

# Web'den veya bir API'den gelen kirli, karmaşık üye veri havuzu
uyeler_veri_havuzu = [
    {"isim": "Ahmet", "gelir": "25000", "borc": 5000},
    {"isim": "Zeynep", "gelir": "Belirtilmemiş", "borc": 0}, # ValueError riski
    {"isim": "Can", "gelir": 45000, "borc": None},          # TypeError riski
    {"isim": "Merve", "gelir": 30000, "borc": 2000}
]

temiz_analiz_listesi = []
hatali_kayitlar_logu = []

print("=== VERİ TARAMA VE ANALİZ BAŞLADI ===")
print("-" * 50)

for veri in uyeler_veri_havuzu:
    isim = veri["isim"]
    try:
        # Metin olarak gelen gelirleri sayıya çevirmeye zorluyoruz
        net_gelir = float(veri["gelir"])
        mevcut_borc = float(veri["borc"])
        
        # Kişinin borç/gelir oranını hesaplayalım
        oran = mevcut_borc / net_gelir
        
    except ValueError:
        hatali_kayitlar_logu.append(f"{isim}: Gelir veya borç bilgisi sayısal değil!")
        continue
    except TypeError:
        hatali_kayitlar_logu.append(f"{isim}: Eksik veri (None) tespit edildi!")
        continue
    except ZeroDivisionError:
        hatali_kayitlar_logu.append(f"{isim}: Geliri 0 olduğu için oran hesaplanamadı!")
        continue
    else:
        # Eğer try bloğu tertemiz çalıştıysa veriyi analiz listemize ekliyoruz
        temiz_analiz_listesi.append({
            "isim": isim,
            "borc_gelir_orani": round(oran, 2)
        })
    finally:
        print(f"-> {isim} verisi kontrol edildi.")

print("-" * 50)
print("=== ANALİZ SONUÇ RAPORU ===")
print(f"Başarıyla İşlenen Temiz Veriler: {temiz_analiz_listesi}")
print(f"Hata Günlüğü (Log) : {hatali_kayitlar_logu}")