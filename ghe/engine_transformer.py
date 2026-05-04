import torch
import torch.nn as nn

class HypothesisEngine(nn.Module):
    def __init__(self, d_model=64):
        super().__init__()

        self.decoder = nn.TransformerDecoder(
            nn.TransformerDecoderLayer(d_model, 4),
            num_layers=2
        )

    def forward(self, latent):
        B, H, D = latent.shape
        outputs = []

        for i in range(H):
            z = latent[:, i, :].unsqueeze(1)
            out = self.decoder(z, z)
            outputs.append(out.squeeze(1))

        return torch.stack(outputs, dim=1)