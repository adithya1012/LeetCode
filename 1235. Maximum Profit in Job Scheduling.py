
def jobScheduling(startTime, endTime, profit) -> int:
    def dfs(pend, i):
        if i >= len(profit):
            return 0
        val1 = 0
        if pend <= startTime[i]:
            val1 = dfs(endTime[i], i+1)+profit[i]
        val2 = dfs(pend, i+1)
        return max(val1, val2)
    return dfs(0, 0)

print(jobScheduling([6,15,7,11,1,3,16,2], [19,18,19,16,10,8,19,8], [2,9,1,19,5,7,3,19]))