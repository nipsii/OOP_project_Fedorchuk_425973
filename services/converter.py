# services/converter.py

CURRENCY_RATES = {
    "USD": {"USD": 1.00, "EUR": 0.92, "PLN": 3.92, "UAH": 37.50, "CAD": 1.36, "AUD": 1.49},
    "EUR": {"USD": 1.09, "EUR": 1.00, "PLN": 4.26, "UAH": 40.75, "CAD": 1.48, "AUD": 1.62},
    "PLN": {"USD": 0.25, "EUR": 0.23, "PLN": 1.00, "UAH": 9.56, "CAD": 0.35, "AUD": 0.38},
    "UAH": {"USD": 0.026, "EUR": 0.024, "PLN": 0.10, "UAH": 1.00, "CAD": 0.036, "AUD": 0.040},
    "CAD": {"USD": 0.73, "EUR": 0.68, "PLN": 2.85, "UAH": 27.70, "CAD": 1.00, "AUD": 1.09},
    "AUD": {"USD": 0.67, "EUR": 0.62, "PLN": 2.61, "UAH": 25.40, "CAD": 0.92, "AUD": 1.00}
}

def validate_input(prompt, data_type=float):
    while True:
        try:
            return data_type(input(prompt))
        except ValueError:
            print("⚠️ Invalid input. Please try again.")

class CurrencyConverter:
    def convert(self):
        from_curr = input("From currency (e.g., USD): ").upper()
        to_curr = input("To currency (e.g., EUR): ").upper()

        if from_curr not in CURRENCY_RATES or to_curr not in CURRENCY_RATES:
            print(f"\n❌ Invalid currency. Supported currencies are: {', '.join(CURRENCY_RATES.keys())}\n")
            return

        amount = validate_input(f"Amount in {from_curr}: $")
        rate = CURRENCY_RATES[from_curr][to_curr]
        converted = amount * rate
        print(f"\n✅ {amount} {from_curr} = {converted:.2f} {to_curr}\n")