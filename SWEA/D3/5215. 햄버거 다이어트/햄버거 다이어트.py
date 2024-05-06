# 햄버거 다이어트

# dfs로 안 풀리는 줄 알고 한참 고민해서 기어코 dp로 풀어서 pass에 성공.
# 그런데 dfs로 더 빠르게 풀리는 문제였음. 상당히 허탈함.
# 풀던 도중에 dfs로 정말 안 될까? 싶어서 대충 몇 분만에 짜서 돌려봤는데 maxRecursion이 발생.
# swea는 import sys를 못 쓰니 재귀 호출 제한을 못 늘려서 안 되는 줄 알았음.
# 내가 안 됐던 이유는 dfs로 넘기는 건 어려울 게 없었는데 종료 조건을 sum_kcal > L 이거 하나만 설정했기 때문.
# i가 N에 도달한 경우에 종료가 2번째,
# 지금까지 더한 점수에 아직 확인 안 한 점수를 모두 더해도 지금까지 갱신된 max_score보다 작은 경우가 3번째였음.

def dfs(i, sum_score, sum_kcal):
    global max_score

    if i == N:
        max_score = max(max_score, sum_score)
        return
    
    if sum_score + sum(score[i:]) <= max_score:
        return
    
    if sum_kcal + kcal[i] <= L:
        dfs(i + 1, sum_score + score[i], sum_kcal + kcal[i])

    dfs(i + 1, sum_score, sum_kcal)


if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        N, L = map(int, input().split())
        score, kcal = [], []
        
        for _ in range(N):
            a, b = map(int, input().split())
            score.append(a)
            kcal.append(b)

        max_score = 0

        dfs(0, 0, 0)

        ans.append(f"#{t} {max_score}")

    print("\n".join(ans))