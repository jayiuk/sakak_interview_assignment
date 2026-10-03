from llm.GetLLM import LLMInstance
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
        ("system", "당신은 한국어로 입력된 헬스케어 단어를 영어로 번역해야 합니다. 딱 그 단어만 바꾸세요."),
        ("human", "콜레스테롤")
    ]

    result = await llm.chat(inputs)
    print(result.content)