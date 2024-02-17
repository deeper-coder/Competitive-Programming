#include<bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
int n;
vector<int> tr(n, 0);

void update(int x, int ad) {
	if (!x) return;
	for (; x <= n; x += x & -x) tr[x] += ad;
}

int query(int x) {
	if (!x) return 0;
	int tot = 0;
	for (; x; x -= x & -x) tot += tr[x];
	return tot;
}

// 离散化
void discrete(vector<int> &nums) {
	vector<int> tmp = nums;
	sort(tmp.begin(), tmp.end());
	tmp.erase(unique(tmp.begin(),tmp.end()),tmp.end()); // 去重
	for (int& num: nums) {
		num = lower_bound(tmp.begin(), tmp.end(), num) - tmp.begin() + 1;
	}
}