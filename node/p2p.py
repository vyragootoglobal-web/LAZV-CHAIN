PEERS = set()

def add_peer(address):
    PEERS.add(address)

def get_peers():
    return list(PEERS)
