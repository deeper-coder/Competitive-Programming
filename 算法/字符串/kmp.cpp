#include <bits/stdc++.h>

using namespace std;
#define xx first
#define yy second
#define lowbit(x) (x & -x)
#define mm(a, x) memset(a, x, sizeof a)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
const int INF = 0x3f3f3f3f, MOD = 1e9 + 7, N = 1e6 + 10;
int n, m;
char p[N], s[N];
int ne[N];
void solve()
{
    cin >> n >> p >> m >> s;
    ne[0] = -1;
    for (int i = 1, j = -1; i < n; ++i)
    {
        while (j != -1 && p[i] != p[j+1]) j = ne[j];
        if (p[i] == p[j+1]) j++;
        ne[i] = j;
    }
    for (int i = 0, j = -1; i < m; ++i)
    {
        while (j != -1 && s[i] != p[j+1]) j = ne[j];
        if (s[i] == p[j+1]) j++;
        if (j == n - 1) 
        {
            cout << i - n + 1 << " ";
            j = ne[j];
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}