# 判断n是否是质数
def is_prime(n):
    return n != 1 and all(n % i for i in range(2, isqrt(n) + 1))