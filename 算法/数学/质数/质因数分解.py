def fac(N):
    res = []
    for i in range(2, isqrt(N) + 1):
        if N % i == 0: 
            while N % i == 0:
                N //= i
            res.append(i)
    if N != 1:
        res.append(N)
    return res