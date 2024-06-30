# 给定树结构，获得以所有节点为根时对应的树的深度，结果以列表返回
def get(edges: List[List[int]]) -> List[int]:
    n = len(edges) + 1
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)

    # f[i] 当前节点为根时的最大深度和次大深度
    f = [[0, 0] for _ in range(n)]

    # 当前树直径
    def dfs(u, fa):
        max_len = 0
        second_len = 0
        for v in g[u]:
            if v == fa: continue
            d = dfs(v, u) + 1
            if d >= max_len:
                second_len = max_len
                max_len = d
            elif d > second_len:
                second_len = d
        f[u] = [max_len, second_len]
        return max_len

    dfs(0, -1)

    # 所有节点中最大深度的最小值
    mnd = inf
    def rdfs(u, fa):
        nonlocal mnd
        # 最大深度，次大深度
        mx, smx = f[u]
        mnd = min(mx, mnd)
        for v in g[u]:
            if v == fa: continue
            # 如果当前v的最大深度 + 1刚好是它父亲u的最大深度，那么不能通过最大深度来更新，而是应该通过次大深度更新
            t = smx if f[v][0] + 1 == mx else mx
            if t + 1 >= f[v][0]: # 大于最大，更新最大和次大
                f[v][1], f[v][0] = f[v][0], t + 1
            elif t + 1 > f[v][1]: # 大于次大，只需要更新次大
                f[v][1] = t + 1
            rdfs(v, u)

    rdfs(0, -1)

    return [d for d, _ in f]