# 점심 식사시간

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


def get_time_costs(people):
    time_costs = []

    for i, j in people:
        a = abs(i - stairs[0][0]) + abs(j - stairs[0][1])
        b = abs(i - stairs[1][0]) + abs(j - stairs[1][1])
        time_costs.append((a, b))

    return time_costs

def move(group_1, group_2, num_people):
    global min_count
    count = 0
    if group_1 == [1,2,2] and group_2 == [5,6,6,7,7,8,9]:
        print(123)

    while 0 < num_people:
        on_stairs_1, on_stairs_2 = 0, 0
        escape_1, escape_2 = 0, 0
        count += 1

        # 계단으로 이동.
        for i in range(len(group_1)):
            tmp = group_1[i]

            if tmp == -stairs[0][2]:
                escape_1 += 1
            elif tmp <= 0 and on_stairs_1 < 3:
                group_1[i] -= 1
                on_stairs_1 += 1
            elif 0 < tmp:
                group_1[i] -= 1

        if escape_1 != 0:
            group_1 = group_1[escape_1:]
            num_people -= escape_1

        for i in range(len(group_2)):
            tmp = group_2[i]
            
            if tmp == -stairs[1][2]:
                escape_2 += 1
            elif tmp <= 0 and on_stairs_2 < 3:
                group_2[i] -= 1
                on_stairs_2 += 1
            elif 0 < tmp:
                group_2[i] -= 1

        if escape_2 != 0:
            group_2 = group_2[escape_2:]
            num_people -= escape_2

    
    min_count = min(min_count, count)

    


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
        
        people, stairs = get_room_pos(room)
        num_people = len(people)
        time_costs = get_time_costs(people)

        group_1, group_2 = [], []
        grouping(group_1, group_2, 0)
        
        ans.append(f'#{t} {min_count}')
    
    print("\n".join(ans))