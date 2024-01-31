def countInversionPair(nums: MutableSequence[int]) -> int:
    """计算逆序对的个数
    sortedList解法
    时间复杂度`O(nlogn)`
    """
    from sortedcontainers import SortedList
    res = 0
    sl = SortedList()
    for num in reversed(nums):
        pos = sl.bisect_left(num)
        res += pos
        sl.add(num)
    return res
