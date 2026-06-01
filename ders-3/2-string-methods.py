msg = "Python Kursumuza Hoş Geldiniz. Ben Sadık Turan"

# sonuc = len(msg)
# sonuc = msg.upper()
# sonuc = msg.lower()
# sonuc = msg.title()
# sonuc = msg.capitalize()

# sonuc = "abc".islower()

# sonuc = "    abc ".strip()
sonuc = msg.split()   # msg.split(' ') da olabilir, default olarak boşluk karakterine göre böler.
# sonuc = msg.split('.')

sonuc = "-".join(sonuc) # sonuc = " ".join(sonuc) # split ile bölünen parçaları tekrar birleştirir.

# index = msg.index('Hoş')
# sonuc = msg.startswith('A')
# sonuc = msg.endswith('n')

# sonuc = msg.replace('Sadık','Çınar')
# sonuc = msg.lower().replace(' ','-').replace('ş','s').replace('.','').replace('ı','i')


print(sonuc)