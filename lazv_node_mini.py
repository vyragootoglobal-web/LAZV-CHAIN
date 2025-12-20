from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Mini blockchain
chain = []

# Peers list (dummy for now)
peers = []

@app.route("/chain", methods=["GET"])
def get_chain():
    return jsonify({"chain": chain, "length": len(chain), "peers": peers})

@app.route("/add/<data>", methods=["POST"])
def add_data(data):
    chain.append(data)
    return jsonify({"message": f"'{data}' added to chain", "length": len(chain)})

@app.route("/peers/add/<peer>", methods=["POST"])
def add_peer(peer):
    if peer not in peers:
        peers.append(peer)
    return jsonify({"peers": peers})

@app.route("/peers", methods=["GET"])
def list_peers():
    return jsonify({"peers": peers})

if __name__ == "__main__":
    # auto sleep if battery < 30% is a manual Termux config; we keep node light here
    app.run(host="0.0.0.0", port=5000)