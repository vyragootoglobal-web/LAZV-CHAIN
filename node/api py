from flask import Flask, jsonify
from core.blockchain import Blockchain

app = Flask(__name__)
chain = Blockchain()

@app.route("/status")
def status():
    return jsonify({
        "height": chain.height,
        "latest_hash": chain.latest_block.hash
    })

app.run(port=8333)
