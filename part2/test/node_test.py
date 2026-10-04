import pytest
from service.llm.StartNode import start_node
from service.llm.Mapping import MappingNode
from service.llm.GetLLM import LLMInstance
from service.llm.total_explain import TotalExplain
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

mapping_query = "간 수치 어때?"
mapping_expected = {
    "mapping_result" : ["AST", "ALT", "yGPT"]
}

te_query = "내 건강검진 결과 어때?"

@pytest.mark.asyncio
async def test_start_node():
    
    llm = LLMInstance(BASE, MODEL)
    node = start_node(llm)
    assert await node.generate(query) == expected
    
  
@pytest.mark.asyncio
async def test_mapping_node():
  llm = LLMInstance(BASE, MODEL)
  node = MappingNode(llm)
  assert await node.generate(mapping_query) == mapping_expected
  

@pytest.mark.asyncio
async def test_total_explain():
    llm = LLMInstance(BASE, MODEL)
    node = TotalExplain(llm)
    result = await node.generate(te_query)
    print(result)