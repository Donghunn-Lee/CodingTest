# ABCED
import sys
input = sys.stdin.readline

# 전체 관계도와 조사할 대상, 확인된 친구관계, 현재 명 수 를 입력
# visited를 통해 현재 루트에서 대상의 조사 확인 여부를 관리함
def dfs(rel_map, start, visited, cnt):
    global result
    if cnt == 5:
        print(1)
        sys.exit(0)
    
    for i in rel_map[start]:
        if not visited[i]:
            visited[i] = True
            dfs(rel_map, i, visited, cnt + 1)
            visited[i] = False
        

# 메인에서는 입력된 명수만큼의 빈 리스트를 가진 리스트를 생성
# rel[0]에 0의 친구들을 모두 입력하는 방식으로 이차원 리스트 relationship을 생성
if __name__ == '__main__':
    N, M = map(int, input().split())
    relationship = [[] for _ in range(N)]
    visited = [False] * N
    result = False
    
    for i in range(M):
        a, b = map(int, input().split())
        relationship[a].append(b)
        relationship[b].append(a)

    # ABCDE중 시작인 A를 0번 부터 N - 1 번까지 각각 대입
    # dfs에서 i번째를 A로 삼아 나머지 친구들을 계산함
    for i in range(N):
        visited[i] = True
        dfs(relationship, i, visited, 1)
        visited[i] = False
    
    print(0)