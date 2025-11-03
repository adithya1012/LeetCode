def maximumEnergy(energy, k: int) -> int:
    def dfs(i):
        if i >= len(energy):
            return 0
        consider = energy[i] + dfs(i + k)
        skip = dfs(i + 1)
        return max(consider, skip)

    res = 0
    for i in range(len(energy)):
        res = max(, dfs(i))
    return res

print(maximumEnergy([-2,-3,-1], 2))