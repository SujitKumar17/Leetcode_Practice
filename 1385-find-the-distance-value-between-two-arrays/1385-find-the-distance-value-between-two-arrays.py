class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        for a in arr1:
            if all(abs(a - b) > d for b in arr2):
                count += 1
        return count
        