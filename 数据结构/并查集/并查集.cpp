class UF {
 public:
	vector<int> fa;
	vector<int> sz;
	int n;
	int comp_cnt;

 public:
	UF(int _n): n(_n), comp_cnt(_n), fa(_n), sz(_n, 1) {
		iota(fa.begin(), fa.end(), 0);
	}

	int find(int x) {
		return fa[x] == x ? x : fa[x] = find(fa[x]);
	}

	void unite(int x, int y) {
		x = find(x);
		y = find(y);
		if (x != y) {
			if (sz[x] < sz[y]) {
				swap(x, y);
			}
			fa[y] = x;
			sz[x] += sz[y];
			--comp_cnt;
		}
	}

	bool connected(int x, int y) {
		x = find(x);
		y = find(y);
		return x == y;
	}
};