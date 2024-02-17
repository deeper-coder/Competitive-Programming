// N为节点的数量，e, ne, w数组长度为边的数量
int h[N], e[N], ne[N], w[N], idx;
inline void add(int a, int b, int c)
{
	w[idx] = c, e[idx] = b, ne[idx] = h[a], h[a] = idx++;
}
// 记得初始化h
memset(h, -1, sizeof h);