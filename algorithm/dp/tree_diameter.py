# 记录最长和次长
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ans = 0

        def dfs(u, fa):
            nonlocal ans
            max_len = 0
            second_len = 0
            for nxt in g[u]:
                if nxt == fa:
                    continue
                d = dfs(nxt, u) + 1
                if d >= max_len:
                    second_len = max_len
                    max_len = d
                elif d > second_len:
                    second_len = d
            ans = max(ans, max_len + second_len)
            return max_len

        dfs(0, -1)
        return ans


# 只记录最长


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ans = 0

        def dfs(u, fa):
            nonlocal ans
            max_len = 0
            for nxt in g[u]:
                if nxt == fa:
                    continue
                d = dfs(nxt, u) + 1
                ans = max(ans, max_len + d)
                max_len = max(max_len, d)
            return max_len

        dfs(0, -1)
        return ans
