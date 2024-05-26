from models.financial_statement import FinancialStatement

class BalanceSheet(FinancialStatement):
    def generate(self, accounts):
        assets = sum(a.balance for a in accounts if a.account_type == 'asset')
        liabilities = sum(a.balance for a in accounts if a.account_type == 'liability')
        equity = sum(a.balance for a in accounts if a.account_type == 'equity')

        return {
            "Assets": assets,
            "Liabilities": liabilities,
            "Equity": equity,
            "Total Liabilities and Equity": liabilities + equity
        }
