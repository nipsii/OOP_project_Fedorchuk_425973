# core/wealth_tracker.py
from .financial_item import FinancialItem

class WealthTracker:
    def __init__(self):
        self.items = []

    def add_item(self, item: FinancialItem):
        self.items.append(item)

    def calculate_net_worth(self):
        return sum(item.get_value() for item in self.items)

    def display_summary(self):
        print("\n📊 YOUR FINANCIAL SUMMARY:")
        for item in self.items:
            print(f"{item.get_name()} — ${item.get_value():.2f}")
            print(f"   Info: {item.get_details()}")
        print(f"\n💰 Net Worth: ${self.calculate_net_worth():.2f}\n")