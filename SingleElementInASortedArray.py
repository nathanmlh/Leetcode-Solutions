# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start < end:
            # Calculate mid
            mid = 2 * ((start + end) // 4)
            if nums[mid] == nums[mid + 1]:
                # Search the part of list after mid
                start = mid + 2
            else:
                # Search part of list before mid
                end = mid

        return nums[start]