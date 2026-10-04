# 건강검진 설명 AI Assistant

## 설명
- Mock API에 있는 건강검진 데이터를 가져와 이를 바탕으로 설명해주는 AI Assistant

## 구성요소

### node
- 각각의 노드는 특정한 역할을 수행
- start_node : 사용자의 입력에 대한 의도 분류, 사용해야할 노드 생성 및 워크플로우 생성
- mapping_node : 사용자의 입력에 특정 항목에 대한 설명이 필요할 경우 특정 항목과 사용자 입력에 있는 항목과 매칭
- explain_node : 건강검진 데이터(전체 혹은 특정항목)를 바탕으로 설명해주는 데이터
- is_normal_node : 건강검진 데이터(전체 혹은 특정항목)가 정상인지 비정상인지 판별
- specific_explain_node : 특정 항목의
- answer_node : 마무리 결과 생성