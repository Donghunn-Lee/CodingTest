# 백만 장자 프로젝트

T  = int(input())
price = []

high_point = 0
hp_index = 1
output = []
for i in range(T) :
    N = int(input())
    price = list(map(int, input().split()))
    pr_sum = 0
    
    while price:
        high_point = max(price)
        hp_index = price.index(high_point)
        if hp_index != 0 :
            pr_sum += (high_point * hp_index) - sum(price[:hp_index])
            del price[:hp_index]

        else :
            del price[hp_index]

    output.append('#{0} {1}'.format(i+1,pr_sum))

print('\n'.join(output))