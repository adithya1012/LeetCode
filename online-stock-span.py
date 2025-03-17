class StockSpanner:

    def __init__(self):
        self.data = []
        self.stack = []
        self.count = 0

    def next(self, price: int) -> int:
        span = 1
        # self.data.append(price)
        while self.stack and self.stack[-1][1] < price:
            span_tmp, val = self.stack.pop()
            span += span_tmp
        self.stack.append([span, price])
        return span

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))
