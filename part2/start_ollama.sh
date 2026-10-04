set -euo pipefail

export OLLAMA_HOST="0.0.0.0:7777"

export OLLAMA_CONTEXT_LENGTH=8192

echo "Ollama 서버 시작: ${OLLAMA_HOST}"

mkdir -p ollama_logs
ollama serve >> ollama_logs/ollama.log 2>&1 < /dev/null & OLLAMA_PID=$!

echo "$OLLAMA_PID" > ollama_logs/ollama.pid
echo "Ollama 실행 요청 완료. PID: $OLLAMA_PID"