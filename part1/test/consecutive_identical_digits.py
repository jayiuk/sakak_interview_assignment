"""
연속된 같은 값들을 하나의 문자열로 묶은 후 그 문자열들의 리스트로 잘 반환하는지 확인
여기선 정규표현식 버전, itertools.groupby 버전 2개를 테스트
정규표현식 버전이 위, groupby 버전이 아래
"""


import pytest
from typing import List
from service.Consecutive import find_consecutive, find_consecutive_groupby


@pytest.mark.parametrize("a, b", [(12233222, ['1', '22', '33', '222']), (555577611, ['5555', '77', '6', '11']), (33111, ['33', '111']), (223112, ['22', '3', '11', '2']), (311332212, ['3', '11', '33', '22', '1', '2'])])
def test_finding_consecutive(a : int, b : List[str]):
    assert find_consecutive(a) == b
    
@pytest.mark.parametrize("a, b", [("12233222", ['1', '22', '33', '222']), ("555577611", ['5555', '77', '6', '11']), ("33111", ['33', '111']), ("223112", ['22', '3', '11', '2']), ("311332212", ['3', '11', '33', '22', '1', '2'])])
def test_finding_consecutive_groupby(a : str, b : List[str]):
    assert find_consecutive_groupby(a) == b