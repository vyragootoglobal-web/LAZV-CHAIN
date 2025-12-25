from polygon.checkpoint import read_last_checkpoint

print("📱 LAZV Light Node")

checkpoint = read_last_checkpoint()
if checkpoint:
    print("Last known chain state:", checkpoint)
else:
    print("No checkpoint found. Waiting for peers.")
