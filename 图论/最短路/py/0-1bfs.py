# https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/solutions/2255262/0-1lu-jing-de-bfsmo-ban-tao-lu-zong-jie-yeoia/
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # 0,0 出发  单源出发的最短路   m-1,n-1
        # 至少有一条有效路径的    最小代价
        # 1,2,3,4 右左下上
        # 选择的话只能向下或者向右走
        m,n = len(grid),len(grid[0])
        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = 0
        q = deque([(0,0)])
        vis = [[False]*n for _ in range(m)]
        while q:
            x,y = q.popleft()
            if vis[x][y]:
                continue
            vis[x][y] = True
            for i,(dx,dy) in enumerate([(x,y+1),(x,y-1),(x+1,y),(x-1,y)]):  # 1,2,3,4 右左下上
                if 0<=dx<m and 0<=dy<n:
                    new_dis = dis[x][y] + (1 if grid[x][y]!=i+1 else 0)
                    if dis[dx][dy] > new_dis:
                        dis[dx][dy] = new_dis
                        if grid[x][y] == i+1:
                            q.appendleft((dx,dy))
                        else:
                            q.append((dx,dy))
        return dis[m-1][n-1]