import numpy as np
import pandas as pd

# Başlangıç veri yapıları
numbers = [20, 30, 40, 50]
letters = ["a", "b", "c", "d", 20]  # Karışık tip: Pandas bunu otomatik 'object' yapar.
dict_data = {"a": 10, "b": 20, "c": 30}
random_numbers = np.random.randint(10, 100, 6)

# =============================================================================
# 1. PANDAS SERIES OLUŞTURMA YÖNTEMLERİ (CONSTRUCTION)
# =============================================================================

pandas_series = pd.Series()                   # Boş bir seri oluşturur.
pandas_series = pd.Series(numbers)            # Standart Python listesinden seri üretir.
pandas_series = pd.Series(letters)            # Karışık listeden üretir (Veri tipi: object).

pandas_series = pd.Series(5)                  # Skaler (tekil) değerden tek elemanlı seri üretir.
pandas_series = pd.Series(5, [0, 1, 2])       # Skaler değeri verilen indeks sayısı kadar çoklar -> [5, 5, 5]
pandas_series = pd.Series(numbers, ["a", "b", "c", "d"]) # Özel harf indeksleri (Label) atayarak üretir.
pandas_series = pd.Series(dict_data)          # Sözlükten üretir: Key'ler "indeks", Value'lar "veri" olur.
pandas_series = pd.Series(random_numbers)     # NumPy dizisini doğrudan seriye dönüştürür.


# =============================================================================
# 2. SAYISAL İNDEKS İLE SEÇİM VE DİLİMLEME (NUMERIC INDEXING)
# =============================================================================
pandas_series = pd.Series([20, 30, 40, 50])

result = pandas_series[0]        # 0. indeksteki elemanı getirir -> 20
result = pandas_series.iloc[-1]  # .iloc yardımıyla en sondaki elemanı güvenle getirir -> 50
result = pandas_series.iloc[-2]  # Sondan bir önceki elemanı getirir -> 40
result = pandas_series[:2]       # İlk iki elemanı dilimler -> [20, 30]
result = pandas_series.iloc[-2:] # Sondan iki elemanı koparır -> [40, 50]


# =============================================================================
# 3. ETİKETLİ İNDEKS İLE SEÇİM VE SINIRLAMALAR (LABEL INDEXING)
# =============================================================================
pandas_series = pd.Series([20, 30, 40, 51], ["a", "b", "c", "d"])

# result = pandas_series[-1]     # ❌ HATA: Harf indeksi varken doğrudan negatif sayı yazılırsa KeyError fırlatır!
result = pandas_series["a"]      # Açık etiket ismiyle çağrı -> 20
result = pandas_series["b"]      # Açık etiket ismiyle çağrı -> 30
result = pandas_series[2:]       # Harf indeksi olsa bile arka plandaki sayısal dilimleme hala çalışır -> [40, 51]
result = pandas_series[["a", "b"]] # Liste halinde birden fazla etiket seçimi (Geriye mini bir Seri döner)
result = pandas_series["b":]     # Harf etiketiyle dilimleme. NOT: Bitiş noktası ("d") da çıktıya dahildir!


# =============================================================================
# 4. SERİ ÖZELLİKLERİ VE MATEMATİKSEL İŞLEMLER
# =============================================================================
# Temel Nitelikler
result = pandas_series.ndim      # Serinin boyut sayısı (Seriler her zaman 1 boyutludur) -> 1
result = pandas_series.dtype     # İçindeki verilerin tipini söyler -> int64
result = pandas_series.shape     # Geometrik şeklini Tuple olarak döndürür -> (4,)

# İstatistiksel Özetler
result = pandas_series.sum()     # Elemanların toplamı
result = pandas_series.max()     # En büyük eleman
result = pandas_series.min()     # En küçük eleman

# Vektörel Operasyonlar (Broadcasting)
result = pandas_series + pandas_series # İndisdaş elemanları birbiriyle toplar.
result = pandas_series + 50            # Tüm elemanlara tek seferde 50 ekler.
result = np.sqrt(pandas_series)        # Tüm elemanların karekökünü vektörel hesaplar.


# =============================================================================
# 5. KOŞULLU FİLTRELEME (BOOLEAN MASKING)
# =============================================================================
result = pandas_series >= 50     # Her elemana sorar, geriye True/False serisi döndürür.

result = pandas_series % 2 == 0  # Çift kontrolü yapar (Not: Kodunuzdaki 51 tektir, o satır False döner).
result = pandas_series[pandas_series % 2 == 0] # Maskeyi seriye giydirir; sadece True (çift) olanları süzüp getirir.


# =============================================================================
# 6. İNDEKS HİZALAMA MANTIĞI (DATA ALIGNMENT)
# =============================================================================
# Pandas'ta iki seri toplanırken sıra numaralarına değil, İNDEKS ETİKETLERİNE bakılır.
opel2025 = pd.Series([20, 30, 40, 10], ["astra", "corsa", "mokka", "insignia"])
opel2026 = pd.Series([40, 30, 20, 10], ["astra", "corsa", "Grandland", "insignia"])

# Ortak indeksler (astra, corsa, insignia) toplanır.
# Birinde olup diğerinde olmayanlar (mokka, Grandland) eşleşemediği için boş veri (NaN) üretir.
toplam = opel2025 + opel2026

# print(toplam)
print(toplam["astra"])  # Eşleşen "astra" etiketlerinin toplamı ekrana basılır -> 60.0