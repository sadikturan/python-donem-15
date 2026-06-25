import pandas as pd

# 1. ADIM: IMDB verisetini yüklüyoruz
df = pd.read_csv("datasets/imdb.csv")

# sonuc = df

# KOLON SEÇME İŞLEMLERİ

sonuc = df["Movie_Title"]
sonuc = type(df["Movie_Title"])                      # Çıktı: <class 'pandas.core.series.Series'>
sonuc = df[["Movie_Title", "YR_Released", "Rating"]] # Çıktı: İki boyutlu DataFrame

# SATIR SEÇME İŞLEMLERİ

sonuc = df.iloc[5]
sonuc = df.iloc[5:7]
sonuc = df.iloc[[5,7,10]]

# SATIR VE SÜTUNU AYNI ANDA DİLİMLEME

sonuc = df.loc[:, "Movie_Title"]
sonuc = df.loc[:, ["Movie_Title", "YR_Released"]]

sonuc = df.loc[:, "Movie_Title":"Rating"]
sonuc = df.loc[:, :"Rating"]

sonuc = df.loc[5:7, "Movie_Title"]
sonuc = df.loc[:10, ["Movie_Title", "YR_Released"]]

# kayıt seçme

sonuc = df["Movie_Title"].head(10)
sonuc = df["Movie_Title"].tail(10)

sonuc = df["Movie_Title"].shift(10).head(20)
sonuc = sonuc = df["Movie_Title"].iloc[10:20]

print(sonuc)
