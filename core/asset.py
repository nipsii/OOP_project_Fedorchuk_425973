# core/asset.py
from .financial_item import FinancialItem

class Asset(FinancialItem):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_details(self):
        return f"Asset: ${self.value:.2f}"