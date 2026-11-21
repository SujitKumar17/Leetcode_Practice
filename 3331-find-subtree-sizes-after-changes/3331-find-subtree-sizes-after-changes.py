class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        last = [-1] * 26
        closest = [-1] * n
        saved = [-1] * n
        order = []

        stack = [(0, False)]
        while stack:
            node, exiting = stack.pop()
            c = ord(s[node]) - 97
            if exiting:
                last[c] = saved[node]
                continue
            order.append(node)
            closest[node] = last[c]
            saved[node] = last[c]
            last[c] = node
            stack.append((node, True))
            for ch in children[node]:
                stack.append((ch, False))

        size = [1] * n
        for x in reversed(order):
            if x == 0:
                continue
            p = closest[x] if closest[x] != -1 else parent[x]
            size[p] += size[x]

        return size