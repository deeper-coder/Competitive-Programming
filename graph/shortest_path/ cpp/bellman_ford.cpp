// 存在负权边且有边数限制
const int INF = 0x3f3f3f3f, N = 1e4 + 10;
int dist[N], backup[N];
int n, m, k;
struct Edge
{
	int a, b, w;
}edges[N];
void bellman_ford()
{
	dist[1] = 0;
	for (int i = 0; i < k; ++i)
	{
		// 每次循环前备份
		memcpy(backup, dist, sizeof dist);
		for (int j = 0; j < m; ++j)
		{
			int st = edges[j].a, ed = edges[j].b, w = edges[j].w;
			if (dist[ed] > backup[st] + w)
				dist[ed] = backup[st] + w;
		}
	}
	if (dist[n] > INF / 2) cout << "impossible" << endl;
	else cout << dist[n] << endl;
}
void solve()
{
	memset(dist, 0x3f, sizeof dist);
	memset(backup, 0x3f, sizeof backup);
	cin >> n >> m >> k;
	for (int i = 0; i < m; ++i) cin >> edges[i].a >> edges[i].b >> edges[i].w;
	bellman_ford();
}