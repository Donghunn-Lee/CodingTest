# 마인크래프트

# 실버 2인데도 구현 문제라 조금 애먹었던 문제.
# 처음엔 투 포인터로 풀어야 하나 고민하다가 블럭을 넣고 빼는 순서를 정하는 데서 막혀 고민함.
# 결국 검색을 해서 코드는 보지 않고 전략만 읽고 힌트를 얻음. 완전 탐색으로 각 높이에서의 결과값을 모두 계산하는 것.

import sys
input = sys.stdin.readline
INF = 1e9

# 평탄화
def flattening(height, inventory):
    global ans_time
    time = 0

    # 모든 지면에 대하여 탐색.
    for i in ground:
        gap = abs(height - i)   # 현재 기준 높이와 지면의 차.

        # 기준 높이보다 지면이 낮은 경우, 인벤토리에서 블럭을 꺼내 채움.
        if i < height:
            time += gap
            inventory -= gap

        # 기준 높이보다 지면이 높은 경우, 블록을 제거해 인벤토리에 추가.
        elif height < i:
            time += gap * 2
            inventory += gap
        
        # 탐색중에 이미 현재 구한 최소 시간보다 현재 시간이 길어지는 경우 종료.
        if ans_time < time:
            return INF
    
    # 인벤토리가 음수라면 계산할 수 없는 경우이므로 INF를 반환.
    if 0 <= inventory:
        return time
    
    else:
        return INF


if __name__ == "__main__":
    N, M, B = map(int, input().split())
    ground = []
    for _ in range(N):
        ground.extend(map(int, sys.stdin.readline().split()))

    max_height = max(ground)
    min_height = min(ground)

    if max_height == min_height:
        print(0, max_height)
        exit()

    ans_time, ans_height = INF, 0

    for i in range(max_height + 1):
        result = flattening(i, B)

        if result < ans_time:
            ans_time, ans_height = result, i
        
        elif result == ans_time:
            ans_height = i

    print(ans_time, ans_height)