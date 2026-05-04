# Simplified placeholder (replace with real Kafka client in production)

class KafkaConsumerMock:
    def poll(self):
        return [
            {"message": "timeout on service A", "metrics": {"latency": 1200}},
            {"message": "retry attempt failed", "metrics": {"retries": 3}}
        ]