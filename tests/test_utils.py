import pytest
from src.utils import calculate_taxes


@pytest.fixture
def prices():
    return [100, 200, 300]


@pytest.mark.parametrize("tax_rate, expected", [(10, [110, 220, 330]),
                                                 (20, [120, 240, 360]),
                                                 (5, [105, 210, 315])])


def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_invalid_tax_value(prices):
    with pytest.raises(ValueError) as exept_info:
        calculate_taxes(prices, tax_rate=-1)


def test_calculate_taxes_invalid_prices():
    with pytest.raises(ValueError) as exept_info:
        calculate_taxes([-1,0,10], 10)


