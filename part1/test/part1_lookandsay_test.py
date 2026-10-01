"""
항을 입력했을 때 해당 항에 맞는 개미수열 값이 나왔는지 테스트
"""


import pytest
from service.LookAndSay import lookandsay

@pytest.mark.parametrize("n, a",[(1, "1"), (3, "21"), (4, "1211"), (5, "111221"), (6, "312211"), (7, "13112221"), (8, "1113213211"), (9, "31131211131221")])
def test_lookandsay(n : int, a : str):
    assert lookandsay(n) == a

