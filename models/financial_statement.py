class FinancialStatement:
    def __init__(self, statement_id, period_start, period_end):
        self.statement_id = statement_id
        self.period_start = period_start
        self.period_end = period_end

    def generate(self):
        raise NotImplementedError("Subclasses should implement this method.")
