class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        import heapq
        
        # adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        K = k + 1                      # run lengths are 1..k, index 0 unused
        INF = float('inf')
        dist = [INF] * (n * K)

        start = 0 * K + 1              # node 0 with run length 1
        dist[start] = 0
        heap = [(0, 0, 1)]             # (distance, node, run)

        while heap:
            d, u, run = heapq.heappop(heap)
            if d > dist[u * K + run]:
                continue
            # first time we pop the target, it is the shortest answer
            if u == n - 1:
                return d
            lu = labels[u]
            for v, w in graph[u]:
                if labels[v] == lu:
                    nrun = run + 1
                    if nrun > k:
                        continue
                else:
                    nrun = 1
                nd = d + w
                idx = v * K + nrun
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq.heappush(heap, (nd, v, nrun))

        return -1