# 일곱 난쟁이

dwarfs = [int(input().rstrip()) for _ in range(9)]
dwarfs.sort()
ans = []

def bfs():    
    for i in range(9):
        for j in range(9):
            height = 0
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