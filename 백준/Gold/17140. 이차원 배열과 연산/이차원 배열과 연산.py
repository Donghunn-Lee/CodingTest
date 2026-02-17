# 17140 이차원 배열과 연산

# counter와 전치를 잘 활용해야 하는 정렬 문제
# 

import sys
from collections import Counter
input = sys.stdin.readline

def r_sort(arr):
    counter = Counter(arr)
    counter.pop(0, None)  # 0 제거

    items = sorted(counter.items(), key=lambda x: (x[1], x[0]))

    new_arr = []
    for num, cnt in items:
        new_arr.append(num)
        new_arr.append(cnt)

    return new_arr[:100]

def transpose(A):
    return list(map(list, zip(*A)))

def solve():
    r, c, k = map(int, input().split())
    r -= 1
    c -= 1

    A = [list(map(int, input().split())) for _ in range(3)]

    time = 0

    while time <= 100:
        if r < len(A) and c < len(A[0]) and A[r][c] == k:
            print(time)
            return

        r_len = len(A)
        c_len = len(A[0])
        max_len = 0

        # R 연산
        if r_len >= c_len:
            for i in range(r_len):
                A[i] = r_sort(A[i])
                max_len = max(max_len, len(A[i]))
                
            for i in range(len(A)):
              A[i].extend([0] * (max_len - len(A[i])))

        # C 연산
        else:
            A = transpose(A)
            for i in range(len(A)):
                A[i] = r_sort(A[i])
                max_len = max(max_len, len(A[i]))

            # 0으로 패딩
            for i in range(len(A)):
              A[i].extend([0] * (max_len - len(A[i])))

            A = transpose(A)

        

        time += 1

    print(-1)

if __name__ == '__main__':
    solve()
