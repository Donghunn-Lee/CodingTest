# 이중 우선순위 큐

# 처음엔 하나의 리스트를 생성하고, 값을 넣을 때마다 이중 분할 탐색으로 정렬된 위치에 값을 넣으려고 시도.
# 물론 시간초과. 그 다음 최대 최소 힙을 동시에 사용하는 방법은 생각했으나, 삭제 후 동기화 할 방법을 못 찾음.
# 결국 검색. 힙을 사용하는 접근은 맞았고, 삭제된 값을 동기화시키는 수단으로 리스트나 딕셔너리가 필요했음.
# 딕셔너리가 더 효율적인 듯해서 딕셔너리를 사용.

import sys, heapq
input = sys.stdin.readline

# 값을 두 힙에 추가하는 함수.
def insert_pQ(n):
    heapq.heappush(min_heap, n)
    heapq.heappush(max_heap, -n)
    
    # 값 추가시 입력값을 키로 하고 값에 1을 할당.
    # 여기서 중복으로 딕셔너리에 이미 키가 있는 경우 + 1.
    if n in nums:
        nums[n] += 1
    else:
        nums[n] = 1

# 값을 제거하는 함수.
def pop_pQ(c):
    if not nums:
        return
    
    # 최댓값을 제거해야 할 경우, 최대 힙에서 nums 에 없는 값(반대쪽 힙에서 제거된 수)은 삭제.
    # nums에 값이 있다면 허수가 아니므로 heappop. nums에서도 확인해야 하므로 tmp에 저장.
    if c == '1':
        while -max_heap[0] not in nums:
            heapq.heappop(max_heap)
        tmp = -heapq.heappop(max_heap)
    
    # 동일한 구조.
    if c == '-1':
        while min_heap[0] not in nums:
            heapq.heappop(min_heap)
        tmp = heapq.heappop(min_heap)

    # nums의 값이 1이었다면 nums 에서도 delete.
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