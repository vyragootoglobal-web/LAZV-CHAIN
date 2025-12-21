import time
import json
import hashlib
import os

DATA_DIR = "data"
CHAIN_FILE = f"{DATA_DIR}/chain.json"

def sha3(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()

def classical_sign(message: str, privkey: str) -> str:
    return sha3((message + privkey).encode())

def pq_sign(message: str, pq_privkey: str) -> str:
    # Placeholder for post-quantum signature
    return sha3(("PQ" + message + pq_privkey).encode())

def hybrid_sign(message: str, privkey: str, pq_privkey: str) -> dict:
    return {
        "classical": classical_sign(message, privkey),
        "post_quantum": pq_sign(message, pq_privkey)
    }

class Blockchain:
    def __init__(self, chain_id="LAZV-1"):
        self.chain_id = chain_id
        self.chain = []
        self.mempool = []
        self.finalized_height = 0
        os.makedirs(DATA_DIR, exist_ok=True)
        self.load_chain()
        if not self.chain:
            self.create_genesis()

    def create_genesis(self):
        genesis = {
            "height": 0,
            "prev_hash": "0"*64,
            "timestamp": time.time(),
            "chain_id": self.chain_id,
            "data": "LAZV Genesis Block"
        }
        genesis["hash"] = self.hash_block(genesis)
        self.chain.append(genesis)
        self.save_chain()

    def hash_block(self, block: dict) -> str:
        return sha3(json.dumps(block, sort_keys=True).encode())

    def add_block(self, data):
        last = self.chain[-1]
        block = {
            "height": last["height"] + 1,
            "prev_hash": last["hash"],
            "timestamp": time.time(),
            "data": data
        }
        block["hash"] = self.hash_block(block)
        self.chain.append(block)
        self.finalized_height = block["height"]
        self.save_chain()
        return block

    def save_chain(self):
        with open(CHAIN_FILE, "w") as f:
            json.dump(self.chain, f, indent=2)

    def load_chain(self):
        if os.path.exists(CHAIN_FILE):
            with open(CHAIN_FILE) as f:
                self.chain = json.load(f)

    # Simulate bridging token from Polygon
    def add_polygon_event(self, token, amount, from_addr):
        event = {
            "event": "polygon_bridge",
            "token": token,
            "amount": amount,
            "from": from_addr,
            "timestamp": time.time()
        }
        self.add_block(event)