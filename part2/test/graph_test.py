from service.llm.orchestrator import AIGraph
import pytest
import os
from dotenv import load_dotenv
from service.llm.GetLLM import LLMInstance

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
MODEL = os.getenv("MODEL")

@pytest.mark.asyncio
async def test_graph():
    llm = LLMInstance(BASE_URL, MODEL)
    graph = AIGraph(llm)
    result = await graph.generate(query = "bmi 수치 괜찮아?")
    print(result)