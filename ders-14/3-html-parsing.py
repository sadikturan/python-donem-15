
# İlk HTML'i Hazırlamak (Parsing)

# Kütüphaneyi kodumuza dahil ederken bs4 paketinin içerisinden BeautifulSoup sınıfını çağırırız.

# BeautifulSoup'un temel görevi, kendisine verdiğimiz ham HTML metnini parçalara ayırarak (parsing) üzerinde kolayca arama yapabileceğimiz düzenli bir nesne ağacına dönüştürmektir.

# Gelin, elimizde ham bir HTML metni varmış gibi simüle ederek ilk ayıklama işlemimizi yapalım:

from bs4 import BeautifulSoup

# Bilgisayarımıza inmiş ham bir HTML metni senaryosu
# ham_html = """
# <html>
#     <head><title>Teknoloji Dünyası</title></head>
#     <body>
#         <h1 id="ana-baslik">Yapay Zeka ve Python</h1>
#         <p class="ozet-yazi">Yapay zeka modelleri arka planda veri analitiği kullanır.</p>
#         <p class="icerik-yazi">NumPy ve Pandas bu sürecin en önemli yapı taşlarıdır.</p>
#         <a href="https://www.python.org" class="kaynak-link">Resmi Web Sitesi</a>
#     </body>
# </html>
# """

with open("kaynak.html", encoding="utf-8") as file:
    ham_html = file.read()

# 1. Ham HTML metnini BeautifulSoup havuzuna bırakıp anlamlandırıyoruz
soup = BeautifulSoup(ham_html, "html.parser")

sonuc = soup
sonuc = soup.prettify()
sonuc = type(soup)
sonuc = soup.title
sonuc = type(soup.title)
sonuc = soup.title.name
sonuc = soup.title.text

sonuc = soup.body
sonuc = soup.body.h1
sonuc = soup.body.h1.name
sonuc = soup.body.h1.string

sonuc = soup.div
sonuc = soup.h2
sonuc = soup.ul
sonuc = soup.ul.li


print(sonuc)
