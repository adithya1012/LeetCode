import unittest
#
#
# def add2No(a, b):
#     return a + b
#
#
# class TestCaseExecution(unittest.TestCase):
#     def test_add2Normal(self):
#         self.assertEqual(add2No(10, 20), 30)
#
#     def test_add2Zero(self):
#         self.assertEqual(add2No(0, 0), 0)
#
#     def test_add2Negetive(self):
#         self.assertEqual(add2No(-10, -20), -30)
#
#
# if "__mani__" == __name__:
#     unittest.main()


# class HitCounter:
#     def __init__(self):
#         self.bandwidth = 300
#         self.time = [0] * self.bandwidth
#         self.count = [0] * self.bandwidth
#
#     def hit(self, timestamp: int) -> None:
#         index = timestamp % self.bandwidth
#         if self.time[index] != timestamp:
#             self.time[index] = timestamp
#             self.count[index] = 1
#         else:
#             self.count[index] += 1
#
#     def getHits(self, timestamp: int) -> int:
#         res = 0
#         for i in range(self.bandwidth):
#             if timestamp - self.time[i] < self.bandwidth:
#                 res += self.count[i]
#         return res

# class TestCaseExecutor(unittest.TestCase):
#     def test_normalFlow(self):
#         h = HitCounter()
#         h.hit(1)
#         h.hit(2)
#         h.hit(3)
#         h.hit(300)
#         self.assertEqual(h.getHits(300), 4)
#         self.assertEqual(h.getHits(301), 3)
#
#     def test_normalFlow1(self):
#         h = HitCounter()
#         h.hit(1)
#         h.hit(2)
#         h.hit(3)
#         h.hit(300)
#         self.assertEqual(h.getHits(299), 4)

# if __name__ == "__main__":
#     unittest.main()

a = "/a/b/c"
a = a.split("/")
print(a)

print("/".join(a[:1]))  