from bs4 import BeautifulSoup

with open("kaynak.html", encoding="utf-8") as file:
    ham_html = file.read()

soup = BeautifulSoup(ham_html, "html.parser")

# id, class, select

sonuc = soup.div
sonuc = soup.find("div")

sonuc = soup.find(id="div1")
sonuc = soup.find("div", id="div2")

sonuc = soup.find(class_="grup1")
sonuc = soup.find("div", class_="grup3")
sonuc = soup.find_all(class_="bolum")

sonuc = soup.div.attrs
sonuc = soup.div.attrs["class"]

sonuc = soup.find("img", attrs={"src": "1.jpg"})
sonuc = soup.find("a", attrs={"href": "python.html"})

print(sonuc)