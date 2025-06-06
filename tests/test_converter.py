import pytest
from core.converter import CurrencyConverter

def test_usd_to_eur():
    c = CurrencyConverter()
    assert round(c.convert("USD", "EUR", 100), 2) == 92.00