from ast import List
from re import M


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        """
            马拉车算法核心
            d1,d2 二者分别表示以位置i为中心的长度为奇数和长度为偶数的回文串个数
            l, r表示遍历过程中回文串覆盖的最右侧位置, l与r之间对称
            如果 s = cbaabd, 那么d2[3] = 2
        """

        def get_d(is_even):
            d = [0] * n
            l, r = 0, -1
            for i in range(0, n):
                k = 1 - is_even if i > r else min(d[l + r - i + is_even], r - i + 1)
                while (
                    0 <= i - k - is_even
                    and i + k < n
                    and s[i - k - is_even] == s[i + k]
                ):
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


# 马拉车算法，详解见https://leetcode.cn/problems/check-if-dfs-strings-are-palindromes/solutions/2957704/mo-ban-dfs-shi-jian-chuo-manacher-suan-f-ttu6/
class Manacher:
    def __init__(self, s: str):
        self.halfLen = self.manacher(list(s))

    def manacher(self, s: list) -> list:
        t = "#".join(["^"] + s + ["$"])
        # halfLen[i] 表示在 t 上的以 t[i] 为回文中心的最长回文子串的回文半径
        # 即 [i-halfLen[i]+1,i+halfLen[i]-1] 是 t 上的一个回文子串
        halfLen = [0] * (len(t) - 2)
        halfLen[1] = 1
        boxM = boxR = 0
        for i in range(2, len(halfLen)):
            hl = 1
            if i < boxR:
                hl = min(halfLen[boxM * 2 - i], boxR - i)
            while t[i - hl] == t[i + hl]:
                hl += 1
                boxM, boxR = i, i + hl
            halfLen[i] = hl

        return halfLen

    # 判断原字符串s的左闭右开区间 [l,r) 是否为回文串  0 <=l<r<=n
    # 其中原字符串s和当前t字符串的下标转换关系为 s[i] 对应 t[2*i+2]
    # 需要满足 halfLen[l + r + 1] - 1 >= r - l，即 halfLen[l + r + 1] > r - l
    def isPalindrome(self, l: int, r: int) -> bool:
        return self.halfLen[l + r + 1] > r - l