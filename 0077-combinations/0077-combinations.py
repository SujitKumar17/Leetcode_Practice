class Solution:
    def combine(self, n, k):
        res = []

        def dfs(start, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(start, n + 1):
                dfs(i + 1, path + [i])

        dfs(1, [])
        return res