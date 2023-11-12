class Node:
    def __init__(self):
        self.ls = self.rs = None
        self.val = -1


class SegmentTree:
    def __init__(self):
        self.root = Node()

    def update(self, node, lc, rc, l, r, v):
        if l <= lc and r >= rc:
            node.val = max(node.val, v)
            return
        self.pushdown(node)
        mid = (lc + rc) >> 1
        if l <= mid:
            self.update(node.ls, lc, mid, l, r, v)
        if r > mid:
            self.update(node.rs, mid + 1, rc, l, r, v)
        node.val = max(node.ls.val, node.rs.val)

    def query(self, node, lc, rc, l, r):
        if l <= lc and r >= rc:
            return node.val
        self.pushdown(node)
        mid = (lc + rc) >> 1
        ans = -1
        if l <= mid:
            ans = max(ans, self.query(node.ls, lc, mid, l, r))
        if r > mid:
            ans = max(ans, self.query(node.rs, mid + 1, rc, l, r))
        return ans

    def pushdown(self, node: Node):
        if node.ls is None:
            node.ls = Node()
        if node.rs is None:
            node.rs = Node()