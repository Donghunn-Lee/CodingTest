# 햄버거 다이어트

def best_burger():
    dp = {0 : 0}

    for score, kcal in score_and_kcal:
        tmp = dict()

        for l_k in dp:
            n_s, n_k = dp[l_k] + score, l_k + kcal

            if n_k > L:
                continue
            
            if tmp.get(n_k):
                tmp[n_k] = max(tmp[n_k], n_s)
            else:
                tmp[n_k] = n_s
        
        for t in tmp:
            if dp.get(t):
                dp[t] = max(dp[t], tmp[t])
            else:
                dp[t] = tmp[t]
    
    return max(dp.values())

if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        N, L = map(int, input().split())
        score_and_kcal = [list(map(int, input().split())) for _ in range(N)]

        ans.append(f"#{t} {best_burger()}")

    print("\n".join(ans))