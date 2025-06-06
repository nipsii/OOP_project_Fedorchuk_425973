import pytest
from core.tracker import WealthTracker

def test_net_worth_calculation():
    tracker = WealthTracker()
    tracker.add_asset_manually("Cash", 1000)
    tracker.add_liability_manually("Debt", 200)
    assert tracker.calculate_net_worth() == 800