# 가능한 시험 점수

# dfs로 쉽게 풀리나 싶었는데 역시 d4문제. 시간초과 발생.
# 어떻게 해야할지 고민해봤는데 dp처럼 1번 반복 돌리고 그 안에서 최소한으로 다시 돌릴 수 있나? 하고 생각
# 은 했으나 방법을 찾아내지 못하고 검색. dp인 것 같긴 한데 딱 와닿진 않는 그런 방식.

# 최대 점수 + 1 길이의 0 리스트를 생성. 0점이 있기 때문에 + 1 길이.
# 결국 모든 점수에 대해서 반복을 1회 돌리고, 0점에서부터 방문한 점수를 더한 값을 새로운 리스트에 추가.
# 다음 점수 방문시 더한 값을 저장한 리스트의 요소들에 대해 반복을 돌리며 모두 더해서 다시 추가.
# 이 때 더해진 각 점수들은 최대 길이 리스트의 index로 사용할 수 있으므로, 각 점수 첫 방문시 0 -> 1로 방문 체크.
# 이후 방문 리스트의 합(1의 개수)가 곧 가능한 모든 시험 점수의 개수가 됨.

def dp():
    score_visit = [1] + [0] * sum(scores) # 최대 점수 길이의 리스트를 생성. 0점은 1로 초기화해 생성.
    score_sum = [0] 

    for s in scores: # 모든 점수를 1회 반복.

        # 0에서부터 더해가며 생성된 결과들에 대해 현재 s를 다시 더해서 모든 경우를 탐색. => O(n!). dfs는 O(n^2).
        for i in range(len(score_sum)): 
            
            # 더한 점수 = score_visit의 index이므로 이를 통해 중복 체크.
            if not score_visit[s +  score_sum[i]]:
                score_visit[s + score_sum[i]] = 1 # 방문 표시.
                score_sum.append(s + score_sum[i]) # 더한 값을 추가.

    # 방문 리스트의 합 = 초기화된 1의 개수를 리턴.
    return sum(score_visit)

if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        N = int(input())
        scores = list(map(int, input().split()))

        ans.append(f'#{t} {dp()}')
    
    print("\n".join(ans))