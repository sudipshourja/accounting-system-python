from models.financial_statement import FinancialStatement

class CashFlowStatement(FinancialStatement):
    def generate(self, transactions):
        cash_inflows = sum(t.amount for t in transactions if t.transaction_type == 'credit')
        cash_outflows = sum(t.amount for t in transactions if t.transaction_type == 'debit')
        net_cash_flow = cash_inflows - cash_outflows

        return {
            "Cash Inflows": cash_inflows,
            "Cash Outflows": cash_outflows,
            "Net Cash Flow": net_cash_flow
        }
