# 상자 정렬하기

# 이게 되게 단순해 보이는데 막상 코드로 짜려니 자꾸 헷갈려서 머리가 아팠던 문제.
# 딕셔너리의 키를 상자 번호, 값을 보관함 번호로 만들고 N번 상자부터 제 자리에 놓여있는지 검사.
# 검사해서 빈 보관함과 교환. 이를 N + 1보관함이 다시 비어있을 때까지 반복.
# 그 과정에서 전역 변수 리스트에 빈 보관함의 위치를 갱신해주면 되는 문제.

def tracking(cur):
    empty_history.append(boxes_dict[cur])
    boxes_dict[cur], boxes_dict[0] = boxes_dict[0], boxes_dict[cur]

    if boxes_dict[0] != N + 1:
        tracking(boxes_dict[0])

def box_sort():
    for i in range(N, 0, -1):
        if boxes_dict[i] != i:
            tracking(i)


if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        N = int(input())
        boxes = list(map(int, input().split())) + [0]
        boxes_dict = {boxes[i] : i + 1 for i in range(N + 1)}
        empty_history = []
        
        box_sort()

        if not empty_history:
            ans.append("\n" + "0")
        else:
            ans.append("\n" + str(len(empty_history)) + "\n" + ' '.join(map(str, empty_history)))
    
    print("\n".join(ans))