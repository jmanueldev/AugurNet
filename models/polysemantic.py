import torch
import torch.nn as nn

class PolysemanticLatent(nn.Module):
    def __init__(self, d_model=64, num_hyp=4):
        super().__init__()
        self.num_hyp = num_hyp

        self.base = nn.Linear(d_model, d_model)
        self.heads = nn.ModuleList([nn.Linear(d_model, d_model) for _ in range(num_hyp)])
        self.weight = nn.Linear(d_model, num_hyp)

    def forward(self, x):
        base = self.base(x)

        hyps = torch.stack([h(base) for h in self.heads], dim=1)
        weights = torch.softmax(self.weight(base), dim=-1)

        return hyps, weights