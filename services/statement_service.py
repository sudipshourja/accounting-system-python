from models.income_statement import IncomeStatement
from models.balance_sheet import BalanceSheet
from models.cash_flow_statement import CashFlowStatement

class StatementService:
    def __init__(self, account_service, transaction_service):
        self.account_service = account_service
        self.transaction_service = transaction_service

    def generate_income_statement(self):
        income_statement = IncomeStatement(1, "2024-01-01", "2024-12-31")
        return income_statement.generate(self.transaction_service.transactions)

    def generate_balance_sheet(self):
        balance_sheet = BalanceSheet(1, "2024-01-01", "2024-12-31")
        return balance_sheet.generate(self.account_service.accounts)

    def generate_cash_flow_statement(self):
        cash_flow_statement = CashFlowStatement(1, "2024-01-01", "2024-12-31")
        return cash_flow_statement.generate(self.transaction_service.transactions)
