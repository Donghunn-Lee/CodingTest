# 카잉 달력

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
    x, y, year = 1, 1, 1    # 첫째 년도인 1, 1로 초기화

    # 반복중인 변수가 찾고 있는 년도인 경우 종료
    while (x, y) != target_year:
        if year > end_year :    # 최댓값을 초과해도 종료
            return -1
        
        # x와 y를 각각 1씩 더하면 시간초과
        # 우선 x가 목푯값에 도달할 때까지 + 1
        if x == target_year[0]:
            y += m
            year += m

        # x가 목표값에 도달한 경우, 여기서부터 m씩 더하면 x는 고정, y만 변동
        # year 역시 m씩 증가
        else:
            x += 1
            y += 1
            year += 1

            # if 문이 참이면 x를 조정할 필요가 없으니 else문에서만 사용
            if x > m:
                x %= m
        
        # y값 조정
        if y > n:
            y %= n
            if y == 0:
                y = n
    
    return year


if __name__ == "__main__":
    T = int(input())
    result = []

    for _ in range(T):
        M, N, X, Y = map(int, input().split())
        result.append(khaing_calendar(M, N, X, Y))
    
    print('\n'.join(map(str, result)))