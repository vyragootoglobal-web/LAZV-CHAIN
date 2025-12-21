import threading, time, socket, json, requests
from flask import Flask, jsonify, request
from blockchain import Blockchain, hybrid_sign

# Node keys
PRIVKEY = "myclassicalkey"
PQ_PRIVKEY = "mypqkey"

chain = Blockchain()
peers = set()
bootstrap_peers = ["<bootstrap-ip1>:5000","<bootstrap-ip2>:5000"]
app = Flask(__name__)

# ---------------------
# Block producer
# ---------------------
def produce_blocks():
    while True:
        time.sleep(10)
        msg = f"heartbeat {time.time()}"
        sig = hybrid_sign(msg, PRIVKEY, PQ_PRIVKEY)
        chain.add_block({"msg": msg, "sig": sig})

threading.Thread(target=produce_blocks, daemon=True).start()

# ---------------------
# P2P listener
# ---------------------
def listen(port=9333):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", port))
    s.listen()
    while True:
        conn, addr = s.accept()
        peers.add(addr[0])
        conn.close()

threading.Thread(target=listen, daemon=True).start()

# ---------------------
# Connect to peer
# ---------------------
def connect_to_peer(addr):
    try:
        ip, port = addr.split(":")
        url = f"http://{ip}:{port}/add_peer"
        requests.post(url,json={"addr": f"{get_local_ip()}:9333"})
        peers.add(ip)
    except:
        pass

# ---------------------
# Periodic peer discovery
# ---------------------
def peer_discovery():
    while True:
        for b in bootstrap_peers:
            connect_to_peer(b)
        for p in list(peers):
            try:
                url = f"http://{p}:5000/get_peers"
                r = requests.get(url, timeout=2)
                for new in r.json():
                    peers.add(new)
            except:
                continue
        time.sleep(30)

threading.Thread(target=peer_discovery, daemon=True).start()

# ---------------------
# Flask API
# ---------------------
@app.route("/")
def status():
    return jsonify({
        "chain_id": chain.chain_id,
        "height": len(chain.chain)-1,
        "peers": list(peers),
        "status": "LAZV node alive"
    })

@app.route("/chain", methods=["GET"])
def get_chain():
    return jsonify(chain.chain)

@app.route("/mine", methods=["POST"])
def mine_block():
    data = request.json.get("data","empty")
    block = chain.add_block(data)
    return jsonify({"message":"Block added","height":block["height"]})

@app.route("/add_peer", methods=["POST"])
def add_peer():
    addr = request.json.get("addr")
    if addr:
        peers.add(addr.split(":")[0])
        return jsonify({"message":"Peer added","addr":addr})
    return jsonify({"error":"No addr provided"}),400

@app.route("/get_peers", methods=["GET"])
def get_peers():
    return jsonify(list(peers))

@app.route("/polygon_bridge", methods=["POST"])
def polygon_bridge():
    token = request.json.get("token")
    amount = request.json.get("amount")
    from_addr = request.json.get("from")
    if token and amount and from_addr:
        chain.add_polygon_event(token, amount, from_addr)
        return jsonify({"message":"Polygon event added"})
    return jsonify({"error":"Missing data"}),400

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
# Helper
# ---------------------
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8",80))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

# ---------------------
# MAIN
# ---------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)