class UF:
    def __init__(self, n):
        self.n = n
        self.fa = [i for i in range(n)]
        self.sz = [1] * n
        self.comp_cnt = n

    def find(self, x):
        if x != self.fa[x]:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.sz[x] < self.sz[y]:
                x, y = y, x
            self.fa[y] = x
            self.sz[x] += self.sz[y]
            self.comp_cnt -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        edge = [(w, x-1, y-1) for x, y, w in connections]
        edge.sort()

        res = 0
        uf = UF(n)
        for w, x, y in edge:
            if uf.connected(x, y):
                continue
            uf.unite(x, y)
            res += w
            if uf.comp_cnt == 1:
                return res
        return -1
