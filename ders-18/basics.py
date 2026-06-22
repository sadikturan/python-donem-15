"""
Bölüm 1: Neden Numpy?
Şimdiye kadar yaptığımız analizlerde Saf Python listelerini ve sözlüklerini kullandık. Ancak milyonlarca satırdan oluşan büyük verilerle (Big Data) çalışırken standart Python listeleri hem çok yavaş kalır hem de yüksek RAM tüketir. İşte bu kırılma noktasında imdadımıza C diliyle yazılmış, ışık hızında çalışan NumPy kütüphanesi yetişir.

NumPy, Python'da bilimsel hesaplamalar ve çok boyutlu diziler (matrisler) üzerinde yüksek performanslı işlemler yapmak için kullanılan en temel kütüphanedir. Pandas, Scikit-Learn, TensorFlow gibi devasa kütüphanelerin tamamı NumPy mimarisinin üzerine inşa edilmiştir.

** Python listelerine aynı anda hem int, hem str, hem bool koyabilirsiniz. Bu esneklik hantallık yaratır. NumPy dizileri ise homojendir; içindeki tüm elemanlar tek bir veri tipinde (örneğin sadece float veya sadece int) olmak zorundadır.

"NumPy veri bilimi ekosisteminin çelik iskeleti, motoru ve matematiksel kalbidir; Pandas ise bu motorun üzerine inşa edilmiş konforlu, zırhlı ve lüks bir kurumsal yönetim arabasıdır."

Bölüm 2: NumPy Kurulumu ve İlk Dizi (Array) Oluşturma

pip install numpy


Vektör neden önemli?

"Hava bugün çok güzel" cümlesi ile "Gökyüzü pırıl pırıl ve güneşli" cümlesi içinde ortak tek bir kelime barındırmaz.

Ancak yapay zeka bu iki cümleyi vektör uzayına yerleştirdiğinde, ikisi de "güzel hava" koordinatlarına çok yakın düşer. Yapay zeka veriyi kelime olarak değil, kavram olarak saklamış olur.

"Kral" kelimesi matematiksel olarak: [0.23, -0.45, 0.89, ..., 0.11]
"Kraliçe" kelimesi matematiksel olarak: [0.21, -0.41, 0.85, ..., 0.13]

"""

import numpy as np

# python list
py_list = [1,2,3,4,5,6,7,8,9]
print(type(py_list))
print(py_list)

# numpy array
np_list = np.array([1,2,3,4,5,6,7,8,9])
print(type(np_list))
print(np_list)

# İç içe geçmiş Python listeleriyle manuel matris simülasyonu
py_multi = [[1,2,3],[4,5,6],[7,8,9]]

# Manuel Dönüşüm: Python listesini doğrudan 2 boyutlu matrise çevirme
num_multi = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Dinamik Dönüşüm: Tek boyutlu 9 elemanlı bir diziyi .reshape() ile 3x3 matrise çevirme
# (3 satır * 3 sütun = 9 eleman kuralına sıkı sıkıya bağlıyız!)
np_multi = np_list.reshape(3,3)

print(np_list)
print(np_multi)

print(np_list.ndim)
print(np_multi.ndim)    # 2 boyutlu. dizinin kaç boyutlu (kaç eksenli) olduğunu söyler.

print(np_list.shape)
print(np_multi.shape)   # (3, 3) yapının iki eksenden (Satırlar ve Sütunlar) oluştuğunu gösterir.


# 1'den 24'e kadar toplam 24 elemanlı tek boyutlu bir dizi oluşturuyoruz
dizi_1d = np.arange(1, 25)

# 3 BOYUTLU DÖNÜŞÜM: Toplam eleman sayısı (2 * 3 * 4 = 24) kuralına sadığız!
dizi_3d = dizi_1d.reshape(2, 3, 4)

# [[[ 1  2  3  4]
#   [ 5  6  7  8]
#   [ 9 10 11 12]]

#  [[13 14 15 16]
#   [17 18 19 20]
#   [21 22 23 24]]]

