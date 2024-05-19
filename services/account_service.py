from models.account import Account
from data.data_manager import AccountDataManager

class AccountService:
    def __init__(self, data_manager=None):
        self.data_manager = data_manager or AccountDataManager()
        self.accounts = [Account(**account) for account in self.data_manager.load_data()]

    def add_account(self, account):
        self.accounts.append(account)
        self.data_manager.save_data([account.__dict__ for account in self.accounts])

    def get_account(self, account_id):
        return next((acc for acc in self.accounts if acc.account_id == account_id), None)
