from polygon.polygon_rpc import send_rpc
from polygon.config import CHAIN_ID

def send_checkpoint(block):
    data = {
        "chain": CHAIN_ID,
        "height": block.height,
        "hash": block.hash,
        "timestamp": block.timestamp
    }
    print("📌 Polygon checkpoint:", data)
    # Future: encode to tx data field

def read_last_checkpoint():
    # Placeholder for indexer / future contract
    return None
