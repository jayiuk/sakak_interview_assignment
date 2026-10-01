"""
항을 입력하면 그 항에 해당하는 개미수열 값이 나오는 함수
반복문을 돌면서 1부터 나온 개미수열 값들을 리스트에 append
최종적으로 리스트에 맨 마지막 값을 반환
"""

from service.Consecutive import find_consecutive_groupby
from service.FormatNumber import format_number

def lookandsay(n : int):
    if n == 1:
        return n
    
    store = []
    for i in range(1, n):
        if i == 1:
            num = i
        else:
            num = store[-1]
        
        consecutive_list = find_consecutive_groupby(num)
        las_result = format_number(consecutive_list)
        store.append(las_result)
    return store[-1]

