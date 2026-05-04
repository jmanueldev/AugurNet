import requests

GHE_ENDPOINTS = [
    "http://ghe1:8001/infer",
    "http://ghe2:8002/infer"
]

def call_ghes(latent):
    results = []

    for url in GHE_ENDPOINTS:
        r = requests.post(url, json=latent.tolist())
        results.append(r.json()["hypothesis"])

    return results