# Neden Değişken Tanımlarız?

print(5500 + (5500 * 0.2))  # urun A
print(6000 + (6000 * 0.2))  # urun B
print(7000 + (7000 * 0.2))  # urun C

# Değişken Tanımlama

urunA = 5500
urunB = 6000
urunC = 7000

# urunA, urunB, urunC = 5500, 6000, 7000

kdv = 0.2

print(urunA + (urunA * kdv))
print(urunB + (urunB * kdv))
print(urunC + (urunC * kdv))

urunA = 8000    # urunA'nın fiyatını güncelledik

print(urunA + (urunA * kdv))