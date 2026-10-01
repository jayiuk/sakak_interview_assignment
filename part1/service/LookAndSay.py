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

