import pytest
from typing import List
from service.Consecutive import find_consecutive, find_consecutive_groupby


@pytest.mark.parametrize("a, b", [(12233222, ['1', '22', '33', '222']), (555577611, ['5555', '77', '6', '11']), (33111, ['33', '111']), (223112, ['22', '3', '11', '2']), (311332212, ['3', '11', '33', '22', '1', '2'])])
def test_finding_consecutive(a : int, b : List[str]):
    assert find_consecutive(a) == b
    
@pytest.mark.parametrize("a, b", [(12233222, ['1', '22', '33', '222']), (555577611, ['5555', '77', '6', '11']), (33111, ['33', '111']), (223112, ['22', '3', '11', '2']), (311332212, ['3', '11', '33', '22', '1', '2'])])
def test_finding_consecutive_groupby(a : int, b : List[str]):
    assert find_consecutive_groupby(a) == b