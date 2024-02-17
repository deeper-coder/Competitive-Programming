class SegTree:
    
    def __init__(self, nums):
        self.n = len(nums)
        self.tr = [0] * (self.n * 4)
        self.add = [0] * (self.n * 4)
        self.nums = nums
        self.build(1, 1, self.n)

    def push_up(self, p):
        self.tr[p] = self.tr[p << 1] + self.tr[p << 1 | 1]

    def build(self, p, l, r):
        # nums数组下标从0开始
        if l == r: self.tr[p] = self.nums[l-1]; return
        mid = l + r >> 1
        self.build(p << 1, l, mid)
        self.build(p << 1 | 1, mid + 1, r)
        self.push_up(p)

    def push_down(self, p, l, r):
        mid = l + r >> 1
        self.add[p << 1] += self.add[p]
        self.tr[p << 1] += self.add[p] * (mid - l + 1)
        self.add[p << 1 | 1] += self.add[p]
        self.tr[p << 1 | 1] += self.add[p] * (r - (mid + 1) + 1)
        self.add[p] = 0

    def change(self, p, l, r, cl, cr, x):
        if cl <= l and cr >= r:
            self.tr[p] += (r - l + 1) * x
            self.add[p] += x
            return
        self.push_down(p, l, r)
        mid = l + r >> 1
        if cl <= mid:
            self.change(p << 1, l, mid, cl, cr, x)
        if cr > mid:
            self.change(p << 1 | 1, mid + 1, r, cl, cr, x)
        self.push_up(p)

    def query(self, p, l, r, ql, qr):
        if ql <= l and qr >= r: return self.tr[p]
        self.push_down(p, l, r)
        mid = l + r >> 1
        res = 0
        if ql <= mid:
            res += self.query(p << 1, l, mid, ql, qr)
        if qr > mid:
            res += self.query(p << 1 | 1, mid + 1, r, ql, qr)
        return res