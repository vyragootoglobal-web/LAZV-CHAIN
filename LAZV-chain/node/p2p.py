PEERS = set()

def add_peer(address):
    PEERS.add(address)

def get_peers():
    return list(PEERS)

def sync_chain(remote_height):
    print("🔄 Sync requested from peer height:", remote_height)
