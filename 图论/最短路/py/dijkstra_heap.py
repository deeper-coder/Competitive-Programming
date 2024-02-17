def dijkstra(edges: List[List[int]], n: int, src: int) -> int:
    g = defaultdict(dict)
    for u, v, w in edges:
        g[u][v] = w
    hpq = [[0, src]]
    dist = [-1] * n
    while hpq:
        d, u = heapq.heappop(hpq)
        if dist[u] != -1: continue
        dist[u] = d
        for v, w in g[u].items():
            heapq.heappush(hpq, [d + w , v])
            
    if min(dist) == -1: return -1
    else: return max(dist)