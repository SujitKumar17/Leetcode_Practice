class Solution(object):
    def minimizeSum(self, nums):
        nums.sort()
        n = len(nums)
        return min(
            nums[n - 3] - nums[0],   # change the two largest
            nums[n - 1] - nums[2],   # change the two smallest
            nums[n - 2] - nums[1],   # change the smallest and the largest
        )


if __name__ == "__main__":
    s = Solution()

    assert s.minimizeSum([1, 4, 7, 8, 5]) == 3
    assert s.minimizeSum([1, 4, 3]) == 0
    assert s.minimizeSum([5, 5, 5]) == 0
    assert s.minimizeSum([1, 2, 3, 4]) == 1
    assert s.minimizeSum([1, 10, 100, 1000]) == 9
    assert s.minimizeSum([1, 1000000000, 1000000000, 1000000000]) == 0
    assert s.minimizeSum([10, 20, 30, 40, 50, 60]) == 30

    print("All tests passed")