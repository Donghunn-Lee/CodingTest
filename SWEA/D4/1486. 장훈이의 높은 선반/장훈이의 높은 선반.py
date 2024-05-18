# 장훈이의 높은 선반

# 2^N 문제인가 싶었는데 딱 N 개수가 20이어서 맞는 듯? 하고 풀었음.
# 거의 비슷한 유형의 문제를 몇 개 풀어본 덕에 쉽게 풀 수 있었음.
# 이번엔 집합을 사용함. 같은 값이 많이 나올 것 같아서.
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