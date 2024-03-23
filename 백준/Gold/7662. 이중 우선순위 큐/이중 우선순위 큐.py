# 이중 우선순위 큐

import sys, heapq
input = sys.stdin.readline

def insert_pQ(n):
    heapq.heappush(min_heap, n)
    heapq.heappush(max_heap, -n)
    
    if n in nums:
        nums[n] += 1
    else:
        nums[n] = 1

def pop_pQ(c):
    if not nums:
        return
    
    if c == '1':
        while -max_heap[0] not in nums:
            heapq.heappop(max_heap)
        tmp = -heapq.heappop(max_heap)
    
    if c == '-1':
        while min_heap[0] not in nums:
            heapq.heappop(min_heap)
        tmp = heapq.heappop(min_heap)

    if 2 <= nums[tmp] :
        nums[tmp] -= 1
    else:
        del nums[tmp]


if __name__ == "__main__":
    T = int(input())
    ans = []
    for _ in range(T):
        k = int(input())
        max_heap = []
        min_heap = []
        nums = dict()

        for i in range(k):
            C, N = input().rstrip().split()

            if C == 'I':
                insert_pQ(int(N))
            elif C == 'D':
                pop_pQ(N)
    
        if nums:
            ans.append(f"{max(nums)} {min(nums)}")
        else:
            ans.append("EMPTY")
            
    print("\n".join(ans))