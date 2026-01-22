import requests
import pandas as pd
from datetime import datetime

url = "https://remoteok.com/api"

response = requests.get(url)
data = response.json()[1:]

jobs = []
for job in data[:20]:
    jobs.append({
        "title": job.get("position"),
        "company": job.get("company"),
        "location": job.get("location"),
        "date": datetime.now().strftime("%Y-%m-%d")
    })

df = pd.DataFrame(jobs)
df.to_csv("data/raw_jobs.csv", index=False)

print("Jobs data fetched successfully")
