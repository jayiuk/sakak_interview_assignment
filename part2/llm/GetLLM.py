from langchain_ollama import ChatOllama

class LLMInstance:
    def __init__(self, base_url, model, temperature : float = 0.1):
        self.llm = ChatOllama(base_url = base_url, model = model, temperature = temperature)
    
    async def chat(self, input):
        return await self.llm.ainvoke(input)