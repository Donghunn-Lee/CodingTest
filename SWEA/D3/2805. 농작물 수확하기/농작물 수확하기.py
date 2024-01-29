# 농작물 수확하기

T = int(input())

for t in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    harvest = sum(farm[N//2][:])

    for i in range(1, (N//2) + 1):
        harvest += sum(farm[(N//2) + i][i: N-i])
        harvest += sum(farm[(N//2) - i][i: N-i])

    print(f"#{t} {harvest}")




