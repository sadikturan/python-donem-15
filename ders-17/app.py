from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
# options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")  # Disable GPU acceleration
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/")

# driver = webdriver.Chrome(options=options)
# driver.get("https://www.amazon.com.tr")

# time.sleep(3)

# arama_kutusu = driver.find_element(By.ID, "twotabsearchtextbox")
# arama_kutusu.send_keys("iphone 17 pro max" + Keys.ENTER)

# 1- Tek ürün alma.

# urun = driver.find_element(By.CSS_SELECTOR, "div[role='listitem']")

# urun_ismi = urun.find_element(By.CSS_SELECTOR, "h2 span").text
# fiyat_metin = urun.find_element(By.CLASS_NAME, "a-price-whole").text
# sayisal_fiyat = float(fiyat_metin.replace(".", "").replace(",", "."))
# link = urun.find_element(By.CLASS_NAME, "a-link-normal").get_attribute("href")


# print(urun_ismi)
# print(fiyat_metin)
# print(sayisal_fiyat)
# print(link)

# 2- Çoklu ürün alma.

# urunler = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")

# for urun in urunler:
#     try:
#         urun_ismi = urun.find_element(By.CSS_SELECTOR, "h2 span").text
#         fiyat_metin = urun.find_element(By.CLASS_NAME, "a-price-whole").text
#         sayisal_fiyat = float(fiyat_metin.replace(".", "").replace(",", "."))
#         link = urun.find_element(By.CLASS_NAME, "a-link-normal").get_attribute("href")

#         print(urun_ismi)
#         print(fiyat_metin)
#         print(sayisal_fiyat)
#         print(link)

#         print("*" * 20)
#     except:
#         continue


# 3- Filtreleme

# MIN_FIYAT = 100000
# MAX_FIYAT = 160000

# urunler = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")

# for urun in urunler:
#     try:
#         urun_ismi = urun.find_element(By.CSS_SELECTOR, "h2 span").text
#         fiyat_metin = urun.find_element(By.CLASS_NAME, "a-price-whole").text
#         sayisal_fiyat = float(fiyat_metin.replace(".", "").replace(",", "."))
#         link = urun.find_element(By.CLASS_NAME, "a-link-normal").get_attribute("href")

#         if "17 pro max" in urun_ismi.lower() and MIN_FIYAT <= sayisal_fiyat <= MAX_FIYAT and "kılıf" not in urun_ismi.lower():
#             urunler.append({"isim": urun_ismi, "fiyat": sayisal_fiyat , "link": link})
#             print(f"Uygun ürün bulundu: {urun_ismi[:40]}... - Fiyat: {sayisal_fiyat} TL")

#             print("*" * 20)
#     except:
#         continue


# 4- Kontrol aralığı

# while True:

#     driver = webdriver.Chrome(options=options)
#     driver.get("https://www.amazon.com.tr")

#     time.sleep(3)

#     arama_kutusu = driver.find_element(By.ID, "twotabsearchtextbox")
#     arama_kutusu.send_keys("iphone 17 pro max" + Keys.ENTER)

#     MIN_FIYAT = 100000
#     MAX_FIYAT = 160000
#     KONTROL_ARALIGI = 60 * 1  # 10 dakika

#     urunler = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")

#     for urun in urunler:
#         try:
#             urun_ismi = urun.find_element(By.CSS_SELECTOR, "h2 span").text
#             fiyat_metin = urun.find_element(By.CLASS_NAME, "a-price-whole").text
#             sayisal_fiyat = float(fiyat_metin.replace(".", "").replace(",", "."))
#             link = urun.find_element(By.CLASS_NAME, "a-link-normal").get_attribute("href")

#             if "17 pro max" in urun_ismi.lower() and MIN_FIYAT <= sayisal_fiyat <= MAX_FIYAT and "kılıf" not in urun_ismi.lower():
#                 urunler.append({"isim": urun_ismi, "fiyat": sayisal_fiyat , "link": link})
#                 print(f"Uygun ürün bulundu: {urun_ismi[:40]}... - Fiyat: {sayisal_fiyat} TL")

#                 print("*" * 20)
#         except:
#             continue

#     driver.quit()

#     time.sleep(KONTROL_ARALIGI)

# 5- Verilerin Kayıt Edilmesi

from datetime import datetime
import csv

def veriyi_kaydet(urun_listesi):
    dosya_adi = "fiyat_takip.csv"
    tarih_saat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(dosya_adi, "a", encoding="utf-8") as dosya:
        yazici = csv.writer(dosya)

        if dosya.tell() == 0:  # Dosya boşsa başlık ekle
            yazici.writerow(["Tarih/Saat", "Ürün İsmi", "Fiyat", "Link"])

        for urun in urun_listesi:
            yazici.writerow([tarih_saat, urun["isim"], urun["fiyat"], urun["link"]])

while True:

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amazon.com.tr")

    time.sleep(3)

    arama_kutusu = driver.find_element(By.ID, "twotabsearchtextbox")
    arama_kutusu.send_keys("iphone 17 pro max" + Keys.ENTER)

    MIN_FIYAT = 100000
    MAX_FIYAT = 160000
    KONTROL_ARALIGI = 10  # 10 saniye

    urunler = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")

    bulunan_urunler = []

    for urun in urunler:
        try:
            urun_ismi = urun.find_element(By.CSS_SELECTOR, "h2 span").text
            fiyat_metin = urun.find_element(By.CLASS_NAME, "a-price-whole").text
            sayisal_fiyat = float(fiyat_metin.replace(".", "").replace(",", "."))
            link = urun.find_element(By.CLASS_NAME, "a-link-normal").get_attribute("href")

            if "17 pro max" in urun_ismi.lower() and MIN_FIYAT <= sayisal_fiyat <= MAX_FIYAT and "kılıf" not in urun_ismi.lower():
                bulunan_urunler.append({"isim": urun_ismi, "fiyat": sayisal_fiyat , "link": link})
                print(f"Uygun ürün bulundu: {urun_ismi[:40]}... - Fiyat: {sayisal_fiyat} TL")

                print("*" * 20)
        except:
            continue

    if bulunan_urunler:
        veriyi_kaydet(bulunan_urunler)
        en_ucuz = min(bulunan_urunler, key=lambda x: x["fiyat"])
        print(f"En ucuz ürün: {en_ucuz['isim']} - Fiyat: {en_ucuz['fiyat']} TL")
    else:
        print("Ürün bulunamadı.")

    driver.quit()

    time.sleep(KONTROL_ARALIGI)