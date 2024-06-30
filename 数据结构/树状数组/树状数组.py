class Fenwick:
    __slots__ = "f"

    def __init__(self, n: int):
        self.f = [0] * (n + 1)

    # 将下标i处值增加val
    def update(self, i: int, val: int) -> None:
        while i < len(self.f):
            self.f[i] += val
            i += i & -i

    # 返回闭区间 [1, i] 的元素和
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.f[i]
            i &= i - 1
        return res

    # 返回闭区间 [l, r] 的元素和
    def query(self, l: int, r: int) -> int:
        if r < l:
            return 0
        return self.pre(r) - self.pre(l - 1)


n = II()
a = LII()
num2idx = {}
for i, x in enumerate(sorted(a), 1):
    num2idx[x] = i
f = Fenwick(n)