import json
from polygon.config import CHAIN_ID

def encode_checkpoint(block):
    payload = {
        "chain": CHAIN_ID,
        "height": block.height,
        "hash": block.hash,
        "timestamp": block.timestamp
    }
    return json.dumps(payload)

def send_checkpoint(block):
    data = encode_checkpoint(block)
    print("📌 Polygon Checkpoint Payload:")
    print(data)

    # NEXT STEP (optional):
    # sign tx
    # send tx with data field
