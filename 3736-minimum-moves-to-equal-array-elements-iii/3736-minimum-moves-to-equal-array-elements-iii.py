class Solution(object):
    def minMoves(self, nums):
        m = max(nums)
        return sum(m - x for x in nums)