class Solution:
    def minLength(self, nums):
        n = len(nums)
        maxn = 2 * n + 2
        nxt = [None] * maxn
        link = [-1] * maxn
        length = [0] * maxn
        cnt = [0] * maxn

        nxt[0] = {}
        sz = 1
        last = 0

        for c in nums:
            cur = sz
            sz += 1
            length[cur] = length[last] + 1
            cnt[cur] = 1
            nxt[cur] = {}
            p = last
            while p != -1 and c not in nxt[p]:
                nxt[p][c] = cur
                p = link[p]
            if p == -1:
                link[cur] = 0
            else:
                q = nxt[p][c]
                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    cl = sz
                    sz += 1
                    length[cl] = length[p] + 1
                    nxt[cl] = dict(nxt[q])
                    link[cl] = link[q]
                    cnt[cl] = 0
                    while p != -1 and nxt[p].get(c) == q:
                        nxt[p][c] = cl
                        p = link[p]
                    link[q] = cl
                    link[cur] = cl
            last = cur

        order = sorted(range(1, sz), key=lambda v: length[v], reverse=True)
        for v in order:
            cnt[link[v]] += cnt[v]

        ans = n
        for v in range(1, sz):
            if cnt[v] == 1:
                ans = min(ans, length[link[v]] + 1)
        return ans

    # aliases in case the judge expects a different method name
    minimumLength = minLength
    smallestUniqueSubarray = minLength
    minUniqueSubarray = minLength