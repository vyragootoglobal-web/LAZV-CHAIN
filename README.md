# LAZV Chain

LAZV is a sovereign blockchain anchored to Polygon for public checkpointing.

Polygon is used only for:
- Public block hash verification
- Network recovery
- Future bridge support

Polygon is **not required** for LAZV to run.
## If the Maintainer Disappears

LAZV is designed to survive.

- Anyone may run a seed node
- Valid chain = longest valid chain + Polygon checkpoints
- Forking is allowed if repository is abandoned

This is intentional.


LAZV-chain/
├─ core/        # Sovereign logic
├─ node/        # Network & nodes
├─ polygon/     # Anchor & recovery
├─ explorer/    # Read-only
├─ docs/        # Survival manuals
├─ README.md
├─ MANIFESTO.md
└─ LICENSE
