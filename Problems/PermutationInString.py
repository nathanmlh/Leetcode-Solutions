# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3333/

class Solution:
	def checkInclusion(self, s: str, t: str) -> bool:
		LS, LT, S, T = len(s), len(t), 0, 0
		if LS > LT: return False
		for i in range(LS): S, T = S + hash(s[i]), T + hash(t[i])
		if S == T: return True
		for i in range(LS, LT):
			T += hash(t[i]) - hash(t[i-LS])
			if S == T: return True
		return False


if __name__ == "__main__":
    s = Solution()
    a = "ab"
    b = "eidboaoo"
    print(s.checkInclusion(a, b))
