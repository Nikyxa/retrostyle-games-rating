import pandas as pd

df1 = pd.read_csv("metacritic.csv")

df2 = pd.read_csv("steam.csv")

merged_df = pd.concat([df1, df2]).drop_duplicates(subset=["Date of release"])

merged_df.to_csv("merged_file.csv", index=False)
