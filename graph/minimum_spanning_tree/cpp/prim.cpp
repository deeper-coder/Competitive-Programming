// 稠密图
const int INF = 0x3f3f3f3f, N = 510;
int n, m;
int g[N][N], dist[N];
bool st[N];
int res;
bool prim()
{
	dist[1] = 0;
	for (int i = 0; i < n; ++i)
	{
		int t = -1;
		for (int j = 1; j <= n; ++j)
			if (!st[j] && (t == -1 || dist[j] < dist[t]))
				t = j;
		if (dist[t] == INF) return false;
		st[t] = true;
		res += dist[t];
		// 注意由于可能存在自环，res更新应在下面这一句循环之前！
		for (int j = 1; j <= n; ++j) dist[j] = min(dist[j], g[t][j]);
	}
	return true;
}
void solve()
{
	memset(g, 0x3f, sizeof g);
	memset(dist, 0x3f, sizeof dist);
	cin >> n >> m;
	for (int i = 0; i < m; ++i)
	{
		int a, b, c; cin >> a >> b >> c;
		g[a][b] = g[b][a] =  min(g[a][b], c);
	}
	bool flag = prim();
	if (!flag) cout << "impossible" << endl;
	else cout << res << endl;
}