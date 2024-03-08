# 카잉 달력 (시간 단축 필요)

import sys
input = sys.stdin.readline

# 최소공배수를 구하기 위한 최대공약수 계산
def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

# 네 변수를 입력받아 해를 구하거나 해가 없음을 판별하여 반환하는 함수
# 1씩 더하면 시간초과가 나므로, x를 고정시킨 후 그 배수로 y를 구하는 방식으로
def khaing_calendar(m, n, x, y):
    end_year = (m * n) // gcd(m, n) # 최댓값(= 한 사이클, = m, n의 최소공배수) 계산
    target_year = y    # 구하는 목푯값인 y를 저장
    y, year = x, x   # m씩 더하며 답을 찾기 위해 x를 기준으로 year를 초기화

    # 최댓값을 초과하면 종료
    while year <= end_year:

        # x는 고정이므로 y값만 조정
        if y > n:
            y %= n
            if y == 0:
                y = n

        # 현재 변수가 찾고 있는 년도인 경우 종료
        if y == target_year :
            return year
        
        y += m
        year += m
    
    return -1


if __name__ == "__main__":
    T = int(input())
    result = []

    for _ in range(T):
        M, N, X, Y = map(int, input().split())
        result.append(khaing_calendar(M, N, X, Y))
    
    print('\n'.join(map(str, result)))