class Account:
    def __init__(self, account_id, name, account_type, balance=0):
        self.account_id = account_id
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def __repr__(self):
        return f"Account({self.account_id}, {self.name}, {self.account_type}, {self.balance})"
