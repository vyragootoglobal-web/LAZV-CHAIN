class Token:
    def __init__(self, name, symbol, supply):
        self.name = name
        self.symbol = symbol
        self.total_supply = supply
        self.balances = {}

    def mint(self, address, amount):
        if address not in self.balances:
            self.balances[address] = 0
        self.balances[address] += amount

    def transfer(self, sender, receiver, amount):
        if self.balances.get(sender, 0) >= amount:
            self.balances[sender] -= amount
            self.balances[receiver] = self.balances.get(receiver, 0) + amount
            return True
        return False