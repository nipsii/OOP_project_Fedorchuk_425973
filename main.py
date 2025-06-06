# main.py

from core.asset import Asset
from core.liability import Liability
from core.wealth_tracker import WealthTracker
from services.converter import CurrencyConverter
from services.calculator import Calculator
from data.top_lists import (
    display_top_list,
    richest_people,
    richest_companies,
    most_valuable_things,
    top_cryptocurrencies
)


REAL_ESTATE_PRICES = {
    "New York": 500000,
    "Los Angeles": 750000,
    "London": 600000,
    "Warsaw": 350000,
    "Krakow": 420000,
    "Tokyo": 900000,
    "Paris": 800000,
    "Prague": 450000,
    "Kyiv": 250000
}

def real_estate_prices():
    print("\n🏠 Supported Cities for Real Estate Lookup:")
    for city in REAL_ESTATE_PRICES:
        print(f" - {city}")

    city = input("\nEnter city/county from the list above: ").strip().title()

    price = REAL_ESTATE_PRICES.get(city)
    if price:
        print(f"\n🏠 Average home price in {city}: ${price:,}\n")
    else:
        print("\n⚠️ Invalid city! Please choose from the list above.\n")

def main():
    tracker = WealthTracker()
    converter = CurrencyConverter()
    calculator = Calculator()

    while True:
        print("\n====== 🧾 WEALTH MANAGEMENT SYSTEM ======")
        print("1. Add Asset")
        print("2. Add Liability")
        print("3. View Financial Summary")
        print("4. Convert Currency")
        print("5. Use Calculator")
        print("6. Real Estate Prices")
        print("7. Display Top 10 People")
        print("8. Display Top 10 Companies")
        print("9. Display Top 10 Things")
        print("10. Display Top 10 Cryptocurrencies")
        print("11. Exit")

        choice = input("Select option: ")

        if choice == "1":
            name = input("Asset name: ")
            value = float(input(f"Value of {name}: $"))
            tracker.add_item(Asset(name, value))
        elif choice == "2":
            name = input("Liability name: ")
            value = float(input(f"Value of {name}: $"))
            tracker.add_item(Liability(name, value))
        elif choice == "3":
            tracker.display_summary()
        elif choice == "4":
            converter.convert()
        elif choice == "5":
            calculator.calculate()
        elif choice == "6":
            real_estate_prices()
        elif choice == "7":
            display_top_list("🏆 Top 10 Richest People", richest_people)
        elif choice == "8":
            display_top_list("🏢 Top 10 Richest Companies", richest_companies,
                             key_name="name", value_key="market_cap", info_key="industry")
        elif choice == "9":
            display_top_list("💎 Top 10 Most Valuable Things", most_valuable_things,
                             key_name="name", value_key="value", info_key="category")
        elif choice == "10":
            display_top_list("🪙 Top 10 Cryptocurrencies", top_cryptocurrencies,
                             key_name="name", value_key="market_cap", info_key="type")
        elif choice == "11":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()