# data/top_lists.py

class TopListItem:
    def get_name(self):
        raise NotImplementedError("Subclasses must implement get_name()")

    def get_value(self):
        raise NotImplementedError("Subclasses must implement get_value()")

    def get_info(self):
        return "No info available"


# ======================
# SUBCLASSES FOR POLYMORPHISM
# ======================

class Person(TopListItem):
    def __init__(self, name, net_worth, source):
        self.name = name
        self.net_worth = net_worth
        self.source = source

    def get_name(self):
        return self.name

    def get_value(self):
        return self.net_worth

    def get_info(self):
        return self.source


class Company(TopListItem):
    def __init__(self, name, market_cap, industry):
        self.name = name
        self.market_cap = market_cap
        self.industry = industry

    def get_name(self):
        return self.name

    def get_value(self):
        return self.market_cap

    def get_info(self):
        return self.industry


class ValuableItem(TopListItem):
    def __init__(self, name, value, category):
        self.name = name
        self.value = value
        self.category = category

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_info(self):
        return self.category


class CryptoCurrency(TopListItem):
    def __init__(self, name, market_cap, coin_type):
        self.name = name
        self.market_cap = market_cap
        self.coin_type = coin_type

    def get_name(self):
        return self.name

    def get_value(self):
        return self.market_cap

    def get_info(self):
        return self.coin_type


# ======================
# SAMPLE DATA LISTS
# ======================

richest_people = [
    Person("Elon Musk", 260, "Tesla, SpaceX"),
    Person("Bernard Arnault", 210, "LVMH"),
    Person("Jeff Bezos", 180, "Amazon"),
    Person("Larry Ellison", 160, "Oracle"),
    Person("Bill Gates", 145, "Microsoft"),
    Person("Mark Zuckerberg", 135, "Meta"),
    Person("Steve Ballmer", 120, "Microsoft"),
    Person("Warren Buffett", 115, "Berkshire Hathaway"),
    Person("Mukesh Ambani", 100, "Reliance Industries"),
    Person("Carlos Slim Helu", 95, "Telecom")
]

richest_companies = [
    Company("Apple Inc.", 2800, "Technology"),
    Company("Microsoft", 2500, "Technology"),
    Company("Saudi Aramco", 2100, "Energy"),
    Company("Alphabet Inc.", 1700, "Technology"),
    Company("Amazon", 1600, "E-commerce"),
    Company("NVIDIA", 1100, "Semiconductors"),
    Company("Tesla", 700, "Automotive"),
    Company("Berkshire Hathaway", 680, "Conglomerate"),
    Company("Meta Platforms", 650, "Social Media"),
    Company("Walmart", 550, "Retail")
]

most_valuable_things = [
    ValuableItem("Global Gold Reserves", 120000, "Commodity"),
    ValuableItem("Global Real Estate", 300000, "Land"),
    ValuableItem("Global Stock Market", 120000, "Finance"),
    ValuableItem("Oil Reserves", 100000, "Energy"),
    ValuableItem("Bitcoin Network", 1500, "Crypto"),
    ValuableItem("Art Market", 2000, "Culture"),
    ValuableItem("Big Tech Data", 10000, "Digital"),
    ValuableItem("AI Technology", 8000, "Tech"),
    ValuableItem("U.S. National Debt", 34000, "Debt"),
    ValuableItem("Global GDP", 100000, "Economy")
]

top_cryptocurrencies = [
    CryptoCurrency("Bitcoin (BTC)", 700, "Decentralized"),
    CryptoCurrency("Ethereum (ETH)", 350, "Smart Contracts"),
    CryptoCurrency("Tether (USDT)", 90, "Stablecoin"),
    CryptoCurrency("BNB (BNB)", 50, "Exchange"),
    CryptoCurrency("XRP (XRP)", 30, "Payments"),
    CryptoCurrency("Cardano (ADA)", 10, "Smart Contracts"),
    CryptoCurrency("Solana (SOL)", 120, "Fast Chain"),
    CryptoCurrency("Polkadot (DOT)", 10, "Interoperability"),
    CryptoCurrency("Dogecoin (DOGE)", 10, "Meme Coin"),
    CryptoCurrency("Avalanche (AVAX)", 20, "Scalable")
]


# ======================
# DISPLAY FUNCTION
# ======================

def display_top_list(title, items):
    print(f"\n{title}")
    print("=" * 60)
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item.get_name()}")
        print(f"   Value: ${item.get_value()} Billion")
        print(f"   Info: {item.get_info()}")
        print("-" * 60)