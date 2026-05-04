import torch

class IterativeInterpreter:
    def __init__(self, steps=3, noise=0.05):
        self.steps = steps
        self.noise = noise

    def refine(self, latent):
        history = []
        current = latent

        for _ in range(self.steps):
            noise = torch.randn_like(current) * self.noise
            current = current + noise
            history.append(current)

        return history