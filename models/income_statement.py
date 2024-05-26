from models.financial_statement import FinancialStatement

class IncomeStatement(FinancialStatement):
    def generate(self, transactions):
        revenue = sum(t.amount for t in transactions if t.transaction_type == 'credit')
        expenses = sum(t.amount for t in transactions if t.transaction_type == 'debit')
        net_income = revenue - expenses

        return {
            "Revenue": revenue,
            "Expenses": expenses,
            "Net Income": net_income
        }
