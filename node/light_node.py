from polygon.checkpoint import read_last_checkpoint

print("📱 LAZV Light Node Starting…")

checkpoint = read_last_checkpoint()
if checkpoint:
    print("🔍 Last known state:", checkpoint)
else:
    print("⚠️ No Polygon checkpoint found — waiting for peers.")
