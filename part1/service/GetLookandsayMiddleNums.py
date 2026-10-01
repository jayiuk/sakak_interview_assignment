"""
최종 함수
항을 입력하면 그 항의 개미수열의 가운데 숫자 2개 출력
"""
from service.LookAndSay import lookandsay
from service.FindMiddle2Number import find_middle_nums

def get_lookandsay_middle_nums(n : int):
    if n <= 3 or n >= 100:
        raise ValueError("조건에 벗어나는 값입니다. 3 초과 100 미만 값으로 하세요.")
    look_and_say_value = lookandsay(n)
    middles = find_middle_nums(look_and_say_value)
    return middles