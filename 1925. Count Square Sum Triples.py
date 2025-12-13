import math
class Solution:
    def countTriples(self, n: int) -> int:
        calculated = set()
        res = 0
        def checkTriples(i):
            # if i in calculated:
            #     return False
            nonlocal res
            j = i+1
            while i * i + j * j <= n * n:
                if math.sqrt(i*i+j*j) == int(math.sqrt(i*i+j*j)) and int(math.sqrt(i*i+j*j)) <= n:
                    if (i, j, math.sqrt(i*i+j*j)) not in calculated:
                        # res += 2
                        calculated.add((i, j, math.sqrt(i*i+j*j)))
                        calculated.add((j, i, math.sqrt(i*i+j*j)))
                j += 1

        for i in range(1, n):
            checkTriples(i)
        return len(calculated)



print(Solution().countTriples(10))