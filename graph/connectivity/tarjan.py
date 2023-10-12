# 无向图求桥 https://leetcode.cn/problems/critical-connections-in-a-network/solutions/2008167/1192-cha-zhao-ji-qun-nei-de-guan-jian-li-guu6/
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ans = []
        g = defaultdict(list)
        
        for x, y in connections:
            g[x].append(y)
            g[y].append(x)
        
        dfn, low = [-1] * n, [-1] * n
        t = 1
        def tarjan(u, fa):
            nonlocal t
            dfn[u] = low[u] = t
            t += 1
            for nxt in g[u]:
                if nxt == fa: continue
                if dfn[nxt] == -1:
                    tarjan(nxt, u)
                    low[u] = min(low[u], low[nxt])
                    if dfn[u] < low[nxt]:
                        ans.append([u, nxt])
                else:
                    low[u] = min(low[u], dfn[nxt])
        tarjan(0, -1)
        return ans