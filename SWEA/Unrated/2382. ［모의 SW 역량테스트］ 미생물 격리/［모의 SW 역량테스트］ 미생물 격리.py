# 미생물 격리

# 문제 안의 알고리즘 자체는 어렵지 않았다고 생각하는데, 이를 계산하기 위한 자료형을 어떻게 할 지가 고민이 필요했음.
# 처음엔 하나의 2차원 리스트에서 군집을 옮겨가며 그 수를 저장하려다가
# 곧 이동한 군집과 아직인 군집이 합쳐지는 문제가 발생할 수 있음을 깨달음.
# 고민끝에 2개의 딕셔너리를 사용해 스왑해주면 이동 전과 후의 미생물들을 관리할 수 있음을 알았음.
# 다른 문제에서도 자주 사용했던 좌표의 튜플을 key, 미생물 수와 방향을 value로 해서 생성.

def move_on_hours(microbes, m):
    dir = {1 : (-1, 0), 2 : (1, 0), 3 : (0, -1), 4 : (0, 1)}    # 방향
    turn_back = {1 : 2, 2 : 1, 3 : 4, 4 : 3}                    # 약품 칸에 도달했을 때를 위한 역방향
    sum_microbes = 0

    # m 시간동안 이동.
    for _ in range(m):
        next_hours = dict()             # 이동을 완료한 군집을 저장할 딕셔너리 생성.

        for cur in microbes:            
            ci, cj = cur                # 현재 좌표(키 값)을 저장.
            cd = microbes[cur][1]       # 현재 방향을 저장.

            ni, nj = ci + dir[cd][0], cj + dir[cd][1]   # 방향대로 1칸 이동한 좌푤르 저장.

            # 약품 칸이 아닌 경우, 그대로 next_hours에 추가.
            if 1 <= ni < N - 1 and 1 <= nj < N - 1:     

                # 현 좌표에 아직 딕셔너리가 없다면 새로 추가.
                if not next_hours.get((ni, nj)):
                    next_hours[(ni, nj)] = [microbes[cur]]

                # 이미 만들어져 있다면 현재 군집도 추가. 이를 위해 앞서 2차원 리스트로 추가함.
                else:
                    next_hours[(ni, nj)].append(microbes[cur])

            # 이동한 좌표가 약품 칸인 경우, 미생물 수를 반감하고 방향 전한.
            else:
                if not next_hours.get((ni, nj)):
                    next_hours[(ni, nj)] = [[microbes[cur][0] // 2, turn_back[microbes[cur][1]]]]
                else:
                    next_hours[(ni, nj)].append([microbes[cur][0] // 2, turn_back[microbes[cur][1]]])


        # 반복을 끝낸 microbes 딕셔너리를 초기화.
        microbes = dict()

        # 비어있는 microbes 딕셔너리에 next_hours 로부터 미생물 군집을 다시 할당받음.
        for moved in next_hours:

            # 한 칸에 군집이 2개 이상 있는 경우, 이를 합치고 가장 수가 많은 군집의 방향으로 새로운 군집 생성.
            if 2 <= len(next_hours[moved]):
                bigest, nd, sum = 0, 0, 0

                for element in next_hours[moved]:
                    sum += element[0]
                    if bigest < element[0]:
                        bigest, nd = element[0], element[1]
                
                microbes[moved] = [sum, nd]

            # 그 칸에 군집이 하나라면 그대로 추가.
            else:
                microbes[moved] = next_hours[moved][0]  # 2차원 리스트 형태이기때문에 [0] 추가.

    # m 시간의 반복이 끝나면 현재 미생물 수의 총합을 계산 후 반환.
    for mcr in microbes:
        sum_microbes += microbes[mcr][0]
    
    return sum_microbes


if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        N, M, K = map(int, input().split())
        microbes = dict()
        result = 0

        for _ in range(K):
            a, b, c, cd = map(int, input().split())
            microbes[(a, b)] = [c, cd]
        
        result = move_on_hours(microbes, M)
        ans.append(f"#{t} {result}")
    
    print("\n".join(ans))
