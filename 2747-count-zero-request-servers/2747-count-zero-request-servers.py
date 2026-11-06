class Solution(object):
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda l: l[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])

        cnt = [0] * (n + 1)
        distinct = 0
        left = right = 0
        m = len(logs)
        res = [0] * len(queries)

        for qi in order:
            q = queries[qi]

            while right < m and logs[right][1] <= q:
                s = logs[right][0]
                if cnt[s] == 0:
                    distinct += 1
                cnt[s] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                s = logs[left][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    distinct -= 1
                left += 1

            res[qi] = n - distinct

        return res
        