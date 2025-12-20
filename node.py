import threading, time, os, random
from blockchain import LAZVChain, hybrid_sign

class LAZVNode:
    def __init__(self):
        self.chain = LAZVChain()
        self.privkey = "myclassicalkey"
        self.pq_privkey = "mypqkey"
        os.makedirs("lumi_nodes", exist_ok=True)
    
    def heartbeat_loop(self):
        hb = 0
        while True:
            time.sleep(10)
            hb += 1
            msg = f'heartbeat {hb}'
            sig = hybrid_sign(msg, self.privkey, self.pq_privkey)
            block_data = {"msg": msg, "sig": sig}
            self.chain.add_block(block_data)
            self.chain.produce_block_from_mempool()

    def start(self):
        threading.Thread(target=self.heartbeat_loop, daemon=True).start()
        print('[LAZV NODE] Anti-Quantum Node started')

if __name__ == "__main__":
    node = LAZVNode()
    node.start()
    
    # Simulasi transaksi
    while True:
        tx = {"from": random.randint(1,1000), "to": random.randint(1,1000), "amount": random.randint(1,100)}
        node.chain.add_tx(tx)
        time.sleep(5)