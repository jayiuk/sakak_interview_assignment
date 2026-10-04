cd "$(dirname "$0")"

echo "전체 실행 시작"

python -m api.MockAPI & python -m api.graph &

echo "전체 실행 종료"