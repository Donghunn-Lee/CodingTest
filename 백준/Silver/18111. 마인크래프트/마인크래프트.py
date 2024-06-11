# 마인크래프트

# 실버 2인데도 구현 문제라 조금 애먹었던 문제.
# 처음엔 투 포인터로 
import sys
input = sys.stdin.readline
INF = 1e11

def flattening(height, inventory):
    global ans_time
    time = 0

    for i in ground:
        gap = abs(height - i)

        if i < height:
            time += gap
            inventory -= gap
        elif height < i:
            time += gap * 2
            inventory += gap
        
        if ans_time < time:
            return False
    
    if 0 <= inventory:
        return time
    
    else:
        return False


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

        if result != False:
            if result < ans_time:
                ans_time, ans_height = result, i
            
            elif result == ans_time:
                ans_height = i

    print(ans_time, ans_height)