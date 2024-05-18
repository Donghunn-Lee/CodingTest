# 장훈이의 높은 선반

def best_tower():
    dp = {0}

    for h in heights:
        tmp = set()

        for d in dp:
            tmp.add(d + h)
        
        dp |= tmp

    gap = 1e6

    for d in dp:
        if 0 <= d - B:
            gap = min(gap, d - B)

            if gap == 0:
                return 0
    
    return gap


if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        N, B = map(int, input().split())
        heights = list(map(int, input().split()))

        ans.append(f'#{t} {best_tower()}')

    print("\n".join(ans))