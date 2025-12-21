import threading
import time
import socket
from flask import Flask, jsonify, request
from blockchain import Blockchain, hybrid_sign

# Node keys
PRIVKEY = "myclassicalkey"
PQ_PRIVKEY = "mypqkey"

chain = Blockchain()
peers = set()
app = Flask(__name__)

# ---------------------
# Block producer + heartbeat
# ---------------------
def produce_blocks():
    while True:
        time.sleep(10)
        msg = f"heartbeat {time.time()}"
        sig = hybrid_sign(msg, PRIVKEY, PQ_PRIVKEY)
        chain.add_block({"msg": msg, "sig": sig})

threading.Thread(target=produce_blocks, daemon=True).start()

# ---------------------
# Simple P2P listener
# ---------------------
def listen(port=9333):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", port))
    s.listen()
    print(f"[NODE] Listening on port {port}")
    while True:
        conn, addr = s.accept()
        peers.add(addr[0])
        conn.close()

threading.Thread(target=listen, daemon=True).start()

# ---------------------
# API endpoints
# ---------------------
@app.route("/")
def status():
    return jsonify({
        "chain_id": chain.chain_id,
        "height": len(chain.chain)-1,
        "peers": len(peers),
        "status": "LAZV node alive"
    })

@app.route("/chain", methods=["GET"])
def get_chain():
    return jsonify(chain.chain)

@app.route("/mine", methods=["POST"])
def mine_block():
    data = request.json.get("data", "empty")
    block = chain.add_block(data)
    return jsonify({"message":"Block added", "height":block["height"]})

@app.route("/add_peer", methods=["POST"])
def add_peer():
    addr = request.json.get("addr")
    if addr:
        peers.add(addr)
        return jsonify({"message":"Peer added","addr":addr})
    return jsonify({"error":"No addr provided"}), 400

@app.route("/polygon_bridge", methods=["POST"])
def polygon_bridge():
    token = request.json.get("token")
    amount = request.json.get("amount")
    from_addr = request.json.get("from")
    if token and amount and from_addr:
        chain.add_polygon_event(token, amount, from_addr)
        return jsonify({"message":"Polygon event added"})
    return jsonify({"error":"Missing data"}), 400

# ---------------------
# Polygon anchor placeholder
# ---------------------
def anchor_to_polygon():
    while True:
        if chain.chain:
            latest = chain.chain[-1]
            print(f"[ANCHOR] Would anchor block {latest['height']} hash {latest['hash']} to Polygon")
        time.sleep(60)

threading.Thread(target=anchor_to_polygon, daemon=True).start()

# ---------------------
# Main
# ---------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)