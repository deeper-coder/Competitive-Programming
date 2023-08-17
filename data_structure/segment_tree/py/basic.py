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