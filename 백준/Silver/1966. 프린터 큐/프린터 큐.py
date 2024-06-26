# 프린터 큐

import sys
from collections import deque
input = sys.stdin.readline

def print_q():
    cnt = 1
    length = N
    while True:
        i = 1

        while i < length:
            if que[0][1] < que[i][1]:
                que.append(que.popleft())
                break
            
            i += 1
        
        else:
            if que[0][0] == M:
                return cnt
            
            else:
                que.popleft()
                length -= 1
                cnt += 1


if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        N, M = map(int, input().split())
        files = list(map(int, input().split()))
        que = deque([[i] for i in range(N)])
        for i in range(N):
            que[i].append(files[i])
        
        ans.append(str(print_q()))
    
    print("\n".join(ans))