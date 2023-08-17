#include <bits/stdc++.h>

using namespace std;
#define xx first
#define yy second
#define lowbit(x) (x & -x)
#define mm(a, x) memset(a, x, sizeof a)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
const int INF = 0x3f3f3f3f, MOD = 1e9 + 7, N = 1e5 + 10;
int n, m;
int a[N];

struct Node {
    int l, r;
    int v;
} tr[N * 4];

void push_up(int p) { tr[p].v = tr[p << 1].v + tr[p << 1 | 1].v; }

void build(int p, int l, int r) {
    if (l == r) {
        tr[p] = {l, r, a[l]};
        return;
    }
    tr[p] = {l, r};
    int mid = (l + r) >> 1;
    build(p << 1, l, mid), build(p << 1 | 1, mid + 1, r);
    push_up(p);
}

void change(int p, int x, int y) {
    if (tr[p].l == x && x == tr[p].r) {
        tr[p].v += y;
        return;
    }
    int mid = (tr[p].l + tr[p].r) >> 1;
    if (x <= mid)
        change(p << 1, x, y);
    else
        change(p << 1 | 1, x, y);
    push_up(p);
}

int query(int p, int ql, int qr) {
    if (tr[p].l >= ql && tr[p].r <= qr) return tr[p].v;
    int mid = (tr[p].l + tr[p].r) >> 1;
    int res = 0;
    if (ql <= mid) res += query(p << 1, ql, qr);
    if (qr > mid) res += query(p << 1 | 1, ql, qr);
    return res;
}

void solve() {
    cin >> n >> m;
    for (int i = 1; i <= n; i++) cin >> a[i];
    build(1, 1, n);
    while (m--) {
        int op, x, y;
        cin >> op >> x >> y;
        if (op == 1)
            change(1, x, y);
        else
            cout << query(1, x, y) << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}