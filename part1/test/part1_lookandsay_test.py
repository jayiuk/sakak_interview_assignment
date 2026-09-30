import pytest
from service.LookAndSay import lookandsay

@pytest.mark.parametrize("n, a",[(3, 21), (4, 1211), (5, 111221), (6, 312211), (7, 13112221), (8, 1113213211), (9, 31131211131221)])
def test_lookandsay(n : int, a : int):
    assert lookandsay(n) == a

