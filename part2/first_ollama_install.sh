set -euo pipefail

export OLLAMA_HOST="127.0.0.1:7777"

ollama pull mistral:7b
ollama list