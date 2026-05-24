# Tip Dönüşümüne Neden İhtiyaç Duyarız?
not1_sayi = 20
not2_sayi = 5
print(not1_sayi + not2_sayi)  # Toplama

not1_metin = "20"
not2_metin = "5"
print(not1_metin + not2_metin)  # Birleştirme (Concatenation)

# input() fonksiyonu ile dışarıdan veri alma.

sayi1 = input("sayi1: ")
sayi2 = input("sayi2: ")
print(sayi1 + sayi2)  # Birleştirme (Concatenation)

# Tip Dönüşümü (Type Casting)

sayi1 = int(input("sayi1: "))
sayi2 = int(input("sayi2: "))
print(sayi1 + sayi2)  # Toplama

# Diğer Tip Dönüşümleri
pi = 3.14
pi_int = int(pi)  # Ondalıklı sayıyı tam sayıya dönüştürme
print(pi_int)  # 3

not_metin = "85"
not_sayi = int(not_metin)  # Metni tam sayıya dönüştürme
print(not_sayi)  # 85

giris_yapti = True
giris_yapti_int = int(giris_yapti)  # Mantıksal değeri tam sayıya dönüştürme
print(giris_yapti_int)  # 1 (True değeri 1'e dönüşür, False değeri 0'a dönüşür)