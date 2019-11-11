from typing import List

def fx_weighted_average(lots: List[int], prices: List[float]) -> float:
    """Calculates the weighted average price per currency"""
    assert len(lots) == len(prices), "amounts list length must equal " \
    "prices list length"
    for lot in lots:
        assert 1 <= lot <= 100, "a lot in lots must be between 1 " \
        "and 100"
    lots_1_mio = [lot * 1000000 for lot in lots]
    lots_by_prices = [a_i * p_i for a_i, p_i in zip(lots_1_mio, prices)]
    lots_sum = sum(lots_1_mio)
    lots_by_prices_sum = sum(lots_by_prices)
    print(f"{format(lots_sum, ',')} at {format(lots_by_prices_sum / lots_sum, '0.5f')}")