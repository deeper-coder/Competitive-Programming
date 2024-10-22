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
int cnt;
int primes[N], st[N];

// 朴素筛法-O(nlogn)
void get_primes(int n)
{
	for (int i = 2; i <= n; i++)
	{
		if (!st[i])
			primes[cnt++] = i;
		for (int j = i + i; j <= n; j += i)
			st[j] = true;
	}
}

// 埃式筛法-O(nloglogn)
void get_primes(int n)
{
	for (int i = 2; i <= n; i++)
	{
		if (!st[i])
		{
			primes[cnt++] = i;
			for (int j = i; j <= n; j += i)
				st[j] = true;
		}
	}
}

// 线性筛法-O(n), n = 1e7的时候基本就比埃式筛法快一倍了
// 算法核心：x仅会被其最小质因子筛去
void get_primes(int x)
{
	for (int i = 2; i <= x; i++)
	{
		if (!st[i])
			primes[cnt++] = i;
		for (int j = 0; primes[j] <= x / i; j++)
		{
			// 对于任意一个合数x，假设pj为x最小质因子，当i<x/pj时，一定会被筛掉
			st[primes[j] * i] = true;
			if (i % primes[j] == 0)
				break;
			/*
			1.i%pj == 0, pj定为i最小质因子，pj也定为pj*i最小质因子
			2.i%pj != 0, pj定小于i的所有质因子，所以pj也为pj*i最小质因子
			*/
		}
	}
}

void solve()
{
	int x;
	cin >> x;
	get_primes(x);
	cout << cnt << endl;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	solve();
	return 0;
}