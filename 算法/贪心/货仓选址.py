pre = list(accumulate(pos, initial=0))
# 中位数贪心，[l, r)区间范围内的数到位于下标m位置的数（通常为中位数点）的距离之和
# 注意原数组下标从0开始
def calSumToMedian(left: int, right: int, m: int):
    s1 = pos[m] * (m - left) - (pre[m] - pre[left])
    s2 = pre[right] - pre[m] - pos[m] * (right - m)
    return s1 + s2
