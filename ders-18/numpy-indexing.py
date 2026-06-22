import numpy as np

# =============================================================================
# 1. TEK BOYUTLU DİZİLERDE (VEKTÖR) İNDEKSLEME VE SLICING
# =============================================================================
# Tek eksenli düz bir çizgi üzerinde çalışıyoruz. İndeks numaraları 0'dan başlar.

sayilar = np.array([1, 3, 5, 7, 9, 12, 15, 43, 4, 6, 8])

result = sayilar[3]    # Nokta Atışı: 3. indeksteki (4. sıradaki) elemanı getirir -> 7
result = sayilar[-1]   # Ters İndeksleme: Dizinin en sonundaki elemanı getirir -> 8
result = sayilar[0:3]  # Dilimleme (Slicing): 0, 1 ve 2. indeksleri alır (3 dahil değil) -> [1, 3, 5]


# =============================================================================
# 2. İKİ BOYUTLU DİZİLERDE (MATRİS) İNDEKSLEME VE SLICING
# =============================================================================
# Formül her zaman şudur: matris[satır_şartı , sütun_şartı]

# Virgülün solu SATIRLARI (Axis 0), sağ tarafı ise SÜTUNLARI (Axis 1) temsil eder.
sayilar2 = np.array([[1, 3, 5], 
                     [7, 9, 12], 
                     [43, 4, 6]])

# A) Nokta Atışı Satır ve Hücre Seçimleri
result = sayilar2[0]     # Sadece tek bir sayı girilirse o indeksteki SATIRIN tamamını getirir -> [1, 3, 5]
result = sayilar2[0, 1]  # 0. satır, 1. sütundaki kesişim hücresini getirir -> 3
result = sayilar2[2, 2]  # 2. satır, 2. sütundaki kesişim hücresini getirir -> 6

# B) İki Boyutlu Dilimleme Kombinasyonları
# İki noktadan (:) önce ve sonra değer yazılmazsa "TÜMÜNÜ AL" anlamına gelir.

result = sayilar2[:, 2]    # Satırların TÜMÜNÜ al, ama sadece 2. indeksteki SÜTUNU getir -> [5, 12, 6]
result = sayilar2[:, 0:2]  # Satırların TÜMÜNÜ al, sütunlardan 0 ve 1. indeksleri getir -> [[1, 3], [7, 9], [43, 4]]
result = sayilar2[-1, :]   # Sadece en son satırı al, o satırın sütunlarının TÜMÜNÜ getir -> [43, 4, 6]

# C) Alt Matris Koparma (Sub-matrix Extraction)
# Hem satırlarda hem sütunlarda sınır çizerek matrisin içinden mini bir kare matris koparıyoruz.
result = sayilar2[:2, :2]  # 0 ve 1. satırların, 0 ve 1. sütunlarıyla kesişen bölgeyi alır.
                           # Çıktı: [[1, 3], 
                           #         [7, 9]]

result = sayilar2[1:, 1:]   # [[ 9 12]
                            #  [ 4  6]]

print(result)