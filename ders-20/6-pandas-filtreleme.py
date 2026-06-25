import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns=["Column1","Column2","Column3","Column4","Column5"])

print(df)
print("*"*50)

sonuc = df
sonuc = df.columns
sonuc = df.head()
sonuc = df.head(10)
sonuc = df.tail()
sonuc = df.tail(10)
sonuc = df["Column1"].head(10)
sonuc = df.Column1.head(10)

sonuc = df[["Column1","Column2"]].head()
sonuc = df[["Column1","Column2"]].tail(10)

sonuc = df[5:15][["Column1","Column2"]].tail(10)
sonuc = df.loc[5:14, ["Column1", "Column2"]] # üstekinin profesyonel alternatifi.

sonuc = df > 50
sonuc = df[df > 50]
sonuc = df[df % 2 == 0]

sonuc = df["Column1"] > 50
sonuc = df[df["Column1"] > 50]
sonuc = df[df["Column1"] > 50][["Column1","Column2"]]

sonuc = df[(df["Column1"] > 20) & (df["Column1"] <=70)][["Column1","Column2"]]
sonuc = df[(df["Column1"] > 50) | (df["Column2"] > 50)][["Column1","Column2"]]

sonuc = df.query("Column1 > 50 & Column1 % 2 == 0")
sonuc = df.query("Column1 > 50 & Column1 % 2 == 0")[["Column1","Column2"]]
sonuc = df.query("Column1 > 50 | Column1 % 2 == 0")[["Column1","Column2"]]


print(sonuc)