import numpy as np

# 0- Temel Rastgele Dizilerin Üretilmesi
sayilar1 = np.random.randint(10, 100, 6)
sayilar2 = np.random.randint(10, 100, 6)

# =============================================================================
# 1. DİZİLERDE VEKTÖREL MATEMATİKSEL İŞLEMLER (ELEMENT-WISE)
# =============================================================================
# NOT: İki dizinin matematiksel işleme girebilmesi için eleman sayılarının (shape) birebir eşit olması gerekir.

result = sayilar1 + sayilar2  # Eleman düzeyinde toplama
result = sayilar1 + 10        # BROADCASTING: Dizinin TÜM elemanlarına tek seferde 10 ekler.
result = sayilar1 - sayilar2  # Eleman düzeyinde çıkarma
result = sayilar1 * sayilar2  # Eleman düzeyinde çarpma
result = sayilar1 / sayilar2  # Eleman düzeyinde bölme


# =============================================================================
# 2. MATRİS ŞEKİLLENDİRME
# =============================================================================
sayilar1 = sayilar1.reshape(2, 3)
sayilar2 = sayilar2.reshape(2, 3) # DÜZELTME: sayilar2'yi kendi bağımsız verisinden şekillendiriyoruz.

result = sayilar1  # 2x3 boyutunda 1. matris
result = sayilar2  # 2x3 boyutunda 2. matris


# =============================================================================
# 3. MATRİS BİRLEŞTİRME OPERASYONLARI (STACKING)
# =============================================================================
# Veri biliminde farklı kaynaklardan gelen öznitelikleri (features) birleştirmek için sıklıkla kullanılır.
# Kritik Kural: Birleştirilecek matrislerin kesişen eksen boyutları uyumlu olmalıdır!

# np.vstack (Vertical Stack): Matrisleri DİKEY (üst üste) birleştirir. Sütun sayıları eşit olmalıdır.
# (2,3) ve (2,3) boyutundaki iki matrisi üst üste koyarak (4,3) boyutunda yeni bir matris üretir.
result1 = np.vstack((sayilar1, sayilar2))

# np.hstack (Horizontal Stack): Matrisleri YATAY (yan yana) birleştirir. Satır sayıları eşit olmalıdır.
# (2,3) ve (2,3) boyutundaki iki matrisi yan yana koyarak (2,6) boyutunda yeni bir matris üretir.
result2 = np.hstack((sayilar1, sayilar2))


# =============================================================================
# 4. MATRİS BAZLI BOOLEAN MASKING (KOŞULLU SORGULAMA)
# =============================================================================
# Matrisin her bir elemanına soruyu sorar ve geriye aynı boyutta True/False matrisi döndürür.

result = sayilar1 >= 50    # Matriste 50'den büyük veya eşit olan hücreleri True yapar.
result = sayilar1 % 2 == 0 # Matriste çift sayı olan hücreleri True, tekleri False yapar.
result = sayilar1[sayilar1 % 2 == 0] # Matriste çift sayı olan hücreleri True, tekleri False yapar.

print(result)