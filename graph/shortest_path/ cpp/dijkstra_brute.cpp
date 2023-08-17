int n, m;
int g[N][N], dist[N];
bool st[N];
void dijkstra()
{
	dist[1] = 0;
	for (int i = 1; i <= n; ++i)
	{
		int t = -1;
		for (int j = 1; j <= n; ++j)
			if (!st[j] && (t == -1 || dist[j] < dist[t]))
				t = j;
		st[t] = true;
		for (int j = 1; j <= n; ++j)
		{
			if (dist[j] > dist[t] + g[t][j])
				dist[j] = dist[t] + g[t][j];
		}
	}
	if (dist[n] == INF) cout << -1 << endl;
	else cout << dist[n] << endl;
}
void solve()
{
	memset(g, 0x3f, sizeof g);
	memset(dist, 0x3f, sizeof dist);
	cin >> n >> m;
	for (int i = 0; i < m; ++i)
	{
		int a, b, c; cin >> a >> b >> c;
		g[a][b] = min(g[a][b], c);
	}
	dijkstra();
}