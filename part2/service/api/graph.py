from llm.GetLLM import LLMInstance
from llm.orchestrator import AIGraph
from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
MODEL = os.getenv("MODEL")

llm = LLMInstance(BASE_URL, MODEL)
graph = AIGraph(llm)

router = FastAPI()

@router.post("/api/generate")
async def chatting(query : str):
    response = await graph.generate(query)
    return response


if __name__ == "__main__":
    uvicorn.run(router, host="0.0.0.0", port=11432)
