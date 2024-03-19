# 나무 자르기

# 처음엔 왜 이렇게 쉽지? 하고 10분만에 풀고 당연하게도 시간초과. 입력 값의 최대치가 100만임을 간과했음.
# 두 번째 풀이는 {나무의 높이 : 같은 높이의 나무 수} 를 딕셔너리로 저장하고, 내림차순 정렬된 리스트에서
# 높은 나무부터 더해가다가 목표치 초과시 높이를 1씩 올려서 확인하는 방법이었으나, 2% 시간초과.
# 위 방법도 첫 번째에 비하면 꽤 빠를 거라고 생각했는데 시간초과가 나왔고, 이미 많이 쓴 시간을 더 써 봐야
# 정답을 구상해내진 못할 것으로 판단하고 검색해서 이분 탐색 문제임을 알게 되었음.
# 높이의 상단과 하단을 중단을 설정함으로써 양분하여 목표치를 만족하는 최고 높이의 위아래를 이분 탐색하는 방식.
import sys
input = sys.stdin.readline

def cut(target_amount):
    # 최하단, 최상단을 설정
    bottom, top = 1, max(trees)

    # 하단 값이 상단을 초과할 경우 중지
    while bottom <= top:
        middle = (top + bottom) // 2    # 범위를 양분하는 중간값을 변화하는 상 하단에 맞게 반복마다 재할당
        amount = 0                      # 합을 계산할 변수

        # 중간값보다 위에 있는 나무, 즉 잘라서 얻어지는 나무의 합을 계산
        for i in trees:
            if i >= middle:
                amount += i - middle
        
        # 합이 목표치를 상회할 경우 덜어내기 위해 하단을 현재 중간값 + 1(기준 높이 + 1)
        if amount >= target_amount:
            bottom = middle + 1
        # 반대의 경우 상단값을 중간값 - 1
        else:
            top = middle - 1

    # 목표치 확인 조건에서 amount >= target_amount 이므로, 조건을 만족하는 최고 높이에 도달한 경우
    # bottom이 증가함. 때문에 while 조건에서 bottom <= top이고 bottom > top인 경우, 직전 변화값인 bottom이
    # 아니라 고정되있던 top을 최고 높이로서 반환.
            
    return top

if __name__ == "__main__":
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    
    print(cut(M))
