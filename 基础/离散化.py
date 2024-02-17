from sortedcontainers import SortedSet
s = SortedSet(sorted(nums))
dsc = {}
idx = 1
for x in s:
    dsc[x] = idx
    idx += 1
