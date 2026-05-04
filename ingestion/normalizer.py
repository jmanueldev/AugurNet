import re
import time
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class TelemetryEvent:
    timestamp: float
    service: str
    level: str
    message: str
    metrics: Dict[str, float]

class LogNormalizer:
    PATTERNS = [
        (re.compile(r"\d+\.\d+\.\d+\.\d+"), "<IP>"),
        (re.compile(r"\b\d+\b"), "<NUM>")
    ]

    def normalize(self, raw: Dict[str, Any]) -> TelemetryEvent:
        msg = raw.get("message", "")

        for p, t in self.PATTERNS:
            msg = p.sub(t, msg)

        return TelemetryEvent(
            timestamp=raw.get("timestamp", time.time()),
            service=raw.get("service", "unknown"),
            level=raw.get("level", "INFO"),
            message=msg,
            metrics=raw.get("metrics", {})
        )