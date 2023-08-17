int h[N], e[N], ne[N], idx, w[N];
int dist[N];
bool st[N];
int n, m;
inline void add(int a, int b, int c)
{
	w[idx] = c, e[idx] = b, ne[idx] = h[a], h[a] = idx++;
}
void dijkstra()
{
	dist[1] = 0;
	priority_queue<pii, vector<pii>, greater<pii>> q;
	q.push({0, 1}); // dist, node
	while (q.size())
	{
		auto t = q.top();
		q.pop();
		int ver = t.yy, d = t.xx;
		if (st[ver]) continue;
		st[ver] = true;

		for (int i = h[ver]; ~i; i = ne[i])
		{
			int j = e[i];
			if (dist[j] > d + w[i])
			{
				dist[j] = d + w[i];
				q.push({dist[j], j});
			}
		}
	}
	if (dist[n] == INF) cout << -1 << endl;
	else cout << dist[n] << endl;
}
void solve()
{
	memset(dist, 0x3f, sizeof dist);
	memset(h, -1, sizeof h);
	cin >> n >> m;
	for (int i = 0; i < m; ++i)
	{
		int a, b, c; cin >> a >> b >> c;
		add(a, b, c);
	}
	dijkstra();
}