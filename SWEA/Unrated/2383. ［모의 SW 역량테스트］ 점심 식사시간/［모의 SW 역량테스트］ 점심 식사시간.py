# 점심 식사시간

# 매우 힘겹게 풀다가 결국 포기하고 며칠 뒤 다시 도전해서 간신히 풀어낸 문제.
# 이전 풀이에서 grouping 하는 부분까진 거의 같지만, 계단을 내려가는 구조에서 그땐 for문을 되게 잡다하게 썼는데
# 이번엔 따로 계단을 내려가는 리스트도 만들지 않고 원래 그룹 리스트에서 음수로 계단의 층수를 표기해서 단순화.
# 또한 거리 계산을 이전엔 move를 실행하는 매번 생성된 그룹에 대해 계산했었는데, 한 번에 전부 계산하여 사용해서 또 단축.

# 방에 있는 사람들의 좌표와 계단의 좌표를 구하는 함수.
def get_room_pos(room):
    people = []
    stairs = []

    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                people.append((i, j))
            elif 1 < room[i][j]:
                stairs.append((i, j, room[i][j]))
                
    return people, stairs


# 사람이 각각 1번, 2번 계단으로 갈 때의 시간(거리)를 구하는 함수.
def get_time_costs(people):
    time_costs = []

    for i, j in people:
        a = abs(i - stairs[0][0]) + abs(j - stairs[0][1])
        b = abs(i - stairs[1][0]) + abs(j - stairs[1][1])
        time_costs.append((a, b))

    return time_costs


# 만들어진 그룹에 대해 탐색을 진행.
def move(group_1, group_2, num_people):
    global min_count
    count = 0

    # 모든 사람이 계단을 빠져나갈 때까지 반복.
    while 0 < num_people:

        # 구한 최소 시간보다 현재 분기의 시간이 더 긴 경우 바로 종료.
        if min_count < count:
            return
        
        on_stairs_1, on_stairs_2 = 0, 0     # 계단 리스트를 만드는 대신 현재 계단 위에 있는 사람의 수를 계산.
        escape_1, escape_2 = 0, 0           # 리스트 갱신을 위해 사람이 빠져나간 경우, 그 시간에 나간 인원을 체크.
        count += 1      # 경과 시간.

        # 1번 그룹 이동.
        for i in range(len(group_1)):
            cur = group_1[i]

            # 계단 입구에 도착 후 내려간 시간을 0에서 1씩 뺀 음수로 확인.
            # 계단 길이가 10일 때 현재 값이 -10이면 계단 이동 완료.

            # 계단 이동 완료를 첫 if문으로 체크. 이 때 on_stairs를 증가시키지 않음.
            if cur == -stairs[0][2]:
                escape_1 += 1   # 탈출 인원 수 + 1.
            
            # 현재 값이 0이거나 음수일 때(= 이미 내려가는 중), 3명까지 내려갈 수 있으므로 on_stairs 상태를 확인.
            # 그룹 생성시 정렬을 해 뒀기 때문에, 가장 가까웠던 사람이 먼저 실행되므로 인원 체크 가능.
            # 계단을 내려가는 인원이 3명 이하인 경우 계단 이동 시작.
            elif cur <= 0 and on_stairs_1 < 3:
                group_1[i] -= 1     
                on_stairs_1 += 1

            # 아직 계단 입구에 도달하지 못한 경우, 계단을 향해 이동.
            elif 0 < cur:
                group_1[i] -= 1

        # 1분의 탐색이 끝나면 탈출한 인원 수를 바탕으로 리스트를 갱신. 탈출 총 인원 수 역시 갱신.
        if escape_1 != 0:
            group_1 = group_1[escape_1:]
            num_people -= escape_1

        # 2번 그룹에 대해 위와 같은 알고리즘 실행.
        for i in range(len(group_2)):
            cur = group_2[i]
            
            if cur == -stairs[1][2]:
                escape_2 += 1
            elif cur <= 0 and on_stairs_2 < 3:
                group_2[i] -= 1
                on_stairs_2 += 1
            elif 0 < cur:
                group_2[i] -= 1

        if escape_2 != 0:
            group_2 = group_2[escape_2:]
            num_people -= escape_2

    # 반복 종료시 전역변수 min_count를 초기화.
    min_count = min(min_count, count)


# 가능한 모든 그룹을 생성하고, 만든 그룹을 오름차순 정렬해 move 함수를 호출하여 탐색을 진행하는 함수.
def grouping(group_1, group_2, num):
    if num == num_people:
        move(sorted(group_1), sorted(group_2), num_people)
        return
    
    group_1.append(time_costs[num][0])
    grouping(group_1, group_2, num + 1)
    group_1.pop()

    group_2.append(time_costs[num][1])
    grouping(group_1, group_2, num + 1)
    group_2.pop()


if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        N = int(input())
        room = [list(map(int, input().split())) for _ in range(N)]
        min_count = 1e10

        people, stairs = get_room_pos(room) # 방의 인원, 계단 정보
        num_people = len(people)            # 총 인원 수
        time_costs = get_time_costs(people) # 모든 사람의 각 계단으로의 이동시간 저장.

        group_1, group_2 = [], []           
        grouping(group_1, group_2, 0)
        
        ans.append(f'#{t} {min_count}')
    
    print("\n".join(ans))