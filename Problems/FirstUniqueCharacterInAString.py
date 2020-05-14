class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}

        for letter in s:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1

        for i, letter in enumerate(s):
            if d[letter] == 1:
                return i

        return -1
