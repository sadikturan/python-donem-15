import numpy as np
import pandas as pd

# 0- Rastgele Veri ve DataFrame Kurulumu
# 1 ile 100 arasında (100 hariç) 3x3 boyutunda tam sayılardan oluşan matris üretimi
random_data = np.random.randint(1, 100, size=(3, 3))

df = pd.DataFrame(random_data, index=["A","B","C"], columns=["column1","column2","column3"])

sonuc = df
sonuc = df["column1"]
sonuc = df[["column1","column3"]]

# 2. SATIR SEÇME

sonuc = df.loc["A"]
sonuc = df.loc["A":"B"]
sonuc = df.iloc[2]
sonuc = df.iloc[0:2]

# # SATIR VE SÜTUNU AYNI ANDA DİLİMLEME

# sonuc = df.loc[:, "column1"]
# sonuc = df.loc[:, ["column1", "column2"]]
# sonuc = df.loc[:, "column1":"column3"]
# sonuc = df.loc[:, :"column3"]

# # SATIR ODAKLI SEÇİMLER 

# sonuc = df.loc["A":"C", :"column2"]
# sonuc = df.loc[:"C", :"column2"]
# sonuc = df.loc["A":"C", :]

# # Standart Parantez Slicing İstisnası:

# sonuc = df[1:3]  # 1. indeksten başlar, 3. indekse kadar olan (3 hariç, yani B ve C) satırlarını süzebilir.

# # SATIR - SÜTUN KESİŞİMLERİ (NOKTA ATIŞI HÜCRE SEÇİMİ)

# sonuc = df.loc["A", "column2"]
# sonuc = df.loc[["A", "B"], "column2"]
# sonuc = df.loc[["A", "B"], ["column1", "column2"]]


print(sonuc)

