"""
연속된 같은수를 하나의 문자열로 변환
그 후 그 문자열들의 리스트를 반환
연속된 같은 수가 없을 때(양 옆으로 혼자일 때)엔 그 숫자 하나가 문자열 하나가 됨
"""
import re
from itertools import groupby

def find_consecutive(n : int):
    """
    정규표현식을 사용한 버전
    입력된 숫자를 문자열로 변환 -> 정규표현식 패턴에 일치하는 경우 그룹화
    """
    using = str(n)
    pattern = r"(\d)\1+"
    result = [m.group() for m in re.finditer(pattern, using)]
    return result

def find_consecutive_groupby(n : int):
    """
    itertools.groupby를 사용한 버전
    입력된 숫자를 문자열로 변환 -> groupby한 후 반복문
    반복문을 돌면서 그룹끼리 join -> key가 숫자인 경우 최종 반환할 리스트에 추가 -> 리스트 반환
    + 추가된 수정 사항
    key가 숫자 문자 인지 확인 안해도 됨. 어차피 숫자를 입력으로 받기 때문.
    """
    if type(n) != int:
        return None
    using = str(n)
    result = []
    for key, group in groupby(using):
        group_string = "".join(group)
        result.append(group_string)
    return result