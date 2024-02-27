# 일곱 난쟁이

dwarfs = [int(input().rstrip()) for _ in range(9)]
ans = []
# dwarfs.sort()

# 9개 중 2개를 뽑는 모든 경우의 수를 탐색.
def bfs():    
    for i in range(9):
        for j in range(9):
            height = 0
            
            # 아래 if 조건 없이 실행하면 2명이 아닌 1명의 난쟁이가 제외된 경우에도
            # 합이 100이 되어 return 되는 경우가 발생.
            # 입력 리스트를 sort()하는 방법으로도 해결 가능.
            if i != j:                          
                tmp = i, j                      
                for k, v in enumerate(dwarfs):
                    if k not in tmp:
                        height += v
                        if height > 100:
                            break
                if height == 100:
                    return tmp
            
stranger = bfs()

for i, j in enumerate(dwarfs):
    if i not in stranger:
        ans.append(j)

ans.sort()

for i in ans:
    print(i)