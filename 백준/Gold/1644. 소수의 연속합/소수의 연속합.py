# 소수의 연속합

# 여러 수 중 소수를 판별 할 때는 소수 전체를 구하고 그 중 소수인 수를 찾는 게 효율적임.
# 전에 소수 관련 문제를 두어 개 푼 적이 있었기에 금방 이 점을 파악하고, 에라토스테네스의 체를 구현함.
# 물론 외우고 있지 못했기에 전에 풀었던 코드를 찾아봤지만 이제 보니 너무 어려워서, 검색해서 이해가 쉬운 코드를 참고.
# 아무튼 에라토스테네스의 체를 이용해 N이하의 소수를 모두 구하고, 그 수열을 반복하며 연속합이 N인 경우를 탐색.

# 그런데 정말 한심하게도 처음에 for문 안에 또 for문을 넣어놓고, 소수가 그리 많지 않을 거라 여겨 소수 길이만큼 반복함.
# 4백만 까지의 소수는 10만개가 넘음. 택도 없다는 뜻.
# 고민끝에 검색해서 알게 된 방법은 투 포인터였음. 투 포인터 문제를 여태 두 개? 정도밖에 안 풀어서 떠올리지 못함.
# 다음엔 연속된 부분을 찾는 이런 경우에 금방 투 포인터를 떠올릴 수 있도록 하자.
import sys
input = sys.stdin.readline

# 에라토스테네스의 체 O(log(log N))
# 핵심 개념은 3부터 시작해서 그 제곱수와 배수를 계산해 모두 소수가 아님(False)표시를 하고, 남아있는 수가 소수라는 것.
def eratosthenes_sieve(prime_numbers):
    sieve = [False, False] + [True] * (N - 1)

    for i in range(2, N + 1):
        if sieve[i]:
            prime_numbers.append(i)
            for j in range(2 * i, N + 1, i):
                sieve[j] = False

# 투 포인터를 사용해 소수의 연속합이 N이 되는 경우의 수를 계산.
# start와 end각각 N번 반복되어야 종료되므로 2N. 즉 O(N)의 시간복잡도밖에 필요하지 않게 됨.
def continuous_sum(prime_numbers):
    count = 0
    start, end = 0, 0
    len_prime = len(prime_numbers)

    # sum함수를 써서 tmp_sum이 N보다 크면 start를 늘려 작은 소수부터 제외하고, 작으면 end를 늘리는 방식으로 진행.
    while end <= len_prime:
        tmp_sum = sum(prime_numbers[start : end])

        if tmp_sum < N:
            end += 1
        
        elif tmp_sum > N:
            start += 1
        
        else:
            count += 1
            end += 1
    
    return count

if __name__ == "__main__":
    N = int(input())
    prime_numbers = []

    eratosthenes_sieve(prime_numbers)
    print(continuous_sum(prime_numbers))