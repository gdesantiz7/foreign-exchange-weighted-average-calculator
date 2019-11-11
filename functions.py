from typing import List

def fx_weighted_average(amounts: List[int], prices: List[float]) -> float:
    """Calculates the weighted average price per currency"""
    assert len(amounts) == len(prices), "amounts list length must equal " \
    "prices list length"
    for amount in amounts:
        assert 1 <= amount <= 100, "an amount in amounts must be between 1 " \
        "and 100"
    amounts_1_mio = [amount * 1000000 for amount in amounts]
    amounts_by_prices = [a_i * p_i for a_i, p_i in zip(amounts_1_mio, prices)]
    amounts_sum = sum(amounts_1_mio)
    amounts_by_prices_sum = sum(amounts_by_prices)
    print(f"{format(amounts_sum, ',')} at {format(amounts_by_prices_sum / \
                                                  amounts_sum, '0.5f')}")