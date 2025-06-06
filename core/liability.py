# core/liability.py
from .financial_item import FinancialItem

class Liability(FinancialItem):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return -self.value  # Liabilities reduce net worth

    def get_details(self):
        return f"Liability: -${abs(self.value):.2f}"