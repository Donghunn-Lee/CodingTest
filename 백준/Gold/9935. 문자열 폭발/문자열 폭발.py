# 문자열 폭발

# 스텍 문제인가? 아님 그냥 구현 문제인가 유형은 정확히 모르겠음.
# 다만 이런 문제가 유형 파악이 쉬운 여타 알고리즘 문제들보다 의외로 머리를 더 많이 쓰게 하는 것 같음.
# 다행히도 이 문제는 50분 안쪽으로 풀긴 했으나, 조금만 복잡해져도 소요시간은 두 배로 뛸듯함.
import sys
from collections import deque
input = sys.stdin.readline

# 폭탄 제거
def removal_bomb(string, bomb):
    bomb_length = len(bomb)
    string_length = len(string)
    result = []

    # 입력 문자열보다 폭탄 길이가 더 크면 폭탄이 존재 할 수 없으므로 그대로 반환.
    if string_length < bomb_length:
        return ''.join(map(str, string))

    # result를 폭탄 길이보다 1 적은 만큼 string에서 popleft로 추가.
    for _ in range(bomb_length - 1):
        result.append(string.popleft())    

    # string을 모두 사용할 때까지 반복
    while string:
        result.append(string.popleft())

        # result의 뒤에서 폭탄 길이만큼의 문자가 폭탄과 일치할경우, 폭탄 수 만큼 pop. remove나 del은 O(N)까지라 불가.
        if result[-bomb_length :] == bomb:
            for _ in range(bomb_length):
                result.pop()
    
    # 폭탄 제거 후 result에 문자가 남아있는지 여부에 따라 출력문을 반환.
    if result:
        return ''.join(map(str, result))
    else:
        return "FRULA"


if __name__ == "__main__":
    string = deque(input().rstrip())
    bomb = list(input().rstrip())

    print(removal_bomb(string, bomb))