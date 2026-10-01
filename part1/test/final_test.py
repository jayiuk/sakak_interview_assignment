"""
최종적으로 항을 넣었을 때 그 항의 개미수열의 가운데 두자릿수가 나오는지 테스트
여기선 범위 밖 숫자에 대한 에러 처리도 같이 테스트 진행
"""


import pytest
from service.GetLookandsayMiddleNums import get_lookandsay_middle_nums


@pytest.mark.parametrize("n, result", [(4, 21), (5, 12), (6, 22), (7, 12), (8, 21), (9, 11)])
def test_final(n : int, result : int):
    assert get_lookandsay_middle_nums(n) == result
    
@pytest.mark.parametrize("n, predicted", [(0, ValueError), (1, ValueError), (2, ValueError), (3, ValueError), (100, ValueError), (101, ValueError), (1000, ValueError)])
def test_under3_over100_except(n, predicted):
    with pytest.raises(predicted):
        get_lookandsay_middle_nums(n)

def test_big_num():
    get_lookandsay_middle_nums(99)