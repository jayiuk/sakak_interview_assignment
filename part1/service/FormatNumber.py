"""
리스트를 개미수열처럼 나오게 바꿔주는 함수
개미수열은 앞에는 연속된 같은 숫자의 개수, 뒤에는 그 숫자 하나
연속된 같은 숫자는 같은 문자열로 묶여있으니 이를 개미수열처럼 바꿔서 하나의 숫자로 반환
"""

from typing import List

def format_number(numbers : List[str]):
    """
    num의 길이의 결과값 타입은 우선 문자열로 바꿔야됨
    그래야 그 숫자와 길이를 하나로 합칠 수 있음(더하기 아님)
    """
    
    result_list = []
    for num in numbers:
        a = str(len(num))
        b = num[0]
        number = a + b
        result_list.append(number)
    result_str = "".join(result_list)
    result = int(result_str)
    return result