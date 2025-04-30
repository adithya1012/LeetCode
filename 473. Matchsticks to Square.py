
def makesquare(matchsticks) -> bool:
    if sum(matchsticks) % 4:
        return False
    matchsticks.sort(reverse=True)
    oneSide = sum(matchsticks) / 4
    taken = [False] * len(matchsticks)

    def dfs(i, val):
        print(i, val)
        if i >= len(matchsticks) and val == oneSide:
            return True
        if val == oneSide:
            return dfs(i, 0)
        if val > oneSide:
            return False

        for index, t in enumerate(taken):
            if not t:
                taken[index] = True
                if dfs(i + 1, val + matchsticks[index]):
                    return True
                taken[index] = False
                break
        return False

    return dfs(0, 0)

print(makesquare([5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]))

