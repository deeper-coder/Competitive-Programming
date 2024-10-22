# https://leetcode.cn/problems/falling-squares/submissions/550347968/?envType=daily-question&envId=2024-07-28

class Node:
    def __init__(self, l, r) -> None:
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        self.v = 0
        self.add = 0

class SegmentTree:
    def __init__(self) -> None:
        self.root = Node(0, 10**9)

    def push_up(self, node):
        node.v = max(node.left.v, node.right.v)

    def push_down(self, node):
        if not node.left:
            node.left = Node(node.l, node.mid)
        if not node.right:
            node.right = Node(node.mid + 1, node.r)
        if node.add:
            node.left.add = node.add
            node.right.add = node.add
            node.left.v = node.add
            node.right.v = node.add
            node.add = 0

    def modify(self, l, r, v, node=None):
        if not node:
            node = self.root
        if l <= node.l and r >= node.r:
            node.v = v
            node.add = v
            return
        if l > node.r or r < node.l:
            return
        self.push_down(node)
        if l <= node.mid:
            self.modify(l, r, v, node.left)
        if r > node.mid:
            self.modify(l, r, v, node.right)
        self.push_up(node)

    def query(self, l, r, node=None):
        if not node:
            node = self.root
        if l <= node.l and r >= node.r:
            return node.v
        if l > node.r or r < node.l:
            return 0
        self.push_down(node)
        res = 0
        if l <= node.mid:
            res = max(res, self.query(l, r, node.left))
        if r > node.mid:
            res = max(res, self.query(l, r, node.right))
        return res