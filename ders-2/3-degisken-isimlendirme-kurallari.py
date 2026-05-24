# Değişken Tanımlama Kuralları

# 1- Sayı ile başlayamaz

# 1sayi => yanlış
# sayi1 => doğru

# 2- Boşluk İçeremez

# urun fiyati = 500 => yanlış
# urun_fiyati = 500 => doğru

# 3- Özel Karakterler Yasaktır: Alt çizgi (_) dışında hiçbir işaret ( @, $, %, !, +, - ) kullanılamaz.

# maas+bonus = 20000 => yanlış
# maas_bonus = 20000 => doğru

# 4- Anahtar Kelimeler Kullanılamaz: Python'ın kendi komutlarını isim olarak seçemezsiniz.

# if = 5, class = "A Sınıfı", import = "veriler" => yanlış
# if_durumu = 5, sinif_adi = "A Sınıfı"          => doğru

# 5- Büyük Küçük Harf Duyarlılığı: Python'da büyük ve küçük harfler farklı değişkenler olarak kabul edilir.

# model = "Tesla"
# Model = "BMW"
# MODEL = "Audi"

# Bunların hepsi bellekte farklı kutularda tutulur.

# 6- Anlamlı İsimler Kullanmak: Değişken isimleri, içerdikleri veriyi veya temsil ettikleri kavramı açıkça ifade etmelidir.

# Kötü İsimlendirme (Kod çalışır ama kimse anlamaz)
a = "Domates"
b = 15
c = 20
d = b * c

# İyi İsimlendirme (Okunduğunda ne olduğu bellidir)
urun_adi = "Domates"
birim_fiyat = 15
miktar = 20
toplam_tutar = birim_fiyat * miktar