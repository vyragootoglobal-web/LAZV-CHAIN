import time, json, hashlib, os

# --------------------------
# Hash & Hybrid Signature
# --------------------------
def sha3(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()

def classical_sign(msg, privkey):
    return sha3((msg + privkey).encode())

def pq_sign(msg, pq_privkey):
    return sha3(("PQ"+msg+pq_privkey).encode())

def hybrid_sign(msg, privkey, pq_privkey):
    return {'classical': classical_sign(msg, privkey), 'post_quantum': pq_sign(msg, pq_privkey)}

# --------------------------
# LAZV Block
# --------------------------
class Block:
    def __init__(self, index, prev_hash, data):
        self.index = index
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calc_hash()
    
    def calc_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'prev_hash': self.prev_hash,
            'data': self.data,
            'timestamp': self.timestamp,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return sha3(block_string)

# --------------------------
# LAZV Blockchain
# --------------------------
class LAZVChain:
    def __init__(self, finality_interval=10):
        self.chain = []
        self.mempool = []
        self.finality_interval = finality_interval
        self.finalized_height = 0
        self.genesis()
    
    def genesis(self):
        self.chain.append(Block(0, '0'*64, 'GENESIS_LAZV'))

    def add_block(self, data):
        prev = self.chain[-1]
        blk = Block(len(self.chain), prev.hash, data)
        self.chain.append(blk)
        self.check_finality()
        print(f'[LAZV BLOCK] #{blk.index} {blk.hash[:16]}')
    
    def check_finality(self):
        if len(self.chain) - self.finalized_height >= self.finality_interval:
            self.finalized_height = len(self.chain) - 1
            print(f'[FINALITY] Block {self.finalized_height} finalized')

    def add_tx(self, tx_data):
        if len(self.mempool) < 1000:
            self.mempool.append(tx_data)
    
    def produce_block_from_mempool(self):
        if self.mempool:
            data_batch = self.mempool[:50]
            self.mempool = self.mempool[50:]
            self.add_block(data_batch)