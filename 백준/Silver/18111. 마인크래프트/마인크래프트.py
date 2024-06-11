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

        # 기준 높이보다 지면이 낮은 경우, 인벤토리에서 블럭을 꺼내 채움.
        if i < height:
            time += height - i
            inventory -= height - i

        # 기준 높이보다 지면이 높은 경우, 블록을 제거해 인벤토리에 추가.
        elif height < i:
            time += (i - height) * 2
            inventory += i - height
        
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

    # 이미 평탄화가 되어 있다면 시간에 0을 반환하고 종료.
    if max_height == min_height:
        print(0, max_height)
        exit()

    ans_time, ans_height = INF, 0

    # 모든 높이에 대하여 탐색.
    for i in range(max_height + 1):
        result = flattening(i, B)

        # 최소 시간을 갱신. 시간이 같은 경우 최대 높이만 갱신.
        if result < ans_time:
            ans_time, ans_height = result, i
        
        elif result == ans_time:
            ans_height = i

    print(ans_time, ans_height)