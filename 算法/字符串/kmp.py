# 非常好的一篇原理讲解（https://www.zhihu.com/question/21923021/answer/642165149）

# 找到pattern在text中所有匹配位置
def kmp(self, text: str, pattern: str) -> List[int]:
    m = len(pattern)
    pi = [0] * m
    c = 0
    for i in range(1, m):
        v = pattern[i]
        while c and pattern[c] != v:
            c = pi[c - 1]
        if pattern[c] == v:
            c += 1
        pi[i] = c

    res = []
    c = 0
    for i, v in enumerate(text):
        v = text[i]
        while c and pattern[c] != v:
            c = pi[c - 1]
        if pattern[c] == v:
            c += 1
        if c == len(pattern):
            res.append(i - m + 1)
            c = pi[c - 1]
    return res