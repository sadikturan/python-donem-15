import pandas as pd

df = pd.read_csv("datasets/nba.csv")

# Soru 1: Veri setindeki ilk 10 satırı ekrana getirin.
print(df.head(10))

# Soru 2: Veri setinde toplam kaç satır ve kaç sütun olduğunu bulun.
print(df.shape)

# Soru 3: Tüm oyuncuları maaşlarına (Salary) göre büyükten küçüğe sıralayarak ilk 5 oyuncuyu listeleyin.
print(df.sort_values(by="Salary", ascending=False).head(5))

# Soru 4: Oyuncuları isimlerine (Name) göre alfabetik (A'dan Z'ye) olarak sıralayın.
print(df.sort_values(by="Name", ascending=True))

# Soru 5: Veri setindeki tüm oyuncuların yaş ortalaması kaçtır?
print(df["Age"].mean())

# Soru 6: Sadece "Los Angeles Lakers" takımında oynayan oyuncuları listeleyin.
print(df.loc[df["Team"] == "Los Angeles Lakers"])

# Soru 7: Yaşı 20'den küçük olan oyuncuların sadece isim, takım ve yaş bilgilerini getirin.
print(df.loc[df["Age"] < 20, ["Name", "Team", "Age"]])

# Soru 8: "Golden State Warriors" takımında oynayan ve pozisyonu "SG" (Shooting Guard) olan oyuncuları filtreleyin.
print(df.loc[(df["Team"] == "Golden State Warriors") & (df["Position"] == "SG")])

# Soru 9: "Kentucky" veya "Duke" üniversitelerinden mezun olan oyuncuları listeleyin.
# Amaç: Metinsel aramada .isin() veya | (VEYA) kullanımı.

print(df.loc[df["College"].isin(["Kentucky", "Duke"])])

# Soru 10: Maaşı 15 Milyon dolardan fazla olan veya yaşı 35'ten büyük olan oyuncuları bulun.
print(df.loc[(df["Salary"] > 15000000) | (df["Age"] > 35)])

# Soru 11: Hangi sütunda kaçar tane eksik veri (NaN) olduğunu bulun.
print(df.isna().sum())

# Soru 12: Üniversite (College) bilgisi boş olan satırları veri setinden tamamen silin (ana dataframe'i bozmadan yeni bir değişkene atayın).
df_kolejli = df.dropna(subset=["College"])

# Soru 13: İsminin içinde "James" kelimesi geçen oyuncuları filtreleyin.
print(df.loc[df["Name"].str.contains("James", case=False, na=False)])

# Soru 14: Oyuncuların kilolarını (Weight) gösteren sütunun en yüksek (Max) ve en düşük (Min) değerlerini bulun.
print("En Ağır:", df["Weight"].max(), "En Hafif:", df["Weight"].min())

# Soru 15: "Salary" sütunundaki boş (NaN) değerleri, tüm ligin maaş ortalaması ile doldurun.
maas_ortalamasi = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(maas_ortalamasi)

# Soru 16: Ligde kaç farklı takım (Team) vardır ve her takımda kaçar oyuncu oynamaktadır?
print(df["Team"].value_counts())

# Soru 17: Pozisyon bazında (Position) oyuncuların maaş ortalamalarını bulun.
print(df.groupby("Position")[["Salary"]].mean())

# Soru 18: Her takımın ödediği toplam maaş yükünü hesaplayıp, en çok harcama yapandan en aza doğru sıralayın.
print(df.groupby("Team")[["Salary"]].sum().sort_values(by="Salary", ascending=False))

# Soru 19: Takımlara göre gruplama yapıp, her takımın en yaşlı ve en genç oyuncusunun yaşını tek bir tabloda raporlayın.
print(df.groupby("Team")["Age"].agg(["min", "max"]))

# Soru 20: Her takımın en yüksek maaş alan oyuncusunun tüm bilgilerini getirin.
# Maaşı boş olanları eliyoruz
df_temiz = df.dropna(subset=["Salary"])

# En yüksek maaşların satır indekslerini buluyoruz
en_yuksek_indeksler = df_temiz.groupby("Team")["Salary"].idxmax()

# .loc ile satırları çekiyoruz
print(df_temiz.loc[en_yuksek_indeksler])

# Soru 21: Veri setindeki en yaşlı oyuncu kimdir ve kaç yaşındadır?
en_yasli = df.sort_values(by="Age", ascending=False).head(1)
print(en_yasli[["Name", "Age", "Team"]])

# Soru 22: "Boston Celtics" takımında oynayan tüm oyuncuların isim, pozisyon ve maaş bilgilerini getirin.
boston_oyunculari = df.loc[df["Team"] == "Boston Celtics", ["Name", "Position", "Salary"]].rename(
    columns={"Name":"İsim", "Position":"Pozisyon", "Salary":"Maaş"}
)
print(boston_oyunculari.dropna())   # dropna() NaN ları sil.

# Soru 23: Yaşı 25'ten küçük veya eşit olan PG (Point Guard) pozisyonundaki oyunculardan, maaşı 5 Milyon'dan fazla olanları listeleyin.
kriterler = (df["Age"] <= 25) & (df["Position"] == "PG") & (df["Salary"] > 5000000)
oyuncular = df.loc[kriterler, ["Name","Age","Position","Salary"]]
print(oyuncular)

# Soru 24: Üniversite (College) sütununda eksik veri (NaN) olan oyuncuların sayısını bulun ve bu oyuncuların ortalama maaşını hesaplayın.
# Üniversite bilgisi boş olanları süzüyoruz
kolejsizler = df.loc[df["College"].isna()]

print(f"Kolej bilgisi eksik oyuncu sayısı: {len(kolejsizler)}")
print(f"Bu oyuncuların ortalama maaşı: {kolejsizler['Salary'].mean():.2f}")

# Soru 25: Her takımdaki oyuncuların ortalama yaşını ve takıma ödenen toplam maaş yükünü bulun. Sonucu toplam maaşa göre büyükten küçüğe sıralayın.
takim_analizi = df.groupby("Team").agg({
    "Age": "mean",
    "Salary": "sum"
}).sort_values(by="Salary", ascending=False)

# print(takim_analizi)