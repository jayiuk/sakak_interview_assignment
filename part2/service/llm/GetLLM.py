from langchain_ollama import ChatOllama
from ollama import ResponseError
import asyncio

"""
repeat_error를 방지하기 위해 재시도 최대 3번까지 하도록 구현
"""


class LLMInstance:
    def __init__(self, base_url, model, temperature : float = 0.1, format = "json", repeat_penalty = 1.1):
        self.llm = ChatOllama(base_url = base_url, model = model, temperature = temperature, format = format, repeat_penalty = repeat_penalty)
    
    async def chat(self, input, max_iter = 2):
        if max_iter < 0:
            raise ValueError("재시도 횟수 초과됐습니다.")
        for i in range(max_iter + 1):
            try:
                return await self.llm.ainvoke(input)
            except ResponseError as e:
                repeat_error = ("prediction aborted, token repeat" in str(e))
            
                if not repeat_error or i == max_iter:
                    raise
                
                await asyncio.sleep(1)
            
            