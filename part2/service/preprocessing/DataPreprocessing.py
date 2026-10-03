import json
from typing import Dict, Any


def only_overview(before : Dict[str, Any]):
    data_dict = before.get("data")
    overview_list = data_dict["overviewList"][0]
    return overview_list