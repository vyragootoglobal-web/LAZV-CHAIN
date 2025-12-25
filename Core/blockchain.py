from core.block import Block
from polygon.checkpoint import send_checkpoint

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0"*64, ["GENESIS"])

    @property
    def height(self):
        return len(self.chain) - 1

    @property
    def latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        block = Block(
            height=self.height + 1,
            prev_hash=self.latest_block.hash,
            transactions=transactions
        )
        self.chain.append(block)

        if block.height % 100 == 0:
            send_checkpoint(block)

        return block
