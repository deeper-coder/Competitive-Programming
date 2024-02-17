def nextPermutation(nums: MutableSequence[int], inPlace=False) -> Tuple[bool, MutableSequence[int]]:
    """返回下一个字典序的排列，如果不存在，返回本身;时间复杂度O(n)"""
    if not inPlace:
        nums = nums[:]

    i = j = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    if i == 0:  # 不存在下一个字典序的排列
        return False, nums

    k = i - 1  
    while nums[j] <= nums[k]:
        j -= 1

    nums[k], nums[j] = nums[j], nums[k]

    l, r = k + 1, len(nums) - 1  
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    return True, nums