import re
from itertools import groupby

def find_consecutive(n : int):
    using = str(n)
    pattern = r"(\d)\1+"
    result = [m.group() for m in re.finditer(pattern, using)]
    return result

def find_consecutive_groupby(n : int):
    if type(n) != int:
        return None
    using = str(n)
    result = []
    for key, group in groupby(using):
        group_string = "".join(group)
        if key.isdigit():
            result.append(group_string)
    return result