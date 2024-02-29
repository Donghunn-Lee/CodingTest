# 리모컨
import sys
input = sys.stdin.readline

target_channel = int(input())
N = int(input())

# 타겟 채널을 맞출 수 있는 최소 버튼 수를 리턴하는 함수
def channeling(tc, b):
    init_channel = abs(100 - tc)    # 시작점인 100에서 가는 게 더 빠른 경우
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
                # sub가 점점 줄어들어 채널 초기값과 같아짐.
                # 이후 다시 sub값이 증가하기 시작한 경우 더 반복할 이유가 없으므로 채널값을 리턴
                # check 값을 sub와 init 다시 벌어지는 상황을 감지하고 리턴하는 트리거로 사용
                if check == True:
                    if init_channel < sub:
                        return init_channel
                if sub == init_channel:
                    check = True
                # 위 코드 사용으로 기존보다 실행시간 50% 단축.
                init_channel = min(init_channel, sub)

    return init_channel

if N!= 0:
    broken = list(map(int, input().split()))
    print(channeling(target_channel, broken))
else:
    print(min(abs(100 - target_channel), len(str(target_channel))))

# 재귀를 사용해 훨씬 빠르게 답을 구할 수 있는 방법이 있음을 알았지만, 지금 이해하기엔 너무 어려운 것으로 보임.