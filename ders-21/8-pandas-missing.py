import numpy as np
import pandas as pd

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index=["a","c","d","f","h"], columns=["column1","column2","column3"])

df = df.reindex(["a","b","c","d","e","f","g","h"])

sonuc = df

sonuc = df.drop("column1", axis = 1)
sonuc = df.drop(["column1","column2"], axis = 1)

sonuc = df.drop("a", axis = 0)
sonuc = df.drop(["a","b"], axis = 0)

sonuc = df.isnull()     # NaN olan yerler "True" getirir.
sonuc = df.notnull()    # NaN olmayan yerler "True" getirir.

# null değerleri sayma
sonuc = df.isnull().sum()
sonuc = df["column1"].isnull().sum()

# yeni kolon ekleme
df["column4"] = [np.nan,30,np.nan,50,np.nan,np.nan,10,20]

print(df)

sonuc = df["column1"].isnull().sum()
sonuc = df["column1"].isnull()

sonuc = df[df["column1"].isnull()]
sonuc = df[df["column1"].isnull()]["column1"]
sonuc = df[df["column1"].notnull()]["column1"]
sonuc = df[df["column1"].notnull()]

# null içerenleri siler.
sonuc = df.dropna()         # axis=0 => satıra göre
sonuc = df.dropna(axis=1)   # axis=1 => sütuna göre

sonuc = df.dropna(how="any")   # her hangi bir na bulursa satırı siler.
sonuc = df.dropna(how="all")   # tüm satır na ise satırı siler.

sonuc = df.dropna(subset=["column1","column2"], how="all")   #  bakacağı kolonları belirttik
sonuc = df.dropna(subset=["column1","column2"], how="any")   #  bakacağı kolonları belirttik

sonuc = df.dropna(thresh=2) # en az 2 dolu değer varsa kaydı silme
sonuc = df.dropna(thresh=3) # en az 3 dolu değer varsa kaydı silme

sonuc = df.fillna(value="no input") # na alanlara veri ataması yapar.
sonuc = df.fillna(value=1)


# Uygulama

toplam = df.sum().sum()
adet = df.size
null_toplam = df.isnull().sum().sum()
gecerli_deger_adet = adet - null_toplam

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

sonuc = df.fillna(value = ortalama(df))


print(sonuc)