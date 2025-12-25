"""
Polygon TX sender (optional).
Do NOT commit private keys.
"""

from web3 import Web3
from polygon.config import POLYGON_RPC

w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))

def send_tx(from_addr, to_addr, data_hex, private_key):
    nonce = w3.eth.get_transaction_count(from_addr)
    tx = {
        "nonce": nonce,
        "to": to_addr,
        "value": 0,
        "gas": 120000,
        "gasPrice": w3.to_wei("40", "gwei"),
        "data": data_hex,
        "chainId": 137
    }
    signed = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    return tx_hash.hex()
