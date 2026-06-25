import pandas as pd

df = pd.read_csv("datasets/imdb.csv")

# 1- Puanı 8.5'ten büyük olan satırları filtreliyoruz
efsane_filmler = df[df["Rating"] >= 8.5]
print(efsane_filmler[["Movie_Title", "Rating"]].head())


# 2- 90'lar sinemasını (1990 - 1999 arası) süzüp getirelim:

doksanlar_sinemasi = df[(df["YR_Released"] >= 1990) & (df["YR_Released"] <= 1999)]
print(doksanlar_sinemasi[["Movie_Title", "YR_Released"]].head())

# 3- Film isminin içinde "The" veya "Star" gibi özel kelimeler geçen yapımları cımbızlayalım:
# Büyük/küçük harf duyarlılığını kapatmak için case=False yapıyoruz.
# na: Not Available, Not Applicable

maske = df["Movie_Title"].str.contains("Star|Wars|Trek", case=False, na=False)
star_filmleri = df[maske]
print(star_filmleri[["Movie_Title", "YR_Released"]].head(20))

# And operatörü için
maske1 = df["Movie_Title"].str.contains("Star", case=False, na=False)
maske2 = df["Movie_Title"].str.contains("Wars", case=False, na=False)

star_wars_filmleri = df[maske1 & maske2]
print(star_wars_filmleri[["Movie_Title", "YR_Released"]].head(3))

# 4- Veri setindeki Record sütununda birden fazla kategorik etiket bulunuyor. Sadece "Top 250 Movies" veya "Bottom 250 Movies" listesindeki uç örnekleri bir arada süzmek isteyelim:

maske = (df["Record"] == "Top 250 Movies") | (df["Record"] == "Bottom 250 Movies")
uc_ornekler = df[maske]
print(uc_ornekler["Record"].value_counts())


# Süresi 180 dakikadan (3 saatten) uzun olan filmleri bulalım ama bize tüm tablo gelmesin; sadece Film Adı ve Süresi kolonları dönsün.

uzun_filmler = df[df["Runtime"] >= 180][["Movie_Title", "Runtime"]]
print(uzun_filmler.head())

# # .loc[satir_şartı , sutun_listesi]
uzun_filmler = df.loc[df["Runtime"] > 180, ["Movie_Title", "Runtime"]]
print(uzun_filmler.head())

# Puanı 8.0 den büyük olan filmleri süzün, sadece film başlığı ve inceleme sayısını alın, ardından en çok inceleme alan ilk 5 filmi yakalamak için sıralama zincirine bağlayın:

zincir_sonuc = df[df["Rating"] >= 8.0][["Movie_Title", "Num_Reviews"]].sort_values(by="Num_Reviews", ascending=False).head(5)
print(zincir_sonuc)

zincir_sonuc = df.loc[df["Rating"] >= 8.0, ["Movie_Title", "Num_Reviews"]].sort_values(by="Num_Reviews", ascending=False).head(5)
print(zincir_sonuc)

# 2000 yılından sonra çekilmiş, IMDB puanı 8.2'den büyük olan ve toplam inceleme sayısı (Num_Reviews) 500 binden fazla olan popüler modern başyapıtları sorgulayalım.

modern_populer = df.loc[(df["YR_Released"] > 2000) & (df["Rating"] >= 8.2) & (df["Num_Reviews"] > 500000), 
                    ["Movie_Title", "Rating", "Num_Reviews"]
]

print(modern_populer.head())

modern_populer = df.query("YR_Released > 2000 & Rating >= 8.2 & Num_Reviews > 500000")[["Movie_Title", "Rating", "Num_Reviews"]]
print(modern_populer.head())

# or kullanımı
modern_veya_populer = df.loc[(df["YR_Released"] > 2000) | (df["Rating"] >= 8.2) & (df["Num_Reviews"] > 500000),
    ["Movie_Title", "Rating", "Num_Reviews"]
]
print(modern_veya_populer.head())

# Kodun içinde dinamik bir sınır yılı tuttuğumuzu varsayalım. Bu değişkeni sorgunun içine güvenle göndermek için önüne @ sembolü ekleriz:

sinir_yili = 1975

eski_klasikler = df.query("YR_Released < @sinir_yili & Rating > 8.5")
print(eski_klasikler[["Movie_Title", "YR_Released", "Rating"]])