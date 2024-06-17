# 연산자 끼워넣기

import sys
input = sys.stdin.readline

def dfs(num, cur_result):
    global ans_max, ans_min

    if num == N:
        ans_max = max(ans_max, cur_result)
        ans_min = min(ans_min, cur_result)
        return

    for i in range(4):
        if 0 < operator[i]:
            operator[i] -= 1

            if i == 0:
                nxt_result = cur_result + seq[num]
            elif i == 1:
                nxt_result = cur_result - seq[num]
            elif i == 2:
                nxt_result = cur_result * seq[num]
            else:
                nxt_result = int(cur_result / seq[num])

            dfs(num + 1, nxt_result)

            operator[i] += 1


if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    operator = list(map(int, input().split()))
    ans_max, ans_min = -1e10, 1e10

    dfs(1, seq[0])

    print(ans_max)
    print(ans_min)