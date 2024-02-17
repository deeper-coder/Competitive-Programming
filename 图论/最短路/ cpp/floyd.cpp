// 带有路径保存

const int INF = 0x3f3f3f3f, N = 210;
int dist[N][N], p[N][N];  // p[i][j]代表i-j两点之间最短路径必须经过p[i][j]表示的点
int n, m, t;

void floyd()
{
	for (int k = 1; k <= n; ++k)
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				if (dist[i][j] > dist[i][k] + dist[k][j])
				{
					dist[i][j] = dist[i][k] + dist[k][j];
					p[i][j] = k;  // i-j之间必须经过k
				}
}

string get_path(int u, int v)
{
	if (p[u][v] == -1) return to_string(u) + "->"; // base case: 直接相连的情况
	int k = p[u][v];
	return get_path(u, k) + get_path(k, v); // 返回左右两端u->k以及k->v的路径
}

void solve()
{
	cin >> n >> m >> t;
	memset(dist, 0x3f, sizeof dist);
	memset(p, 0x3f, sizeof p);
	for (int i = 1; i <= n; ++i) dist[i][i] = 0;  // 处理自环
	for (int i = 0; i < m; ++i)
	{
		int a, b, c;
		cin >> a >> b >> c;
		dist[a][b] = min(dist[a][b], c);  // 处理重边
		p[a][b] = -1;  // 如果两点之间有一条直接路径，那么意味着无需经过任何点，我们设为-1
	}
	floyd();
	while (t--)
	{
		int x, y;
		cin >> x >> y;
		if (dist[x][y] > INF / 2) cout << "impossible" << endl;  // 由于循环过程可能存在负权边更新，所以必须要大于inf/2
		else
		{
			cout << dist[x][y] << endl;
			string path = get_path(x, y) + to_string(y);
			cout << path << endl;
		}
	}
}