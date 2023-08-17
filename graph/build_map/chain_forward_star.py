class Graph:
    def __init__(self, n, m):
        self.h = [-1] * (n + 10)
        self.e, self.ne, self.w = [0] * (m + 10), [0] * (m + 10), [0] * (m + 10)
        self.idx = 0

    def add(self, a, b, c):
        self.w[self.idx] = c; self.e[self.idx] = b
        self.ne[self.idx] = self.h[a]; self.h[a] = self.idx
        self.idx += 1
