class Solution(object):
    def minOperations(self, nums, x, k):
        n = len(nums)
        vals = sorted(set(nums))
        rank = {}
        for i, v in enumerate(vals):
            rank[v] = i + 1
        size = len(vals)
        cnt = [0] * (size + 1)
        sm = [0] * (size + 1)

        def update(i, dc, ds):
            while i <= size:
                cnt[i] += dc
                sm[i] += ds
                i += i & -i

        top = 1
        while top * 2 <= size:
            top *= 2
        m = (x + 1) // 2

        def window_cost(total):
            pos, remaining, acc = 0, m, 0
            pw = top
            while pw:
                nxt = pos + pw
                if nxt <= size and cnt[nxt] < remaining:
                    pos = nxt
                    remaining -= cnt[nxt]
                    acc += sm[nxt]
                pw >>= 1
            med = vals[pos]
            left = acc + remaining * med
            right = total - left
            return (med * m - left) + (right - med * (x - m))

        cost = [0] * (n - x + 1)
        total = 0
        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                out = nums[i - x]
                update(rank[out], -1, -out)
                total -= out
            if i >= x - 1:
                cost[i - x + 1] = window_cost(total)

        INF = float("inf")
        prev = [0] * (n + 1)
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                take = prev[i - x] + cost[i - x]
                skip = cur[i - 1]
                cur[i] = take if take < skip else skip
            prev = cur
        return int(prev[n])