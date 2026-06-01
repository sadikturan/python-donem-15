# 1- Neden Listeleri Kullanırız?

ogrenci1 = "Ahmet"
ogrenci2 = "Mehmet"
ogrenci3 = "Ayşe"

# 2- Listeler Nasıl Oluşturulur?

# Basit bir liste
meyveler = ["Elma", "Armut", "Muz", "Çilek"]

# Farklı veri tiplerinden oluşan bir liste
kullanici = ["Ahmet", 25, True, 85.5]

# Boş bir liste tanımlama
bos_liste = []

# İç içe listeler (nested lists)
ogrenciler = [["ali",20],["ahmet",22]]

# listeAli = ["ali",20]
# listeAhmet = ["ahmet",22]
# ogrenciler = [listeAli,listeAhmet]

# 3- Liste Öğelerine Erişme (Indexing)

renkler = ["Kırmızı", "Mavi", "Yeşil", "Sarı"]

print(renkler[0])   # "Kırmızı" (İlk eleman)
print(renkler[2])   # "Yeşil"
print(renkler[-1])  # "Sarı" (En sondaki eleman)

# 4- Liste Öğelerini Değiştirme

arabalar = ["Tesla", "BMW", "Audi"]
arabalar[1] = "Mercedes" # BMW yerine Mercedes geldi

print(arabalar) # ["Tesla", "Mercedes", "Audi"]

# 5- Liste Eleman Silme
sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa"]
del sehirler[2] # İzmir silindi
print(sehirler) # ["İstanbul", "Ankara", "Bursa"]

