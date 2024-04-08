from webbrowser import get


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        '''
            马拉车算法核心
            d1,d2 二者分别表示以位置i为中心的长度为奇数和长度为偶数的回文串个数
            l, r表示遍历过程中回文串覆盖的最右侧位置, l与r之间对称
            如果 s = cbaabd, 那么d2[3] = 2
        '''
        def get_d(is_even):
            d = [0] * n
            l, r = 0, -1
            for i in range(0, n):
                k = 1 - is_even if i > r else min(d[l + r - i + is_even], r - i + 1)
                while 0 <= i - k - is_even and i + k < n and s[i - k - is_even] == s[i + k]:
                    k += 1
                d[i] = k
                k -= 1
                if i + k > r:
                    l = i - k - is_even
                    r = i + k
            return d
        
        d1 = get_d(0)
        d2 = get_d(1)

        ans = ""
        for i, (l1, l2) in enumerate(zip(d1, d2)):
            if 2 * l1 - 1 > len(ans):
                l1 -= 1
                ans = s[i - l1 : i + l1 + 1]
            if 2 * l2 > len(ans):
                l2 -= 1
                ans = s[i - l2 - 1 : i + l2 + 1]
        return ans