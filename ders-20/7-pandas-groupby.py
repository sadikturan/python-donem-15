import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)

sonuc = df
sonuc = df["Maaş"].sum()
sonuc = df["Maaş"].mean()

sonuc = df.groupby("Departman").groups
sonuc = df.groupby(["Departman","Semt"]).groups


# print("***********Semtlere göre*********")
# semtler = df.groupby("Semt")
# for name, group in semtler:
#     print(name)
#     print(group)


# print("**************Departmanlara göre************")
# departmanlar = df.groupby("Departman")

# for name, group in departmanlar:
#     print(name)
#     print(group)

# print("**************Departman ve semtlere göre************")

# departman_semt = df.groupby(["Departman","Semt"])

# for name, group in departman_semt:
#     print(name)
#     print(group)


sonuc = df.groupby("Semt").get_group("Kadıköy")
sonuc = df.groupby("Departman").get_group("Muhasebe")

# Tüm departmanları otomatik olarak ayrı tablolara böler
departman_tablolari = {isim: grup for isim, grup in df.groupby("Departman")}

# Doğrudan erişim:
print(departman_tablolari["Muhasebe"])
print(departman_tablolari["Bilgi İşlem"])

# Oluşturduğunuz sözlüğün sadece anahtarlarını (isimlerini) alır
sadece_isimler = list(departman_tablolari.keys())

# Matematiksel işlemler

sonuc = df.groupby("Departman")[["Yaş","Maaş"]].sum()
sonuc = df.groupby("Departman")[["Yaş","Maaş"]].mean()

sonuc = df.groupby("Semt")["Çalışan"].count()
sonuc = df.groupby("Departman")["Yaş"].max()
sonuc = df.groupby("Departman").get_group("Muhasebe")["Yaş"].max()

sonuc = df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.max, np.min])
sonuc = df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.max, np.min]).loc["Muhasebe"]


print(sonuc)