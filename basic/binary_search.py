# 搜索区间左闭右闭
def binary_search(nums, target):
    n = len(nums)
    l, r = 0, n - 1
    while l <= r:
        mid = l + r >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

def binary_search(nums):
    # mid不需要+1
    n = len(nums)
    l, r = 0, n - 1
    while l < r:
        mid = l + r >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return l

def binary_search(nums):
    # mid需要+1
    n = len(nums)
    l, r = 0, n - 1
    while l < r:
        mid = l + r + 1 >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    return l