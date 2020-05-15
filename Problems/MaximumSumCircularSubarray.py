# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3330/

class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_so_far = min_so_far = min_ending_here = max_ending_here = A[0]
        for x in A[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
            min_ending_here = min(x, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)
        if min_so_far == sum(A):
            return max_so_far
        else:
            return max(max_so_far, sum(A) - min_so_far)


if __name__ == "__main__":
    s = Solution()
    a = [1, -2, 3, -2]
    b = [5, -3, 5]
    c = [3,-1,2,-1]
    d = [3,-2,2,-3]
    e = [-2,-3,-1]
    f = [2,-2,2,7,8,0]
    print(s.maxSubarraySumCircular(a))
    print(s.maxSubarraySumCircular(b))
    print(s.maxSubarraySumCircular(c))
    print(s.maxSubarraySumCircular(d))
    print(s.maxSubarraySumCircular(e))
    print(s.maxSubarraySumCircular(f))


