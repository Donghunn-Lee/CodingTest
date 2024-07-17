# 감소하는 수

# 처음엔 단순하게 돌려도 1000000번, 그 안에서 자리수만큼이니까 간당간당하게 시간을 넘지 않을 거라고 생각함.
# 하지만 나올 수 있는 가장 큰 감소하는 수가 9876543210임을 깨닫고 생각을 다시 하게 됌.
# 핵심 조건은 감소하는 수에선 모든 숫자가 한 번 씩만 사용된다는 것, n번째보다 n + 1번째 수가 더 큰 수여야 한다는 것.
# 그래서 조합을 떠올림. 조합으로 자릿수 1개부터 10개까지 모든 조합을 만들고 정렬하면 되는 것이 아닌가.
# 다만 그러면 뭔가 너무 쉬워지는 것 같아서, 조금 찾아봄.

# 과연 1의 자리부터 시작해서 크기 순으로 직접 만드는 방법도 있었음. 단순하지만 효율적인 방법이라고 생각함.
import sys
input = sys.stdin.readline

def check_decreasing_num(n):
    decreasing_num = list('0123456789')
    length = 1

    while length < 10:
        for i in decreasing_num:
            if len(i) == length:
                for j in range(10):
                    if int(i[-1]) > j:
                        decreasing_num.append(i + str(j))
        
        length += 1
    
    if 1022 < n:
        return(-1)
    else:
        return(decreasing_num[n])

if __name__ == "__main__":
    N = int(input())
    
    print(check_decreasing_num(N))
