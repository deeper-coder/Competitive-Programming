#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define vi vector<int>
#define vii vector<vector<int>>
#define pii pair<int, int>
#define nl '\n'
const int mod = 1e9 + 7, inf = 0x3f3f3f3f, N = 2e5 + 10;
const ll lnf = 0x3f3f3f3f3f3f3f3f;
const double eps = 1e-5;
template <class T> T lowbit(T x) { return x & -x; }

ll n, m, k;
ll a[N];
double sinsum[4 * N], cossum[4 * N], todo[4 * N];

// 整合子节点信息
void push_up(ll u) {
    sinsum[u] = sinsum[u << 1] + sinsum[u << 1 | 1];
    cossum[u] = cossum[u << 1] + cossum[u << 1 | 1];
}
// 修改单个节点，但不下放
void change_single_node(ll u, ll val) {
    double tmpsin = sinsum[u], tmpcos = cossum[u];
    sinsum[u] = cos(val) * tmpsin + sin(val) * tmpcos;
    cossum[u] = cos(val) * tmpcos - sin(val) * tmpsin;
    todo[u] += val;
}
// 下放懒标记
void push_down(ll u, ll l, ll r, ll val) {
    if (val != 0) {
        change_single_node(u, val);
    }
}

void build(ll u, ll l, ll r) {
    if (l == r) {
        // 初始化单个节点信息
        sinsum[u] = sin(a[l]);
        cossum[u] = cos(a[l]);
        return;
    }
    ll mid = (l + r) >> 1;
    build(u << 1, l, mid);
    build(u << 1 | 1, mid + 1, r);
    push_up(u);
}

void change(ll u, ll l, ll r, ll L, ll R, ll val) {
    if (L <= l && r <= R) {
        change_single_node(u, val);
        return;
    }

    ll mid = (l + r) >> 1;
    push_down(u << 1, l, mid, todo[u]);
    push_down(u << 1 | 1, mid + 1, r, todo[u]);
    todo[u] = 0; // 还原标记

    if (L <= mid) {
        change(u << 1, l, mid, L, R, val);
    }
    if (R > mid) {
        change(u << 1 | 1, mid + 1, r, L, R, val);
    }
    push_up(u);
}

double query(ll u, ll l, ll r, ll L, ll R) {
    if (L <= l && r <= R) {
        return sinsum[u];
    }

    ll mid = (l + r) >> 1;
    push_down(u << 1, l, mid, todo[u]);
    push_down(u << 1 | 1, mid + 1, r, todo[u]);
    todo[u] = 0; // 还原标记

    double res = 0;
    if (L <= mid) {
        res += query(u << 1, l, mid, L, R);
    }
    if (R > mid) {
        res += query(u << 1 | 1, mid + 1, r, L, R);
    }
    return res;
}

void solve() {
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    cin >> m;
    build(1, 1, n);
    while (m--) {
        ll op, l, r;
        cin >> op >> l >> r;
        if (op == 1) {
            ll x;
            cin >> x;
            change(1, 1, n, l, r, x);
        } else {
            printf("%.1lf\n", query(1, 1, n, l, r));
        }
    }
}

int main() {
    ll t = 1;
    // cin >> t;
    while (t--)
        solve();
    return 0;
}