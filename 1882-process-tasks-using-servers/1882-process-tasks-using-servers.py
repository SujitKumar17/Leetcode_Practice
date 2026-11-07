class Solution(object):
    def assignTasks(self, servers, tasks):
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = [0] * len(tasks)
        t = 0

        for j, duration in enumerate(tasks):
            # Task j enters the queue at second j
            t = max(t, j)
            if not free:
                t = max(t, busy[0][0])

            # Release all servers that are free by time t
            while busy and busy[0][0] <= t:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            ans[j] = i
            heapq.heappush(busy, (t + duration, w, i))

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.assignTasks([3, 3, 2], [1, 2, 3, 2, 1, 2]) == [2, 2, 0, 2, 1, 2]
    assert s.assignTasks([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1]) == [1, 4, 1, 4, 1, 3, 2]
    assert s.assignTasks([1], [5, 5, 5]) == [0, 0, 0]
    assert s.assignTasks([10, 10], [1, 1, 1]) == [0, 0, 0]
    print("All tests passed")