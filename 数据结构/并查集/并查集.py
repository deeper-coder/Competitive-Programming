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