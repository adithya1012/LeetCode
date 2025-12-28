from collections import defaultdict
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        for i, ingredient in enumerate(ingredients):
            graph[recipes[i]] = graph[recipes[i]] + ingredient
        print(graph)
        supplies = set(supplies)
        cycle = set()
        visit = set()

        def dfs(i):
            if i in visit:
                return True
            if i in cycle:
                return False
            if i not in supplies:
                return False
            cycle.add(i)
            for j in graph[i]:
                if not dfs(j):
                    return False
            cycle.remove(i)
            visit.add(i)
            return True

        res = []
        for i in recipes:
            if dfs(i):
                res.append(i)
        return res

print(Solution().findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))


