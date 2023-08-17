# 埃氏筛
MX = 10 ** 2 + 1
primes = []
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False

# 线性筛
MX = 10 ** 2 + 1
primes = []
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
    for p in primes:
        if i * p >= MX: break
        is_prime[i * p] = False
        if i % p == 0: break