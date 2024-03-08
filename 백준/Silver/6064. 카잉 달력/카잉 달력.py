# 카잉 달력 (시간 단축 필요)

import sys
input = sys.stdin.readline

# 한 사이클의 최댓값(= 최소공배수)를 구하기 위한 최대공약수 계산
def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

# 네 변수를 입력받아 해를 구하거나 해가 없음을 판별하여 반환하는 함수
def khaing_calendar(m, n, x, y):
    end_year = (m * n) // gcd(m, n) # 한 사이클, 최대공배수 계산
    target_year = (x, y)    # x, y를 변수로 쓰기 위해 타겟 년도를 저장
    y, year = x, x   # 첫째 년도인 1, 1로 초기화

    # 최댓값을 초과하면 종료
    while year <= end_year:
        # y값 조정
        if y > n:
            y %= n
            if y == 0:
                y = n

        if (x, y) == target_year :    # 현재 변수가 찾고 있는 년도인 경우 종료
            return year
        
        # x와 y를 각각 1씩 더하면 시간초과, m씩 더함
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