# 1. Aritmetik Operatörler (Matematiksel İşlemler)

print(10 + 5)  # Toplama
print(10 - 5)  # Çıkarma
print(10 * 5)  # Çarpma
print(10 / 5)  # Bölme
print(10 // 3)  # Tam Bölme
print(10 % 3)  # Mod (Kalan)
print(10 ** 2)  # Üs Alma

# 2. Karşılaştırma Operatörleri (Karşılaştırma İşlemleri)
print(10 == 5)  # Eşit mi?
print(10 != 5)  # Eşit değil mi?
print(10 > 5)   # Büyük mü?
print(10 < 5)   # Küçük mü?
print(10 >= 5)  # Büyük veya eşit mi?
print(10 <= 5)  # Küçük veya eşit mi?

# 3. Atama Operatörleri (Değer Atama)
x = 10
x += 5  # x = x + 5
x -= 3  # x = x - 3
x *= 2  # x = x * 2
x /= 4  # x = x / 4
x //= 2  # x = x // 2
x %= 3  # x = x % 3
x **= 2  # x = x ** 2
print(x)

# 4. Mantıksal Operatörler (Mantıksal İşlemler)
print(True and False)  # Ve (AND)
print(True or False)   # Veya (OR)
print(not True)        # Değil (NOT)

# Parola kontrolü
username = "sadikturan"
password = "12345"

isLoggedIn = username == "sadikturan" and password == "12345"
print(isLoggedIn)

# Kullanıcının sepet tutarı 500 TL'den büyük olmalı VEYA kullanıcı "Premium" üye olmalı.

sepet_tutari = 600
kullanici_uyelik = "Premium"
indirim_kazandi_mi = (sepet_tutari > 500) or (kullanici_uyelik == "Premium")
print(indirim_kazandi_mi)  # True

