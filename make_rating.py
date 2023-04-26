import pandas as pd
from datetime import datetime

df = pd.read_csv("merged_file.csv")

df_orig = df.copy()

df["Date of release"] = pd.to_datetime(df["Date of release"], format="%m/%Y")

current_year = datetime.now().year

df["Rating"] = (df["Rating"] - df["Rating"].min()) / (
    df["Rating"].max() - df["Rating"].min()
)
df["Amount of ratings"] = (df["Amount of ratings"] - df["Amount of ratings"].min()) / (
    df["Amount of ratings"].max() - df["Amount of ratings"].min()
)

df["Rating Score"] = (
    df["Rating"]
    + df["Amount of ratings"]
    + ((current_year - df["Date of release"].dt.year) / 100)
)

df = df.sort_values(by="Rating Score", ascending=False).head(150)

df = df.reset_index(drop=True)
df.index += 1

df["Rating"] = df_orig["Rating"]
df["Amount of ratings"] = df_orig["Amount of ratings"]

df.to_csv("rating150.csv", index_label="ID")
