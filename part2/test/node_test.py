import pytest
from llm.StartNode import start_node
from llm.GetLLM import LLMInstance
import os
from dotenv import load_dotenv

load_dotenv()

BASE = os.getenv("BASE_URL")
MODEL = os.getenv("MODEL")

query = "bmi 수치 괜찮아?"

expected = {
  "question" : f"{query}",
  "intent" : ["MEDICAL"],
  "execution_plan" : [
    {"node" : "data_node"},
    {"node" : "is_normal_node"}
  ],
}

@pytest.mark.asyncio
async def test_start_node():
    
    llm = LLMInstance(BASE, MODEL)
    node = start_node(llm)
    assert await node.generate(query) == expected
    