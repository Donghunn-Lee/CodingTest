# AC

# 역시 단순하게 접근했다가 1 시간초과.
# 생각하다가 덱으로 배열을 저장 후 리버스를 하지 않고 함수를 분해해서 pop과 popleft를 사용해 답을 도출.
# 그렇게 해서 문제는 맞았지만 실행시간이 너무 길어 모범답안을 찾아보니, R로 split을 하는 방법이 있었음.
import sys
# from collections import deque
input = sys.stdin.readline

def sol(cmd, lst):
    cmd_d = list(map(len, cmd.replace('RR','').split('R')))   # R 기준 split. D의 개수만이 저장된 리스트 생성.
    rev = (len(cmd_d) - 1) % 2    # R을 기준으로 제외했으니 남은 원소의 수 -1을 2로 나눈 값이 리버스 여부가 됨.

    # 처음 써 보는 try except문. 입력이 0일 경우에 right에서 1로 시작하며 인덱스 에러가 발생할 가능성을 예방.
    left = sum(cmd_d[0::2])
    try:
        right = sum(cmd_d[1::2])
    except:
        right = 0

    # left와 right의 합은 총 D의 수. 원소 수보다 D가 더 많으면 error.
    if N < left + right:
        return 'error'
    else:
        # 구한 left, right를 바탕으로 리스트 재할당
        lst = lst[left : (N - right)]

        # rev 여부에 따라 처리 후 출력
        return f'[{",".join(reversed(lst) if rev else lst)}]'  

if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        error = False
        cmd = input().rstrip()
        N = int(input())
        lst = input().strip("[]\n").split(",")

        ans.append(sol(cmd, lst))
       
    print('\n'.join(ans))

# 다 풀고 나서 원래 코드가 왜 이렇게 실행시간이 길었는지 알았음.
# 처음 입력을 받을 때 eval() 함수를 사용했기 때문. 이게 이렇게 시간을 많이 잡아먹는 함수인 줄 몰랐음.
# 1000ms 나오던 게 136ms으로 감소함ㅋㅋ. 다만 위 모범답안이 일일이 R과 D를 대조하지 않아 더 효율적인 것은 맞음.