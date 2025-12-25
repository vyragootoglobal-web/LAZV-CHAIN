class Token:
    SYMBOL = "LAZV"
    SUPPLY = 21_000_000

    def __init__(self):
        self.balances = {}

    def mint(self, address, amount):
        self.balances[address] = self.balances.get(address, 0) + amount
