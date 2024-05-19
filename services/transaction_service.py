from models.transaction import Transaction
from data.data_manager import TransactionDataManager

class TransactionService:
    def __init__(self, data_manager=None):
        self.data_manager = data_manager or TransactionDataManager()
        self.transactions = [Transaction(**transaction) for transaction in self.data_manager.load_data()]

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        transaction.account.balance += transaction.amount if transaction.transaction_type == 'credit' else -transaction.amount
        self.data_manager.save_data([transaction.__dict__ for transaction in self.transactions])
