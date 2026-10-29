class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = max(1, n.bit_length())
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        up = [[0] * n for _ in range(LOG)]

        timer = 0
        stack = [(0, -1, 0)]
        while stack:
            node, parent, state = stack.pop()
            if state == 0:
                tin[node] = timer
                timer += 1
                up[0][node] = parent if parent != -1 else 0
                stack.append((node, parent, 1))
                for nxt in adj[node]:
                    if nxt != parent:
                        depth[nxt] = depth[node] + 1
                        stack.append((nxt, node, 0))
            else:
                tout[node] = timer - 1

        for k in range(1, LOG):
            prev = up[k - 1]
            cur = up[k]
            for i in range(n):
                cur[i] = prev[prev[i]]

        size = n + 2
        bit = [0] * (size + 1)
        chars = [1 << (ord(c) - 97) for c in s]

        def add(i, val):
            i += 1
            while i <= size:
                bit[i] ^= val
                i += i & -i

        def point(i):
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        for i in range(n):
            add(tin[i], chars[i])
            add(tout[i] + 1, chars[i])

        def get_lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            k = 0
            while diff:
                if diff & 1:
                    a = up[k][a]
                diff >>= 1
                k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return up[0][a]

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                x = int(parts[1])
                nm = 1 << (ord(parts[2]) - 97)
                if nm != chars[x]:
                    delta = chars[x] ^ nm
                    add(tin[x], delta)
                    add(tout[x] + 1, delta)
                    chars[x] = nm
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = get_lca(u, v)
                mask = point(tin[u]) ^ point(tin[v]) ^ chars[w]
                ans.append((mask & (mask - 1)) == 0)
        return ans