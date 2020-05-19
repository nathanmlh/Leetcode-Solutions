# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3334/

# Using two arrays
# class StockSpanner:
#
#     def __init__(self):
#         self.prices = []
#         self.spans = []
#
#     def next(self, price: int) -> int:
#         index = len(self.prices) - 1
#         while index >= 0 and self.prices[index] <= price:
#             span = self.spans[index]
#             index = index - span
#         self.prices.append(price)
#         span = len(self.prices) - 1 - index
#         self.spans.append(span)
#         return span

# Using a stack of pairs
class StockSpanner:

    def __init__(self):
        self.prices_and_spans = []

    def next(self, price: int) -> int:
        count = 1
        while self.prices_and_spans and self.prices_and_spans[-1][0] <= price:
            count += self.prices_and_spans[-1][1]
            self.prices_and_spans.pop()
        self.prices_and_spans.append((price, count))
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)