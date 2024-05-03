def dijkstra(edges: List[List[int]], n: int, src: int) -> int:
    g = defaultdict(lambda: defaultdict(lambda: inf))
    # 有向图情况, 注意处理重边！
    for u, v, w in edges:
        g[u][v] = w
    dist = [-1] * n
    dist[src] = 0
    h = [[0, src]]
    while h:
        d, u = heappop(h)
        if d > dist[u]: continue
        for v, w in g[u].items():
            nd = d + w
            if dist[v] == -1 or dist[v] > nd:
                dist[v] = nd
                heappush(h, [nd, v])
    return dist