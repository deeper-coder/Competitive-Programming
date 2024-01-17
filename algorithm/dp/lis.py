def lis(nums: List[int]) -> List[int]:
    res = [0] * n
    g = []
    for i, x in enumerate(nums):
        j = bisect_left(g, x)
        if j == len(g):
            g.append(x)
        else:
            g[j] = x
        res[i] = j + 1
    return res