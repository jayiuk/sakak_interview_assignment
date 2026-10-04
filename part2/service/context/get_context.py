import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

def get_prompt(node_name : str):
    base_path = os.getenv("PROMPT_PATH")
    node_prompt_path = Path(base_path + "/" + node_name + ".md")
    if os.path.isabs(node_prompt_path) == False:
        node_prompt_path = node_prompt_path.resolve()
    
    return node_prompt_path.read_text(encoding = "utf-8").strip()
    