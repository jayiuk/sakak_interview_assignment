import json
import re

def parsing_json_response(llm_result):
    json_start = llm_result.find('{')
    json_end = llm_result.rfind('}') + 1
    if json_start >= 0 and json_end > json_start:
        result = json.loads(llm_result[json_start:json_end])
    
    return result