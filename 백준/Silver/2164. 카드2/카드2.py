# 카드2

import sys
from collections import deque
input = sys.stdin.readline

def sol(n):
    deq = deque([i for i in range(1, N + 1)])

    while 1 < len(deq):
        deq.popleft()
        deq.append(deq.popleft())

    return deq[0]


if __name__ == "__main__":
    N = int(input())

    print(sol(N))