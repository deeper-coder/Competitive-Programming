class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        ans = 0
        mask = [sum(v << j for j, v in enumerate(row)) for i, row in enumerate(mat)]
        set = (1 << cols) - 1
        while set < 1 << len(mat[0]):
            ans = max(ans, sum(row & set == row for row in mask))  # row & set = row 表示 row 是 set 的子集，所有 1 都被覆盖
            # Gosper's Hack，用于生成在n元集合中所有k元子集的算法
            lb = set & -set
            x = set + lb
            set = (set ^ x) // lb >> 2 | x
        return ans