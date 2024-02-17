class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    # 将下标 i 上的数加一
    def inc(self, i: int) -> None:
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    # 返回闭区间 [1, i] 的元素和
    def sum(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

    # 返回闭区间 [left, right] 的元素和
    def query(self, left: int, right: int) -> int:
        return self.sum(right) - self.sum(left - 1)

n = II()
a = LII()
num2idx = {}
for i, x in enumerate(sorted(a), start=1):
    num2idx[x] = i
ft = FenwickTree(n)