class Solution(object):
    def busiestServers(self, k, arrival, load):
        free = list(range(k))
        heapq.heapify(free)
        busy = []
        count = [0] * k

        for i, (start, dur) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, sid = heapq.heappop(busy)
                shifted = i + ((sid - i) % k)
                heapq.heappush(free, shifted)

            if not free:
                continue

            shifted = heapq.heappop(free)
            sid = shifted % k
            count[sid] += 1
            heapq.heappush(busy, (start + dur, sid))

        best = max(count)
        return [i for i in range(k) if count[i] == best]