"""
Indexer skeleton:
Read Polygon TX input and extract LAZV checkpoint.
"""

def parse_checkpoint(tx_input_hex):
    try:
        decoded = bytes.fromhex(tx_input_hex[2:]).decode()
        return decoded
    except:
        return None

def get_last_checkpoint():
    # placeholder — future scan logic
    return {
        "chain": "LAZV",
        "height": 0,
        "hash": "GENESIS"
    }
