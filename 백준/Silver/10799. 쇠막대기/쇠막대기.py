# 쇠막대기
import sys
input = sys.stdin.readline

S = input()

# 쇠막대 위치와 레이저를 쏘일 위치를 계산하여 각각 반환하는 함수.
def positioning(s):
    i = 0
    sticks, left, rasor = [], [], []
    N = len(s)

    while i < N:
        # (를 발견하면 left에 쇠막대의 시작점을 저장.
        # 레이저인지 확인을 위해 다음 요소를 체크후 레이저라면 저장.
        # )를 발견하면 맞물리는 쇠막대의 시작점을 찾기 위해 left에서 pop.
        # 쇠막대 시작점과 끝점을 리스트로 저장.
        if s[i] == '(':
            if i < N - 2 and s[i + 1] == ')':
                rasor.append(i)
                i += 1
            else:
                left.append(i)
        elif s[i] == ')':
            sticks.append([left.pop(), i])

        i += 1
    # 주어진 쇠막대들의 양 끝점이 저장된 리스트와 레이저의 위치를 반환
    return sticks, rasor

# 주어진 타겟의 양 끝점 위치와 레이저를 쏠 포인트를 받아 조각을 계산하여 반환하는 함수.
def cutting(target, point):
    # 주어진 막대의 처음 개수를 result에 저장.
    result = len(target)

    # 포인트가 대상의 양 끝점 사이에 있는 경우 (= 레이저에 절단되는 쇠막대 수)를 tmp에 저장.
    for r in point:
        tmp = 0
        for left_end, right_end in target:
            if left_end < r < right_end:
                tmp += 1
        result += tmp
    
    # 절단 후 총 개수를 반환
    return result

sticks_num, rasor_point = positioning(S)

print(cutting(sticks_num, rasor_point))