from fastapi import FastAPI
import torch

app = FastAPI()

@app.post("/infer")
def infer(latent: list):
    tensor = torch.tensor(latent)
    result = tensor.mean(dim=-1)  # placeholder logic

    return {"hypothesis": result.tolist()}