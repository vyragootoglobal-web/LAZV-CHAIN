from core.blockchain import Blockchain
import time

chain = Blockchain()
print("🚀 LAZV Seed Node is LIVE")

while True:
    chain.add_block(["block reward"])
    print(f"⛏️ Block {chain.height} mined — hash {chain.latest_block.hash[:8]}...")
    time.sleep(10)
