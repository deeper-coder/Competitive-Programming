// 稀疏图
const int INF = 0x3f3f3f3f, N = 1e5 + 10, M = 2e5 + 10;
int n, m;
int p[N];
struct Edge
{
	int a, b, w;

	bool operator<(const Edge& E) const
	{
		return w < E.w;
	}
} edges[M];
int find(int x)
{
	if (x != p[x]) p[x] = find(p[x]);
	return p[x];
}
void kruskal()
{
	int cnt = 0, res = 0;
	for (int i = 0; i < m; ++i)
	{
		int a = edges[i].a, b = edges[i].b, w = edges[i].w;
		int pa = find(a), pb = find(b);
		if (pa != pb)
		{
			p[pa] = pb;
			cnt++;
			res += w;
		}
	}
	if (cnt < n - 1) cout << "impossible" << endl;
	else cout << res << endl;
}
void solve()
{
	cin >> n >> m;
	for (int i = 1; i <= n; ++i) p[i] = i;
	for (int i = 0; i < m; ++i) cin >> edges[i].a >> edges[i].b >> edges[i].w;
	sort(edges, edges + m);
	kruskal();
}