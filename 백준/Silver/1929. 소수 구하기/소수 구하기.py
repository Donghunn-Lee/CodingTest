#소수 구하기

M, N = map(int, input().split())
primes = []

def calPrimeNumber():
    for i in range(M, N + 1):
        if i != 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
        
            else:
                print(i)
                    

calPrimeNumber()