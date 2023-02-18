import json
import requests

r = requests.get("https://stud-api.sabir.pro/articles")
j = json.loads(r.text)

for e in j:
    i = e["id"]

    requests.delete(
        f"https://stud-api.sabir.pro/articles/{i}",
        headers={"authorization": "r:764a3c255228b9ae3ac1aaa5f97d897c"},
    )

    print(f"deleting {i}..")
