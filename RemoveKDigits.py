# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for number in num:
            while k and stack and stack[-1] > number:
                # Remove last number put in stack
                stack.pop(-1)
                k -= 1
            stack.append(number)

        # If there is still numbers to be removed
        while k:
            stack.pop()
            k -= 1

        # Remove leading zeros
        ans = "".join(stack).lstrip("0")

        return (ans if ans else "0")