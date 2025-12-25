from polygon.indexer import get_last_checkpoint

print("📱 LAZV Light Node")

checkpoint = get_last_checkpoint()
print("🔎 Public checkpoint:", checkpoint)
print("ℹ️ Chain can be recovered from this state.")
