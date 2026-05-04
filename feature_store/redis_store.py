import redis
import json

class RedisFeatureStore:
    def __init__(self, host="localhost", port=6379):
        self.client = redis.Redis(host=host, port=port, decode_responses=True)

    def set_feature(self, key, value):
        self.client.set(key, json.dumps(value))

    def get_feature(self, key):
        val = self.client.get(key)
        return json.loads(val) if val else None

    def cache_hypothesis(self, key, value):
        self.client.setex(key, 300, json.dumps(value))  # TTL 5 min