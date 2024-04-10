# 절댓값 힙

import sys, heapq
input = sys.stdin.readline

def abs_heap(cmd):
    q = []
    ans = []

    for c in cmd:
        if c:
            heapq.heappush(q, (abs(c), c))
        else:
            if q:
                ans.append(str(heapq.heappop(q)[1]))
            else:
                ans.append('0')
    
    print('\n'.join(ans))


if __name__ == "__main__":
    N = int(input())
    cal_info = [int(input()) for _ in range(N)]

    abs_heap(cal_info)