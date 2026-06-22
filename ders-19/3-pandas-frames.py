import pandas as pd

# =============================================================================
# 1. PANDAS SERİLERİNİ BİRLEŞTİREREK DATAFRAME OLUŞTURMA
# =============================================================================
s1 = pd.Series([1, 3, 4, 6])
s2 = pd.Series([0, 5, 8, 6])

# Serileri bir sözlüğe (dict) anahtar isimleriyle vererek kolonlaştırıyoruz
data = dict(apples=s1, oranges=s2)
df = pd.DataFrame(data)
# print(df)

# =============================================================================
# 2. LİSTELERDEN (ARRAY) DATAFRAME OLUŞTURMA VARYASYONLARI
# =============================================================================

df = pd.DataFrame()  # Boş bir DataFrame matrisi açar.

df = pd.DataFrame([1, 2, 3, 4])  # Tek boyutlu listeden tek sütunlu DataFrame üretir.

# İç içe geçmiş (2D) matris listesinden, sütun isimlerini (columns) belirterek üretme:
df = pd.DataFrame(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], columns=["a", "b", "c", "d"]
)

# Kayıt (Satır) tabanlı listelerden DataFrame üretme:
list_data = [["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]]
df = pd.DataFrame(list_data, columns=["İsim", "Puan"])

# Kayıt tabanlı listeden üretirken satır indekslerini (index) özelleştirme:
df = pd.DataFrame(list_data, columns=["İsim", "Puan"], index=[1, 2, 3, 4])


# =============================================================================
# 3. SÖZLÜKLERDEN (DICTIONARY) SÜTUN TABANLI DATAFRAME OLUŞTURMA
# =============================================================================
# Sözlük yapısında Key'ler doğrudan "Sütun İsimleri", Value'lar ise "Sütun Verileri" olur.
# NOT: Verilen listelerin eleman sayılarının (uzunluklarının) eşit olması zorunludur!
dict_data = {"İsim": ["Ahmet", "Ali", "Yağmur", "Çınar"], "Puan": [50, 60, 70, 80]}
df = pd.DataFrame(dict_data)


# =============================================================================
# 4. SÖZLÜK LİSTELERİNDEN (LIST OF DICTS) SATIR TABANLI DATAFRAME OLUŞTURMA
# =============================================================================
# NoSQL veritabanlarından (MongoDB) veya API'lerden (JSON) gelen kurumsal veriler genellikle bu formattadır.
# Her bir sözlük bir "Satırı (Record)" temsil eder, anahtarlar ise kolon eşleşmesini sağlar.
dict_list = [
    {"İsim": "Ahmet", "Puan": 50},
    {"İsim": "Ali", "Puan": 60},
    {"İsim": "Yağmur", "Puan": 70},
    {"İsim": "Çınar", "Puan": 80},
]

df = pd.DataFrame(dict_list)  # Varsayılan olarak 0, 1, 2, 3 indeksleriyle oluşturur.

# Satır etiketlerini kurumsal ID'ler veya özel indekslerle maskeleme:
df = pd.DataFrame(dict_list, index=[100, 101, 102, 103])

print(df)