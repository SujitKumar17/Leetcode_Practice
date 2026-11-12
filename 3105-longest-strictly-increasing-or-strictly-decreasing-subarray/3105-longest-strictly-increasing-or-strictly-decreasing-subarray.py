class Solution(object):
    def longestMonotonicSubarray(self, nums):
        best = inc = dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            best = max(best, inc, dec)
        return best


# Tests
if __name__ == "__main__":
    s = Solution()
    assert s.longestMonotonicSubarray([1, 4, 3, 3, 2]) == 2
    assert s.longestMonotonicSubarray([3, 3, 3, 3]) == 1
    assert s.longestMonotonicSubarray([3, 2, 1]) == 3
    assert s.longestMonotonicSubarray([5]) == 1
    assert s.longestMonotonicSubarray([1, 2, 3, 4, 5]) == 5
    assert s.longestMonotonicSubarray([1, 2, 2, 3, 4]) == 3
    assert s.longestMonotonicSubarray([1, 3, 2, 4, 3]) == 2
    print("All tests passed")