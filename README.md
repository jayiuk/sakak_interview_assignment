# sakak_interview_assignment

cuda 버전 : 13.0
os : ubuntu
사용한 서빙 도구 : ollama
사용한 모델 : mistral:7b

의존성 설치 : requirements.txt

## 주식회사 사각 과제테스트

### part1
- 개미수열에서 특정 항의 값의 가운데 두자리 출력
- 알고리즘의 경우 for문이 많이 사용됨(특정 공식 부재)

#### part1 실행 방법
- part1 디렉토리로 이동
- main.py 실행
- 터미널 창에 항 입력 요청 나온 부분에 항 입력
- 결과 확인

### part2
- 건강검진 데이터 기반 LLM Q&A 시스템
- 건강검진 데이터를 가져와 이를 바탕으로 질의응답이 가능하게 함

#### part2 실행 방법
- 우선 part2 디렉토리로 이동
- 모델이 설치돼지 않았다면 first_ollama_install.sh 실행
- 모델 설치 후 start_ollama.sh 실행
- service 디렉토리로 이동
- start_server.sh 실행
- 현재 확인은 postman이나 http://localhost:11432/docs에 접속하여 확인해야함

## 주의사항
- 실행 전 무조건 requirements.txt 설치 필수(part1, part2 모두)