struct Edge {
    int a, b, w;
    Edge(int _a, int _b, int _w): a(_a), b(_b), w(_w) {}
    bool operator< (const Edge& that) const {
        return w > that.w;
    }
};

class Solution {
private:
    static constexpr int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<int> seen(m * n, 0);
        vector<int> dist(m * n, 0);
        priority_queue<Edge> q;
        q.emplace(0, 0, 0);
        dist[0] = 0;
        while (q.size()) {
            auto [a, b, w] = q.top();
            q.pop();
            if (seen[a * n + b])
                continue;
            seen[a * n + b] = 1;
            dist[a * n + b] = w;
            for (int i = 0; i < 4; ++i) {
                int nx = a + dirs[i][0];
                int ny = b + dirs[i][1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !seen[nx * n + ny]) {
                    q.emplace(nx, ny, max(w, abs(heights[a][b] - heights[nx][ny])));
                }
            }
        }
        return dist.back();
    }
};