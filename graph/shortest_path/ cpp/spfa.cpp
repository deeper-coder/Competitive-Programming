const int INF = 0x3f3f3f3f, N = 1e5 + 10;
int n, m;
int dist[N];
bool st[N];
int h[N], e[N], ne[N], idx, w[N];
inline void add(int a, int b, int c)
{
	w[idx] = c, e[idx] = b, ne[idx] = h[a], h[a] = idx++;
}
void spfa()
{
	queue<int> q;
	dist[1] = 0;
	st[1] = true;
	q.push(1);
	while (q.size())
	{
		auto t = q.front();
		q.pop();
		st[t] = false;
		for (int i = h[t]; ~i; i = ne[i])
		{
			int j = e[i];
			if (dist[j] > dist[t] + w[i])
			{
				dist[j] = dist[t] + w[i];
				if (!st[j])
				{
					st[j] = true;
					q.push(j);
				}
			}
		}
	}
	if (dist[n] == INF) cout << "impossible" << endl;
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
	spfa();
}