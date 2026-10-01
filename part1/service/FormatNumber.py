from typing import List



def format_number(numbers : List[str]):
    result_list = []
    for num in numbers:
        a = str(len(num))
        b = num[0]
        number = a + b
        result_list.append(number)
    result_str = "".join(result_list)
    result = int(result_str)
    return result