class PrefixSum2D:
    def __init__(self, mat):
        self.m, self.n = len(mat), len(mat[0])  # m*n的原矩阵
        self.mat = mat
        self.s = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        self.build()

    def build(self):
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.s[i][j] = (
                    self.s[i - 1][j] + self.s[i][j - 1] - self.s[i - 1][j - 1] + self.mat[i - 1][j - 1]
                )

    # [(x1, y1) -> (x2, y2)] 闭区间范围, (x1, y1)和(x2, y2)为原来矩阵中的坐标
    def get(self, x1, y1, x2, y2):
        return self.s[x2 + 1][y2 + 1] - self.s[x2 + 1][y1] - self.s[x1][y2 + 1] + self.s[x1][y1]