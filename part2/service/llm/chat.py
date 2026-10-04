import os
from dotenv import load_dotenv
from service.context.get_context import get_prompt
from service.preprocessing.parsing_result import parsing_json_response


load_dotenv()

class Chat:
    def __init__(self, llm):
        self.llm = llm
        self.name = "chat"
    
    def build_system_prompt(self):
        system_prompt = get_prompt(self.name)
        return system_prompt
    
    async def generate(self, query : str):
        messages = [
            ("system", self.build_system_prompt()),
            ("human", query)
        ]
        response = await self.llm.chat(messages)
        response_json = response.content
        print(response_json)
        result = parsing_json_response(response_json)
        return result
