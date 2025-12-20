import requests, time, random

NODES = [
    "http://NODE1_IP:5000",
    "http://NODE2_IP:5000",
]

def pick_node():
    return random.choice(NODES)

def ping(node):
    try:
        r = requests.get(f"{node}/status", timeout=5)
        return r.json()
    except:
        return None

def latest(node):
    try:
        r = requests.get(f"{node}/latest", timeout=5)
        return r.json()
    except:
        return None

while True:
    node = pick_node()
    status = ping(node)

    if status:
        print("Connected:", node)
        print("Status:", status)
        print("Latest:", latest(node))
    else:
        print("Node down, retrying...")

    time.sleep(30)