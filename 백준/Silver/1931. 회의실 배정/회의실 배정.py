# 회의실 배정

# 정말 어지러웠던 문제.
# 여태 문제를 풀면서 푸는 방법을 머리속으로 대략 그리면서 그 방법에 맞춰 데이터 타입을 정하곤 했음.
# 이번 문제 역시 dfs인가? 싶어 그렇게 한 번 풀어봤으나 예상대로 시간초과 발생. 여기서 일단 뇌정지.
# DP인가 싶어 해보려고 해도 딱히 효율적이라고 생각되지 않음. 해봤으나 답이 안나옴.

# 결론은 그냥 데이터를 제대로 정렬만 하면 그 다음엔 끝나는 순서만 저장해가며 다음 원소를 비교하면 되는 거였음.
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    # 파이썬 sort에서 key로 정렬 기준을 설정할 수 있다는 것은 알았는데 떠올리지 못했음.
    # 애초에 끝나는 시간을 기준으로 오름차순 정렬해야겠다는 생각도 못함. 오늘 너무 머리를 많이 쓴 탓임 분명(아님).
    # 다만 한 번에 두 개 조건을 받아서 이차원 리스트를 각 원소를 기준으로 정렬 하는 건 새롭게 알게 됨.
    meeting_list = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: (x[1], x[0]))
    ans, end = 0, 0

    for i, j in meeting_list:
        if end <= i:
            ans += 1
            end = j
    
    print(ans)