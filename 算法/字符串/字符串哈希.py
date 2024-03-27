import random

class StringHash:
    def __init__(self, s, MOD=random.randint(10**18, 2 * 10**18)):
        n = len(s)
        self.BASE = BASE = 131  # or use 13331
        self.MOD = MOD
        self.h = h = [0] * (n + 1)
        self.p = p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = (p[i - 1] * BASE) % MOD
            h[i] = (h[i - 1] * BASE % MOD + ord(s[i - 1])) % MOD

    # get hash of s[l:r), if l == r, return 0
    def get_hash(self, l, r):
        return (self.h[r] - self.h[l] * self.p[r - l] % self.MOD) % self.MOD