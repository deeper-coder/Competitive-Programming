# 方法1 有序数组（只有lc平台支持）
def countInversionPair(nums: MutableSequence[int]) -> int:
    from sortedcontainers import SortedList
    res = 0
    sl = SortedList()
    for num in reversed(nums):
        pos = sl.bisect_left(num)
        res += pos
        sl.add(num)
    return res

# 方法2 树状数组
from bisect import bisect
from typing import List
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.tree[x]
            x -= BIT.lowbit(x)
        return ret

    def update(self, x):
        while x <= self.n:
            self.tree[x] += 1
            x += BIT.lowbit(x)

def reversePairs(record: List[int]) -> int:
    n = len(record)
    # 离散化
    tmp = sorted(record)
    for i in range(n):
        record[i] = bisect.bisect_left(tmp, record[i]) + 1
    # 树状数组统计逆序对
    bit = BIT(n)
    ans = 0
    for i in range(n - 1, -1, -1):
        ans += bit.query(record[i] - 1)
        bit.update(record[i])
    return ans