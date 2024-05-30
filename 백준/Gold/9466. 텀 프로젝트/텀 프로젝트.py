# 팀 프로젝트

# dfs로 풀어야 한다는 사실을 파악하고 풀어보려 했으나 조금 어렵게 생각해서 금방 풀지 못한 문제.
# 처음엔 탐색을 처음 시작한 값을 계속해서 재귀로 넘기고, 그 값이 재등장했을 때 만들어진 팀을 추가하는 방식으로 구현.
# 하지만 이렇게 하면 문제는 풀려도 모든 학생들을 시작점으로 해서 완전탐색을 해야 하므로 거의 끝에서 시간초과 발생.
# index를 생각하긴 했는데, 조금 모자라고 시간도 이미 너무 많이 써서 찾아보니 index로 훨씬 간단하게 풀 수 있었음.

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(cur):
    global teamed_up

    visited[cur] = 1        # 방문 체크.
    team.append(cur)        # 팀 구성.
    nxt = students[cur]     # 현재 학생이 지목한 다음 학생.

    # 다음 학생을 아직 방문하지 않은 경우, 탐색 진행.
    if not visited[nxt]:
        dfs(nxt)

    # 다음 학생을 이미 방문했고, 그 학생이 지금 구성중인 팀에 들어 있는 경우에 사이클이 발생했음을 알 수 있음.
    elif nxt in team:
        # 학생 번호는 중복되지 않으므로, index를 써서 해당 학생 이후로 추가된 학생의 수만큼을 팀이 구성된 인원에 더함.
        teamed_up += len(team[team.index(nxt) : ])

if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        N = int(input())
        students = [0] + list(map(int, input().split()))
        visited = [0] * (N + 1)
        teamed_up = 0

        # 아직 방문하지 않은 학생들을 순서대로 탐색.
        # 여기서 이미 팀이 구성되거나 팀을 이룰 수 없음이 확인된 학생들은 모두 방문 처리 됐으므로 가지치기가 이뤄짐.
        for i in range(1, N + 1):
            if not visited[i]:
                team = []
                dfs(i)
        
        ans.append(str(N - teamed_up))
    
    print("\n".join(ans))