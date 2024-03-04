# ABCED
import copy

# 현재 확인된 친구 관계 리스트와 조사할 다음 대상을 입력
# 깊은복사로 리스트를 넘겨서 아직 조사하지 않은 대상을 찾아가며 추가하는 함수
# 확인된 관계가 5명인 경우 result에 True를 할당하고 종료
def dfs(c, n, l):
    global result
    if result or l == 5:
        result = True
        return
    
    for j in relationship[n]:
        connected = copy.deepcopy(c)
        if j not in connected:
            connected.append(j)
            dfs(connected, j, l + 1)

# 메인에서는 입력된 명수만큼의 빈 리스트를 가진 리스트를 생성
# rel[0]에 0의 친구들을 모두 입력하는 방식으로 이차원 리스트 relationship을 생성
if __name__ == '__main__':
    N, M = map(int, input().split())
    relationship = [[] for _ in range(N)]
    result = False
    
    for i in range(M):
        a, b = map(int, input().split())
        relationship[a].append(b)
        relationship[b].append(a)
    
    # 시간 단축을 위해 친구 관계가 적은 사람부터 조사하기 위해 order 리스트 생성
    # 친구 관계가 적을수록 해당 사람이 ABCDE 중 A 또는 E일 가능성이 높기 때문
    order = []
    for i in range(N):
        order.append([i, len(relationship[i])])
    order.sort(key = lambda order: order[1])
    
    # ABCDE중 시작인 A를 0번 부터 N - 1 번까지 각각 대입
    # dfs에서 i번째를 A로 삼아 나머지 친구들을 계산함
    for i, j in order:
        if result:
            print(1)
            break
        else:
            dfs([i], i, 1)

    if not result:
        print(0)