# 톱니바퀴

def spin(target, spin_way):
    if spin_way == 1:
        gears[target].insert(0, gears[target].pop())

    elif spin_way == -1:
        gears[target].insert(len(gears[target]), gears[target][0])
        del gears[target][0]


gears = []
score = 0

for i in range(4):
    gears.append(list(input()))

K = int(input())

for k in range(K):
    gear_num, way = map(int, input().split())
    gear_num -= 1
    spin_target = []
    l_way, r_way = way, way
    spin_target.append([gear_num, way])
    for i in range(3):
        # left
        if l_way != 0:
            if gear_num-i-1 >= 0:
                if gears[gear_num - i][6] != gears[gear_num - i - 1][2]:
                    l_way *= -1
                    spin_target.append([gear_num - i - 1, l_way])
                else:
                    l_way = 0

        #right
        if r_way != 0:
            if gear_num+i+1 < 4:
                if gears[gear_num + i][2] != gears[gear_num + i + 1][6]:
                    r_way *= -1
                    spin_target.append([gear_num + i + 1, r_way])
                else:
                    r_way = 0
    for t in spin_target:
        spin(t[0], t[1])

if gears[0][0] == '1':
    score += 1
if gears[1][0] == '1':
    score += 2
if gears[2][0] == '1':
    score += 4
if gears[3][0] == '1':
    score += 8

print(score)