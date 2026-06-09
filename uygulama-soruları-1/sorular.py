satis_verisi: list[dict] = [
    {"id": 1, "kategori": "Elektronik", "urun": "Kablosuz Kulaklık", "adet": 2, "fiyat": 1200, "musteri": "Premium"},
    {"id": 2, "kategori": "Moda", "urun": "Kışlık Mont", "adet": 1, "fiyat": 3500, "musteri": "Standart"},
    {"id": 3, "kategori": "Ev & Yaşam", "urun": "Kahve Makinesi", "adet": 1, "fiyat": 4500, "musteri": "Premium"},
    {"id": 4, "kategori": "Elektronik", "urun": "Akıllı Saat", "adet": 3, "fiyat": 2500, "musteri": "Standart"},
    {"id": 5, "kategori": "Moda", "urun": "Spor Ayakkabı", "adet": 2, "fiyat": 1800, "musteri": "Premium"},
    {"id": 6, "kategori": "Ev & Yaşam", "urun": "Nevresim Takımı", "adet": 1, "fiyat": 950, "musteri": "Standart"},
    {"id": 7, "kategori": "Kitap", "urun": "Yazılım Bilimi Tarihi", "adet": 5, "fiyat": 150, "musteri": "Premium"},
    {"id": 8, "kategori": "Elektronik", "urun": "Bluetooth Hoparlör", "adet": 1, "fiyat": 850, "musteri": "Standart"},
    {"id": 9, "kategori": "Moda", "urun": "Deri Ceket", "adet": 1, "fiyat": 5000, "musteri": "Premium"},
    {"id": 10, "kategori": "Ev & Yaşam", "urun": "Dikey Süpürge", "adet": 1, "fiyat": 8900, "musteri": "Premium"},
    {"id": 11, "kategori": "Kitap", "urun": "Python ile Veri Analizi", "adet": 3, "fiyat": 220, "musteri": "Standart"},
    {"id": 12, "kategori": "Elektronik", "urun": "Oyuncu Mouse", "adet": 2, "fiyat": 650, "premium": "Premium"}, 
    {"id": 13, "kategori": "Moda", "urun": "Sırt Çantası", "adet": 1, "fiyat": 450, "musteri": "Standart"},
    {"id": 14, "kategori": "Ev & Yaşam", "urun": "Çelik Tencere Seti", "adet": 1, "fiyat": 2300, "musteri": "Standart"},
    {"id": 15, "kategori": "Kitap", "urun": "Algoritmalar 101", "adet": 2, "fiyat": 180, "musteri": "Premium"},
    {"id": 16, "kategori": "Elektronik", "urun": "27' Oyuncu Monitörü", "adet": 1, "fiyat": 7200, "musteri": "Premium"},
    {"id": 17, "kategori": "Moda", "urun": "Güneş Gözlüğü", "adet": 1, "fiyat": 1200, "musteri": "Standart"},
    {"id": 18, "kategori": "Ev & Yaşam", "urun": "Hava Temizleyici", "adet": 1, "fiyat": 5400, "musteri": "Premium"},
    {"id": 19, "kategori": "Kitap", "urun": "Yapay Zeka Felsefesi", "adet": 1, "fiyat": 200, "musteri": "Standart"},
    {"id": 20, "kategori": "Elektronik", "urun": "Mekanik Klavye", "adet": 2, "fiyat": 1100, "musteri": "Standart"},
    {"id": 21, "kategori": "Moda", "urun": "Klasik Takım Elbise", "adet": 1, "fiyat": 6000, "musteri": "Premium"},
    {"id": 22, "kategori": "Ev & Yaşam", "urun": "Akıllı Ampul", "adet": 4, "fiyat": 350, "musteri": "Standart"},
    {"id": 23, "kategori": "Kitap", "urun": "İstatistik Mantığı", "adet": 1, "fiyat": 250, "musteri": "Premium"},
    {"id": 24, "kategori": "Elektronik", "urun": "USB-C Çoklayıcı", "adet": 3, "fiyat": 400, "musteri": "Standart"},
    {"id": 25, "kategori": "Moda", "urun": "Pamuklu Tişört", "adet": 5, "fiyat": 300, "musteri": "Premium"}
]

# Soru 1: Toplam Ciro ve Toplam Satılan Ürün Adedini Bulma
# Her işlemin cirosu (adet * fiyat) formülüyle bulunur. List Comprehension ve sum() kullanarak 
# mağazanın toplam ciro ve satılan toplam ürün adedini hesaplayınız.
# Cevap:



# Soru 2: En Çok Ürün Satın Alan Müşteri Tipini Bulma 
# Pazarlama ekibi için Premium müşterilerin mi toplamda daha fazla adet ürün satın aldığını, 
# yoksa Standart müşterilerin mi daha fazla aldığını sum() yardımıyla adet bazında karşılaştırınız.
# Cevap:




# Soru 3: En Ucuz Tekil Ürünü Bulma (min)
# Mağazanın en düşük birim fiyatlı (adet gözetmeksizin, sadece 'fiyat' özelliğine göre) 
# ürününün hangisi olduğunu ve hangi kategoride yer aldığını min() fonksiyonu ve lambda ile bulunuz.
# Cevap:



# Soru 4: En Yüksek Ciro Yapan Tekil Satışı Bulma (max)
# Gün içinde tek seferde en büyük ciroyu (adet * fiyat) bırakan faturayı ve ürünü 
# max() fonksiyonu ve lambda yardımıyla filtreleyiniz.
# Cevap:



# Soru 5: Ürünleri Kazandırdığı Ciroya Göre Küçükten Büyüğe Sıralama (sorted)
# Gün sonu raporunda listelenmek üzere, tüm satış işlemlerini kazandırdığı ciroya göre 
# küçükten büyüğe doğru sıralanmış yeni bir liste haline sorted() ve lambda kullanarak getiriniz.
# Cevap:




# Soru 6: Yüksek Değerli Satışları Ayıklama (filter)
# Cirosu (adet * fiyat) tek seferde 5.000 TL ve üzerinde olan "büyük satışları" 
# filter() ve lambda mimarisini kullanarak ayıklayıp listeleyiniz.
# Cevap:



# Soru 7: Kitap Kategorisindeki Ortalama Sepet Tutarını Bulma
# Kitap satışlarının performansını ölçmek için filter() ve map() (veya list comprehension) kullanarak 
# sadece "Kitap" kategorisindeki satışların cirolarını ayıklayın ve bu kategorinin ortalama satış tutarını hesaplayınız.
# Cevap:




# Soru 8: Müşteri Segmentasyonu Doğrulama Analizi (map & all/any)
# Premium müşterilerin harcamalarını analiz ediniz. Mağazadaki tüm Premium müşterilerin 
# tek seferde en az 1000 TL ve üzerinde harcama yapıp yapmadığını all() veya any() ile kontrol ediniz.
# Cevap:



# Soru 9: Müşteri Tipi ve Kategoriye Göre Pivot Analizi
# Çift filtreleme mantığı kullanarak, hem "Premium" müşteri tipi olan hem de "Elektronik" 
# kategorisinden yapılan alışverişlerin kümülatif toplam cirosunu bulunuz.
# Cevap:



# Soru 10: Kategori Bazlı Kümülatif Ciro Dağılımı (Sözlük Optimizasyonu)
# Döngü ve sözlük (dict) metotlarını (.get(), items()) harmanlayarak, hangi kategoriden 
# toplamda ne kadar ciro kazanıldığını gösteren dinamik bir özet tablo (sözlük) üretiniz.
# Cevap: