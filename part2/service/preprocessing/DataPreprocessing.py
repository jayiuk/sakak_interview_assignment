import json
from typing import Dict, Any, List


def get_data_part(before : Dict[str, Any]):
    result = before.get("data")
    return result

def only_overview(before : Dict[str, Any]):
    data_dict = get_data_part(before)
    overview_list = data_dict["overviewList"][0]
    return overview_list

def only_unit(before : Dict[str, Any]):
    data_dict = get_data_part(before)
    unit = data_dict["referenceList"][0]
    return unit

def only_normal_A(before : Dict[str, Any]):
    data_dict = get_data_part(before)
    normal_a = data_dict["referenceList"][1]
    return normal_a

def only_normal_B(before : Dict[str, Any]):
    data_dict = get_data_part(before)
    normal_b = data_dict["referenceList"][2]
    return normal_b

def only_suspected(before : Dict[str, Any]):
    data_dict = get_data_part(before)
    return data_dict["referenceList"][-1]

def only_result_list(before : Dict[str, Any]):
    data_dict = get_data_part(before)
    return data_dict["resultList"][0]

def get_name(before : Dict[str, Any]):
    data_dict = get_data_part(before)
    return data_dict["patientName"]

def get_specific_result(before : Dict[str, Any], specific_list = List[str]):
    overview = only_overview(before)
    result= {}
    for s in specific_list:
        specific_result = int(overview.get(s))
        result[s] = specific_result
    return result