from p2p import P2PNetwork
network = P2PNetwork()
@app.route('/add_peer', methods=['POST'])
def add_peer():
    peer = request.json['peer']
    network.add_peer(peer)
    return jsonify({"message": "Peer added"})
    @app.route('/receive_block', methods=['POST'])
def receive_block():
    block_data = request.json
    blockchain.chain.append(type('Block', (), block_data))
    return jsonify({"message": "Block received"})