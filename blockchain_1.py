from block import Block
import time

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "LAZV Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest = self.get_latest_block()
        new_block = Block(
            index=latest.index + 1,
            previous_hash=latest.hash,
            timestamp=time.time(),
            data=data
        )
        self.chain.append(new_block)