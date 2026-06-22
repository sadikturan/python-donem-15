import numpy as np

# Temel Manuel Dizi Oluşturma
result = np.array([1, 3, 5, 7, 9])

# =============================================================================
# 1- HAZIR DİZİ ÜRETME FONKSİYONLARI (BUILT-IN GENERATORS)
# =============================================================================

# np.arange(start, stop, step): Belirli aralıkta, belirlenen artış miktarına göre dizi üretir.
result = np.arange(1, 10)       # 1'den başlar 10'a kadar (10 dahil değil) birer birer sayar.
result = np.arange(10, 100, 3)  # 10'dan başlar 100'e kadar üçer üçer artarak dizi oluşturur.

# np.zeros(shape): Belirtilen boyutta tamamen sıfırlardan oluşan "boş" bir matris/vektör açar.
result = np.zeros(10)           # 10 elemanlı sıfır vektörü (Veri tipi varsayılan olarak şamandıralı/float'tır)

# np.ones(shape): Belirtilen boyutta tamamen birlerden (1) oluşan matris üretir.
result = np.ones(10)            # 10 elemanlı birler vektörü
result = np.ones((3, 4))        # 2 boyutlu (3 satır, 4 sütun) birlerden oluşan matris

# np.linspace(start, stop, num): Başlangıç ve bitiş arasını, birbirine EŞİT UZAKLIKTA 'num' adet parçaya böler.
result = np.ones((3, 4)) # 0 ile 100 arasını eşit mesafeli 5 sayıya böler -> [0, 25, 50, 75, 100]
result = np.linspace(1, 5, 5)   # 1 ile 5 arasını eşit mesafeli 5 sayıya böler -> [1, 2, 3, 4, 5]


# =============================================================================
# 2- RASTGELE VERİ ÜRETİMİ 
# =============================================================================

# np.random.randint(low, high, size): Belirlenen aralıkta rastgele tam sayılar (integer) üretir.

result = np.random.randint(0, 10)        # 0 ile 10 arasında (10 hariç) rastgele TEK BİR tam sayı üretir.
rand_list = np.random.randint(0, 100, 5) # 0 ile 100 arasında rastgele 5 adet tam sayı içeren bir vektör üretir.

# np.random.rand(rows, cols): 0 ile 1 arasında Uniform (Düzgün) dağılıma sahip ondalıklı sayılar üretir.
result = np.random.rand(3, 3)           # 3x3 boyutunda, tüm elemanları 0-1 arasında olan matris.
result = np.random.randn(3, 3)          # 3x3 boyutunda, eksi veya artı değerler alabilen normal dağılımlı matris.


# =============================================================================
# 3- DİZİ ÖZELLİKLERİ VE ŞEKİLLENDİRME (RESHAPING)
# =============================================================================

np_array = np.arange(50)             # 0'dan 49'a kadar olan 50 elemanlı tek boyutlu düz bir çizgi (vektör).
np_multi = np_array.reshape(5, 10)   # Toplam eleman sayısını bozmadan 5 satır ve 10 sütunlu 2D matrise çevirir.


# =============================================================================
# 4- MATEMATİKSEL VE İSTATİSTİKSEL OPERASYONLAR (AGGREGATION)
# =============================================================================

# AXIS MANTIĞI: 2 boyutlu matrislerde işlem yönünü belirler.
# axis=0 -> SÜTUNLAR boyunca (yukarıdan aşağıya diklemesine) işlem yapar.
# axis=1 -> SATIRLAR boyunca (soldan sağa enlemesine) işlem yapar.

result = np_multi.sum(axis=0)  # Her bir sütunun kendi içindeki toplamını verir (Çıktı 10 elemanlı bir vektör olur).
result = np_multi.sum(axis=1)  # Her bir satırın kendi içindeki toplamını verir (Çıktı 5 elemanlı bir vektör olur).

result = np_multi.max()        # Tüm matris içindeki en büyük (maksimum) değeri bulur -> 49
result = np_multi.min()        # Tüm matris içindeki en küçük (minimum) değeri bulur -> 0
result = np_multi.mean()       # Tüm matrisin aritmetik ortalamasını hesaplar -> 24.5

# Endeks Avcılığı (.argmax ve .argmin)
# Sayının kendisini değil, o sayının kaçıncı sırada (indekste) durduğunu tespit eder.
result = rand_list.argmax()    # rand_list içindeki en büyük sayının hangi indeks numarasında olduğunu döndürür.

print(result)