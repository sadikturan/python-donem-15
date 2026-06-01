# 1- Liste Uzunluğu
hayvanlar = ["Kedi", "Köpek", "Kuş", "Balık"]
print(len(hayvanlar)) # 4

# 2- append() - Listeye eleman ekler
hayvanlar.append("Tavşan")
print(hayvanlar) # ["Kedi", "Köpek", "Kuş", "Balık", "Tavşan"]

# 3- insert() - Belirli bir konuma eleman ekler
hayvanlar.insert(1, "At") # 1. indexe At eklendi
print(hayvanlar) # ["Kedi", "At", "Köpek", "Kuş", "Balık", "Tavşan"]

# 4- remove() - Belirli bir elemanı siler
hayvanlar.remove("Köpek")
print(hayvanlar) # ["Kedi", "At", "Kuş", "Balık", "Tavşan"]

# 5- pop() - Belirli bir konumdaki elemanı siler ve döndürür
cikarilan = hayvanlar.pop(2) # 2. indexteki Kuş silindi ve cikarilan değişkenine atandı
print(cikarilan) # "Kuş"

# 6- clear() - Tüm elemanları siler
hayvanlar.clear()
print(hayvanlar) # []

# 7- index() - Belirli bir elemanın indexini döndürür
meyveler = ["Elma", "Armut", "Muz", "Çilek"]
print(meyveler.index("Muz")) # 2

# 8- count() - Belirli bir elemanın kaç kez geçtiğini sayar
meyveler.append("Elma")
print(meyveler.count("Elma")) # 2

# 9- sort() - Liste elemanlarını sıralar
sayilar = [5, 2, 9, 1, 3]
sayilar.sort()
print(sayilar) # [1, 2, 3, 5, 9]

# 10- reverse() - Liste elemanlarının sırasını tersine çevirir
sayilar.reverse()
print(sayilar) # [9, 5, 3, 2, 1]

# 11- copy() - Listenin bir kopyasını oluşturur
orjinal = ["A", "B", "C"]
kopya = orjinal.copy()
print(kopya) # ["A", "B", "C"]



