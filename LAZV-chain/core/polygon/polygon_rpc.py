import requests
from polygon.config import POLYGON_RPC

def send_rpc(method, params):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }
    r = requests.post(POLYGON_RPC, json=payload, timeout=10)
    return r.json()
