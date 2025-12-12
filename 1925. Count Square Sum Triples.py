class Solution:
    def countTriples(self, n: int) -> int:
        calculated = set()
        res = 0
        def checkTriples(i):
            if i in calculated:
                return False
            nonlocal res
            j = i+1
            while j <= n:
                if i*i + j*j <= n*n:
                    print(i, j)
                    res += 1
                    calculated.add(j)
                    j+=1
                else:
                    break
        for i in range(1, n):
            if not checkTriples(i):
                return res
        return res

Solution().countTriples(5)