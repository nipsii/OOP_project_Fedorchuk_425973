# core/financial_item.py

class FinancialItem:
    def get_name(self):
        raise NotImplementedError("Subclasses must implement get_name()")

    def get_value(self):
        raise NotImplementedError("Subclasses must implement get_value()")

    def get_details(self):
        return "No details available"