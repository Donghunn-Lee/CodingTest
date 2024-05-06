# 햄버거 다이어트

# dfs는 당연히 시간초과 날 것 같아서 정렬이나 dp를 잘 사용해야겠다고 생각함.
# 그런데 dp를 어떻게 해야할 지 몰라서 한참 고민.
# 최근 풀었던 '가능한 시험 점수' 문제처럼 0에서부터 score를 더해가며 결과값을 리스트에 저장,
# 그 결과값 리스트의 모든 요소에 현재의 score를 모두 더하고 그 결과를 다시 저장하는 방식이면 풀릴 거라고 판단.
# 리스트 대신 딕셔너리를 사용. 그 딕셔너리를 for문으로 돌리고 내부에서 요소를 추가하니
# dictionary changed size during iteration 에러 발생.
# 시험 점수 문제는 시험 점수라는 하나의 도메인만 계산하지만 이 문제는 kcal가 있어서 length로 반복을 하기 어려웠음.
# 그래서 생각한 건 결과값을 바로 추가하지 않고 임시 딕셔너리를 만들어 결과값의 for문이 끝난 뒤 추가하는 방식으로 진행.
# 제출 결과는 pass. 하지만 더 간단한 방법이 분명 있을 거라고 생각함. 

# ㅋㅋㅋ dfs로 풀리는 문제였음. 고민하다가 dfs로 정말 안 될까? 싶어서 대충 몇 분만에 짜서 돌려봤는데 maxRecursion이 뜨기에 swea는 import sys를 못 쓰니 안될 줄 알았는데 됨. 내가 종료 조건을 kcal > L 하나만 설정해서 그런 거였음.

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