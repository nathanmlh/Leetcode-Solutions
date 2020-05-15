# https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # This is Kadane's algorithm
        max_curr = max_global = nums[0]
        for i in range(1, len(nums)):
            max_curr = max(nums[i], max_curr + nums[i])
            if max_curr > max_global:
                max_global = max_curr
        return max_global

if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
