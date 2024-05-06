# 보석 도둑

# 단순히 둘 다 정렬하고 N^2으로 풀리나 싶었지만 어림없었음. 대충 60만에 제한시간 1초니까.
# 고민해봤지만 힙을 써야하나? 까지만 생각이 들고 어떻게 적용시킬지 와닿지 않아서 검색.
# 해답은 우선 가방은 오름차순 정렬해서 작은 순으로 보석을 넣는 그리디 방식이 맞았음.
# 보석은 무게 기준 힙에 넣음. 가방에 넣을 수 있는 보석을 모두 pop하여 가치 기준 최대 힙에 추가.
# 최대 힙에 들어있는 보석은 이후의 모든 가방에도 들어갈 수 있음. 가방마다 하나씩 pop.
# 힙에 데이터를 넣고 뺄 때는 각각 logN의 시간복잡도. 
import sys, heapq
input = sys.stdin.readline

def cal_max_price():
    result = 0
    tmp_jewels = []

    # 모든 가방에 대해서 jewels가 빌 때까지, 현재 가방보다 작은 보석을 모두 tmp_jewels에 추가.
    for b in bags:
        while jewels and b >= jewels[0][0]:
            heapq.heappush(tmp_jewels, -heapq.heappop(jewels)[1])  # 가치 기준 최대 힙.

        # 가치 기준의 최대 힙이므로 가장 높은 가치의 보석을 pop하여 결과값에 +.
        if tmp_jewels:
            result -= heapq.heappop(tmp_jewels)

        # 가방에 넣을 수 있는 보석을 모두 넣었을 때 종료.
        elif not jewels:
            break
    
    return result


if __name__ == "__main__":
    N, K = map(int, input().split())

    jewels = []
    for _ in range(N):
        heapq.heappush(jewels, list(map(int, input().split())))

    bags = [int(input()) for _ in range(K)]
    bags.sort()

    print(cal_max_price())