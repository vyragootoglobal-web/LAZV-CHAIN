# LAZV Chain – Mini Node (Termux Stable)

import hashlib
import json
import time
import socket
import threading

def sha3(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()

class Block:
    def __init__(self, index, prev_hash, txs):
        self.index = index
        self.prev_hash = prev_hash
        self.txs = txs
        self.timestamp = time.time()
        self.hash = self.compute_hash()

    def compute_hash(self):
        raw = json.dumps({
            "i": self.index,
            "p": self.prev_hash,
            "t": self.txs,
            "ts": self.timestamp
        }, sort_keys=True).encode()
        return sha3(raw)

class Chain:
    def __init__(self):
        self.blocks = []
        self.genesis()

    def genesis(self):
        self.blocks.append(Block(0, "0"*64, []))

    def add_block(self):
        last = self.blocks[-1]
        blk = Block(len(self.blocks), last.hash, [])
        self.blocks.append(blk)
        return blk

class Node:
    def __init__(self, port=9333):
        self.chain = Chain()
        self.port = port

    def start(self):
        threading.Thread(target=self.listen, daemon=True).start()
        self.loop()

    def listen(self):
        s = socket.socket()
        s.bind(("0.0.0.0", self.port))
        s.listen()
        print(f"[NODE] Listening on {self.port}")
        while True:
            conn, _ = s.accept()
            conn.close()

    def loop(self):
        while True:
            time.sleep(10)
            blk = self.chain.add_block()
            print(f"[BLOCK] #{blk.index} {blk.hash[:16]}...")

if __name__ == "__main__":
    Node().start()