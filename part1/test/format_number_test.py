import pytest
from typing import List
from service.FormatNumber import format_number

@pytest.mark.parametrize("a, b", [(['1', '22', '33', '222'], 11222332), (['5555', '77', '6', '11'], 45271621), (['33', '111'], 2331), (['22', '3', '11', '2'], 22132112), (['3', '11', '33', '22', '1', '2'], 132123221112)])
def test_formatting(a : List[str], b : int):
    assert format_number(a) == b