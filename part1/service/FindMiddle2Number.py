"""
숫자에서 가운데 2개 숫자를 구하는 함수
여기서 입력값 n의 자릿수가 홀수인 경우는 고려하지 않음
개미수열은 첫번째 값 제외하고는 다 짝수가 나오기 때문
"""


def find_middle_nums(n : str):
    """
        수열의 가운데 값 두개를 구하는 함수
        해당 문제에서 수열은 개미수열 이므로 해당 수열의 자릿수가 홀수인 경우를 고려하지 않음
        문자열로 변경 -> 길이 구함 -> 길이에서 2를 나눠 그 값을 anchor로 설정 -> 문자열 anchor-1번째와 anchor번째 값을 구한 후 이 둘을 합침(더하기 아님)
        최종적으로 다시 숫자로 바꿔서 반환
    """
    
    length = len(n)
    anchor = length // 2
    first_target, second_target = n[anchor-1], n[anchor]
    result = int(first_target + second_target)
    return result