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
    # FUTURE: encode this data into a Polygon transaction memo field
    return data

def read_last_checkpoint():
    # placeholder for future indexer / Chain data lookup
    return None
