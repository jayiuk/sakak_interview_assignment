from service.llm.GetLLM import LLMInstance
import os
from dotenv import load_dotenv
import pytest

load_dotenv()
BASE = os.getenv("BASE_URL")
MODEL = os.getenv("MODEL")

@pytest.mark.asyncio
async def test_chat():
    llm = LLMInstance(BASE, MODEL)

    inputs = [
        ("system", "무조건 한국어로 답해야 합니다. 그리고 무조건 한 줄 이내로 답하세요"),
        ("human", "넌 뭐야?")
    ]

    result = await llm.chat(inputs)
    print(result.content)
    
