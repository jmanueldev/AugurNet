from transformers import AutoTokenizer, AutoModel
import torch

class BertLogEncoder:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
        self.model = AutoModel.from_pretrained("distilbert-base-uncased")

    def encode(self, logs):
        tokens = self.tokenizer(
            logs,
            padding=True,
            truncation=True,
            return_tensors="pt"
        )

        with torch.no_grad():
            output = self.model(**tokens)

        return output.last_hidden_state.mean(dim=1)