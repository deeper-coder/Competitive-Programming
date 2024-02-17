# 单点更新，区间查询
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        u = max(nums)
        mx = [0] * (4 * u)

        def modify(o: int, l: int, r: int, i: int, val: int) -> None:
            if l == r:
                mx[o] = val
                return
            m = (l + r) // 2
            if i <= m: modify(o * 2, l, m, i, val)
            else: modify(o * 2 + 1, m + 1, r, i, val)
            mx[o] = max(mx[o * 2], mx[o * 2 + 1])

        # 返回区间 [L,R] 内的最大值
        def query(o: int, l: int, r: int, L: int, R: int) -> int:  # L 和 R 在整个递归过程中均不变，将其大写，视作常量
            if L <= l and r <= R: return mx[o]
            res = 0
            m = (l + r) // 2
            if L <= m: res = query(o * 2, l, m, L, R)
            if R > m: res = max(res, query(o * 2 + 1, m + 1, r, L, R))
            return res

        for x in nums:
            if x == 1:
                modify(1, 1, u, 1, 1)
            else:
                res = 1 + query(1, 1, u, max(x - k, 1), x - 1)
                modify(1, 1, u, x, res)
        return mx[1]


# 区间更新，区间查询

# nums下标从0开始
class SegTree0:

    def __init__(self, nums):
        n = len(nums)
        self.n = n
        self.nums = nums
        self.tr = [0] * (4 * n)
        self.build(0, 0, n - 1)

    def push_up(self, p):
        self.tr[p] = self.tr[p * 2 + 1] + self.tr[p * 2 + 2]

    def build(self, p, l, r):
        if l == r: self.tr[p] = self.nums[l]; return
        mid = l + r >> 1
        self.build(p * 2 + 1, l, mid)
        self.build(p * 2 + 2, mid + 1, r)
        self.push_up(p)

    def change(self, p, l, r, x, y):  
        if x == l and x == r: self.tr[p] = y; return
        mid = l + r >> 1
        if x <= mid:
            self.change(p * 2 + 1, l, mid, x, y)
        else:
            self.change(p * 2 + 2, mid + 1, r, x, y)
        self.push_up(p)

    def query(self, p, l, r, ql, qr):
        if ql <= l and qr >= r: return self.tr[p]
        mid = l + r >> 1
        res = 0
        if ql <= mid:
            res += self.query(p * 2 + 1, l, mid, ql, qr)
        if qr > mid:
            res += self.query(p * 2 + 2, mid + 1, r, ql, qr)
        return res

# nums下标从1开始
class SegTree1:

    def __init__(self, nums):
        n = len(nums) - 1
        self.n = n
        self.nums = nums
        self.tr = [0] * (4 * n + 10)
        self.build(1, 1, n)

    def push_up(self, p):
        self.tr[p] = self.tr[p << 1] + self.tr[p << 1 | 1]

    def build(self, p, l, r):
        if l == r: self.tr[p] = self.nums[l]; return
        mid = l + r >> 1
        self.build(p << 1, l, mid)
        self.build(p << 1 | 1, mid + 1, r)
        self.push_up(p)

    def change(self, p, l, r, x, y):
        if x == l and x == r: self.tr[p] += y; return
        mid = l + r >> 1
        if x <= mid: self.change(p << 1, l, mid, x, y)
        else: self.change(p << 1 | 1, mid + 1, r, x, y)
        self.push_up(p)

    def query(self, p, l, r, ql, qr):
        if ql <= l and qr >= r: return self.tr[p]
        mid = l + r >> 1
        res = 0
        if ql <= mid:
            res += self.query(p << 1, l, mid, ql, qr)
        if qr > mid:
            res += self.query(p << 1 | 1, mid + 1, r, ql, qr)
        return res