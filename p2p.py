import requests

class P2PNetwork:
    def __init__(self):
        self.peers = set()

    def add_peer(self, address):
        self.peers.add(address)

    def broadcast_block(self, block):
        for peer in self.peers:
            try:
                requests.post(f"{peer}/receive_block", json=block)
            except:
                pass