import sys, heapq

input = sys.stdin.readline

N  = int(input())
l_h, r_h, output= [], [], []

for _ in range(N):
    num = int(input())
    
    if len(l_h) == len(r_h):
        heapq.heappush(l_h, (-num, num)) # 최대 힙 만들기. 튜플이면 첫 원소 기준 힙 구성
    else:
        heapq.heappush(r_h, (num, num))
    
    if r_h and l_h[0][1] > r_h[0][0]:
        min = heapq.heappop(r_h)[0]
        max = heapq.heappop(l_h)[1]
        heapq.heappush(l_h,(-min, min))
        heapq.heappush(r_h,(max, max))
    
    output.append(f"{l_h[0][1]}")

sys.stdout.write('\n'.join(output))