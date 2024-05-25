class Transaction:
    def __init__(self, transaction_id, account, amount, transaction_type, description=''):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description

    def __repr__(self):
        return f"Transaction({self.transaction_id}, {self.account}, {self.amount}, {self.transaction_type})"
