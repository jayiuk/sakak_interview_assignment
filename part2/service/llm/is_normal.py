from service.context.get_context import get_prompt
from service.preprocessing.parsing_result import parsing_json_response
import os
from dotenv import load_dotenv
import json
from service.preprocessing.DataPreprocessing import get_specific_normal_a,get_specific_normal_b, get_specific_result, get_specific_suspected
from typing import List, Dict, Any
import requests

load_dotenv()

BASE_MOCK_API = os.getenv("BASE_MOCK_API")

class IsNormal:
    def __init__(self, llm):
        self.llm = llm
        self.name = "is_normal"
    
    def get_data(self, patient_id, specific_list : Dict[str, Any]):
        MOCK_API = BASE_MOCK_API + "/" + str(patient_id)
        response = requests.get(MOCK_API)
        response.raise_for_status()
        original = response.json()
        mapped_list = specific_list["mapping_result"]
        specific_result = get_specific_result(original, mapped_list)
        specific_normal_a = get_specific_normal_a(original, mapped_list)
        specific_normal_b = get_specific_normal_b(original, mapped_list)
        specific_suspected = get_specific_suspected(original, mapped_list)
        
        specific_data = {"checkup" : specific_result, "referenceList" : [specific_normal_a, specific_normal_b, specific_suspected]}
        return specific_data
    
    def build_system_prompt(self):
        system_prompt = get_prompt(self.name)
        return system_prompt
    
    def build_messages(self, specific_list : Dict[str, Any], query : str):
        data = self.get_data(patient_id = 1, specific_list = specific_list)
        context = (json.dumps(data, ensure_ascii = False))
        messages = [
            ("system", self.build_system_prompt()),
            ("human", context),
            ("human", query)
        ]
        return messages
    
    async def generate(self, specific_list : Dict[str, Any], query : str):
        messages = self.build_messages(specific_list, query)
        response = await self.llm.chat(messages)
        response_json = response.content
        print(response_json)
        result = parsing_json_response(response_json)
        return result