from bs4 import BeautifulSoup

with open("kaynak.html", encoding="utf-8") as file:
    ham_html = file.read()

soup = BeautifulSoup(ham_html, "html.parser")

sonuc = soup.div
sonuc = soup.find("div")
sonuc = soup.find_all("div")
sonuc = len(soup.find_all("div"))

sonuc = soup.find_all("div")[0].ul.li
sonuc = soup.find_all("div")[0].ul.find_all("li")[1]

for div in soup.find_all("div"):
    # div.h2.a ifadesi h2'nin içinde <a> etiketi var mı diye bakar
    if div.h2.a != None:
        # Link varsa içindeki metni çek
        print(f"Bağlantılı Başlık: {div.h2.a.string.strip()}")
    else:
        # Link yoksa (None ise) h2'nin kendi metnini çek
        print(f"Düz Metin Başlık : {div.h2.string.strip()}")


for a in soup.find_all("a"):
    link_metni = a.string
    link_adresi = a["href"] # Sözlük mantığıyla href niteliğini söküyoruz
    print(f"Yazı: {link_metni:<15} | Gittiği Adres: {link_adresi}")


# print(sonuc)