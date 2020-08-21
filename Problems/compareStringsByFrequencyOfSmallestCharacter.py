# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        queryFrequencies = [s.count(min(s)) for s in queries]
        wordFrequencies = [s.count(min(s)) for s in words]

        answer = [0] * len(queries)
        # Loop through queries
        for i, q in enumerate(queryFrequencies):
            for w in wordFrequencies:
                if q < w:
                    answer[i] += 1

        return answer


if __name__ == "__main__":
    s = Solution()
    # queries = ["cbd"]
    # words = ["zaaaz"]

    queries = ["bbb", "cc"]
    words = ["a", "aa", "aaa", "aaaa"]
    print(s.numSmallerByFrequency(queries, words))