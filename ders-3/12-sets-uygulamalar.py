# A Kampanyasına katılan müşteri ID'leri
grup_A = {101, 102, 103, 104, 105}

# B Kampanyasına katılan müşteri ID'leri
grup_B = {104, 105, 106, 107, 108}

# YÖNTEM 1: Kesişim (Intersection) -> Her iki kampanyaya da katılan ortak müşteriler kimler?
ortak_musteriler = grup_A.intersection(grup_B)
# Veya sembolik olarak: ortak_musteriler = grup_A & grup_B
print("Her iki gruba da dahil olanlar:", ortak_musteriler) # {104, 105}

# YÖNTEM 2: Birleşim (Union) -> Kampanyalara katılan tüm benzersiz müşterilerin listesi
tum_musteriler = grup_A.union(grup_B)
# Veya sembolik olarak: tum_musteriler = grup_A | grup_B
print("Toplam tekil müşteri havuzu :", tum_musteriler) # {101, 102, 103, 104, 105, 106, 107, 108}

# YÖNTEM 3: Fark (Difference) -> A grubunda olup B grubunda olmayan müşteriler kimler?
sadece_A = grup_A.difference(grup_B)
# Veya sembolik olarak: sadece_A = grup_A - grup_B
print("Sadece A grubunda olanlar    :", sadece_A) # {101, 102, 103}


print("====== VERİ ANALİTİĞİ TEKİL KULLANICI TESPİTİ ======\n")

# Gün içinde siteye girenlerin ham IP listesi (Bazı kullanıcılar gün içinde defalarca girmiş)
ziyaretci_ip_loglari = [
    "192.168.1.1", "10.0.0.5", "192.168.1.1", 
    "172.16.0.4", "10.0.0.5", "192.168.1.1", "185.45.2.1"
]

print("Toplam Toplanan Log Sayısı (Satır sayısı):", len(ziyaretci_ip_loglari))

# Veri Temizleme Adımı: Listeyi anında Set yapısına dönüştürerek tüm tekrarları yok ediyoruz
benzersiz_ziyaretciler = set(ziyaretci_ip_loglari)

print("Sistemdeki Benzersiz IP Adresleri        :", benzersiz_ziyaretciler)
print("Sitemizi Ziyaret Eden Gerçek Kişi Sayısı :", len(benzersiz_ziyaretciler))