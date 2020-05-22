# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/

import operator

class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for letter in s:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1

        sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

        ans = ""
        for key in sorted_d.keys():
            for num in range(sorted_d[key]):
                ans += key
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort("Aabb"))