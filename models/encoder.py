import torch
import torch.nn as nn

class CrossModalEncoder(nn.Module):
    def __init__(self, d_model=64):
        super().__init__()

        self.text_proj = nn.Embedding(1000, d_model)
        self.metric_proj = nn.Linear(8, d_model)

        self.attn = nn.MultiheadAttention(d_model, 4, batch_first=True)

    def forward(self, text_ids, metric_vec):
        text_emb = self.text_proj(text_ids)
        metric_emb = self.metric_proj(metric_vec).unsqueeze(1)

        fused, _ = self.attn(text_emb, metric_emb, metric_emb)
        return fused.mean(dim=1)