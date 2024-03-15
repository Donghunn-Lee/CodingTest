# 최대 힙

import sys, heapq
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    heap = []
    ans = []

    for i in range(N):
        x = int(input())

        if x == 0:
            if heap:
                ans.append(-heapq.heappop(heap))
            else:
                ans.append(0)
        else:
            heapq.heappush(heap, -x)
    
    sys.stdout.write("\n".join(map(str, ans)))
