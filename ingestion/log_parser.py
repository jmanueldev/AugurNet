import re
from collections import defaultdict

class DrainParser:
    def __init__(self):
        self.templates = defaultdict(int)

    def parse(self, log: str):
        template = re.sub(r"\d+", "<NUM>", log)
        template = re.sub(r"[A-Fa-f0-9]{8,}", "<HEX>", template)

        self.templates[template] += 1
        return template