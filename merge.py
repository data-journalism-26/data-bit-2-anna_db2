
import pandas as pd
import io

df_prize = pd.read_csv("data/prize_money.csv")
df_wiki  = pd.read_csv("data/wikipedia_views.csv")

instagram_raw = """name,instagram
Aryna Sabalenka,5100000
Elena Rybakina,882000
Iga Świątek,2300000
Coco Gauff,2300000
Jessica Pegula,357000
Amanda Anisimova,491000
Mirra Andreeva,525000
Jasmine Paolini,697000
Victoria Mboko,162000
Elina Svitolina,1700000
Karolina Muchova,222000
Belinda Bencic,442000
Linda Noskova,45200
Ekaterina Alexandrova,46300
Marta Kostyuk,543000
Naomi Osaka,2900000
Iva Jovic,225000
Clara Tauson,51400
Madison Keys,353000
Diana Shnaider,32300"""

df_insta = pd.read_csv(io.StringIO(instagram_raw))

df_prize = df_prize[["name", "prize_money_usd"]].rename(
    columns={"prize_money_usd": "earnings"}
)

df_wiki = df_wiki[["name", "ranking", "views_total"]].rename(
    columns={"views_total": "wiki_views"}
)

df = df_wiki \
    .merge(df_prize, on="name", how="left") \
    .merge(df_insta, on="name", how="left")

df = df.sort_values("ranking").reset_index(drop=True)

df = df[["name", "ranking", "earnings", "wiki_views", "instagram"]]


missing = df[df.isnull().any(axis=1)]


df.to_csv("data/wta_final.csv", index=False)

print(df.to_string(index=False))

