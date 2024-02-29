# 리모컨

target_channel = int(input())
N = int(input())

def channeling(tc, b):
    init_channel = abs(100 - tc)
    check = False
    if b == 0:
        return init_channel

    for i in range(1000001):
        tmp = str(i)

        for j in range(len(tmp)):
            if int(tmp[j]) in b:
                break
            elif j == len(tmp) - 1:
                sub = abs(int(tmp) - tc) + len(tmp)
                if check == True:
                    if init_channel < sub:
                        return init_channel
                if sub == init_channel:
                    check = True
                init_channel = min(init_channel, sub)

    return init_channel

if N!= 0:
    broken = list(map(int, input().split()))
    print(channeling(target_channel, broken))
else:
    print(min(abs(100 - target_channel), len(str(target_channel))))

