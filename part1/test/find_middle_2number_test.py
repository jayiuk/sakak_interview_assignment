import pytest
from service.FindMiddle2Number import find_middle_nums

@pytest.mark.parametrize("num, result", [(1211, 21), (111221, 12), (3333555512, 55), (80942524, 42), (34530987567410958313, 67)])
def test_find_nums(num : int, result : int):
    assert find_middle_nums(num) == result