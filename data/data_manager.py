import json

class DataManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def save_data(self, data):
        with open(self.filepath, 'w') as f:
            json.dump(data, f, default=lambda o: o.__dict__, indent=4)

    def load_data(self):
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

# Specific data managers for users, accounts, and transactions
class UserDataManager(DataManager):
    def __init__(self, filepath='data/users.json'):
        super().__init__(filepath)

class AccountDataManager(DataManager):
    def __init__(self, filepath='data/accounts.json'):
        super().__init__(filepath)

class TransactionDataManager(DataManager):
    def __init__(self, filepath='data/transactions.json'):
        super().__init__(filepath)
