from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify([block.__dict__ for block in blockchain.chain])

@app.route('/mine', methods=['POST'])
def mine_block():
    data = request.json.get("data", "empty")
    blockchain.add_block(data)
    return jsonify({"message": "Block added", "data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)