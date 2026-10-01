"""
1번 문제 최종 실행 함수
이 파일 실행 시 3 초과 100 미만의 숫자를 입력하면 그 항의 개미수열 값의 가운데 두자릿수 출력
해당 범위 준수하지 않을 땐 ValueError가 나옴.
"""


from service.GetLookandsayMiddleNums import get_lookandsay_middle_nums


def part1_final(n : int):
    try:
        las_value = get_lookandsay_middle_nums(n)
        return las_value
    except ValueError as e:
        raise(e)
    
if __name__ == "__main__":
    print(part1_final(int(input("3 초과, 100 미만 숫자 하나를 입력하세요 : "))))