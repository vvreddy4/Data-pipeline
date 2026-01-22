import pandas as pd

df = pd.read_csv("data/raw_jobs.csv")

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df.to_csv("data/cleaned_jobs.csv", index=False)

print("Data cleaned successfully")
