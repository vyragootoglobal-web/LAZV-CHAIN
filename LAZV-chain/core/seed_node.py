from core.blockchain import Blockchain
import time

chain = Blockchain()

print("✅ LAZV Seed Node Running")

while True:
    chain.add_block(["block reward"])
    print(f"⛏️ Block {chain.height} mined")
    time.sleep(10)
