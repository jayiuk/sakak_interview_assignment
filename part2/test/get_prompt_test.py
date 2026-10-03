import pytest
from context.get_context import get_prompt

name = "test"
expected = "# 이건 테스트용 입니다.\n## 테스트\n### 테스트"

def test_get_start_promopt():
    assert get_prompt(name) == expected