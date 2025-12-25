import time
import hashlib
import json

class Block:
    def __init__(self, height, prev_hash, transactions, timestamp=None):
        self.height = height
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.timestamp = timestamp or int(time.time())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = json.dumps({
            "height": self.height,
            "prev_hash": self.prev_hash,
            "tx": self.transactions,
            "timestamp": self.timestamp
        }, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()
