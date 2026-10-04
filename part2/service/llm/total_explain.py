from context.get_context import get_prompt
from preprocessing.parsing_result import parsing_json_response
from preprocessing.DataPreprocessing import only_overview
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

BASE_MOCK_API = os.getenv("BASE_MOCK_API")


class TotalExplain:
    def __init__(self, llm):
        self.llm = llm
        self.name = "total_explain"
    
    def get_data(self, patient_id : int):
        MOCK_API = BASE_MOCK_API + "/" + str(patient_id)
        response = requests.get(MOCK_API)
        response.raise_for_status()
        data = response.json()
        data_fin = only_overview(data)
        return data_fin
    
    def build_system_prompt(self):
        system_prompt = get_prompt(self.name)
        return system_prompt
    
    def build_messages(self, query : str):
        data = self.get_data(patient_id = 1)
        system_prompt = self.build_system_prompt()
        context = (json.dumps(data, ensure_ascii = False))
        messages = [
            ("system", system_prompt),
            ("human", context),
            ("human", query)
        ]
        return messages
    
    async def generate(self, query : str):
        messages = self.build_messages(query)
        response = await self.llm.chat(messages)
        response_json = response.content
        print(response_json)
        result = parsing_json_response(response_json)
        return result