"""
is_limit表示当前是否受到了n的约束。若为真，则第i位填入的数字至多为s[i]，否则可以是9。如果在受到约束的情况下填了s[i]，那么后续填入的数字仍会受到n的约束。
is_num表示idx前面的数位是否填了数字。若为假，则当前位可以跳过（不填数字），或者要填入的数字至少为1；若为真，则必须填数字，且要填入的数字可以从0开始。
为什么is_num为Fasle时，填入的数字至少为1？因为前面已经单独考虑过本位跳过不填的情况，也就是本位填0的情况，所以至少为1从而避免重复计数。
"""
@lru_cache(None)
def dfs(idx, mask, is_limit, is_num):
    if idx == len(s):
        return int(is_num)
    res = 0
    if not is_num:
        res += dfs(idx+1, mask, False, False)
    up = int(s[idx]) if is_limit else 9
    for d in range(1-int(is_num), up+1):
        if (mask >> d) & 1 == 0:
            res += dfs(idx+1, mask | (1 << d), is_limit and d == up, True)
    return res
return dfs(0, 0, True, False)