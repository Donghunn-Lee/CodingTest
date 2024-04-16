# 문자열 폭발

# 스텍 문제인가? 아님 그냥 구현 문제인가 유형은 정확히 모르겠음.
# 다만 이런 문제가 유형 파악이 쉬운 여타 알고리즘 문제들보다 의외로 머리를 더 많이 쓰게 하는 것 같음.
# 다행히도 이 문제는 50분 안쪽으로 풀긴 했으나, 조금만 복잡해져도 소요시간은 두 배로 뛸듯함.

import sys
input = sys.stdin.readline

# 폭탄 제거
def removal_bomb(string, bomb):
    bomb_length = len(bomb)
    flag = bomb[-1]
    result = []

    # string의 원소를 반복.
    for s in string:
        result.append(s)

        # result의 뒤에서 폭탄 길이만큼의 문자가 폭탄과 일치할 경우, 뒤에서부터 폭탄 수만큼 제거.
        # +++ 폭탄의 마지막 문자를 flag에 저장, result의 마지막 문자가 flag일 경우에만 조건 체크. (336ms->204ms)
        if s == flag and result[- bomb_length :] == bomb:
            del result[-bomb_length:]
    
    # 폭탄 제거 후 result에 문자가 남아있는지 여부에 따라 출력문을 반환.
    if result:
        return ''.join(map(str, result))
    else:
        return "FRULA"


if __name__ == "__main__":
    string = list(input().rstrip())
    bomb = list(input().rstrip())

    print(removal_bomb(string, bomb))