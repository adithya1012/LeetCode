from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        n = len(tickets)
        for a, b in tickets:
            graph[a].append(b)

        for a in graph:
            graph[a].sort(reverse=True)

        res = []

        def dfs(node, n):
            if n == 0:
                return True
            tmp = graph[node].copy()
            for i in tmp:
                ele = graph[node].pop()
                res.append(i)
                if dfs(i, n - 1):
                    return True
                res.pop()
                graph[node].append(ele)
            return False

        dfs("JFK", n)
        return ["JFK"] + res


print(Solution().findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","ATL"],["ATL","BBB"],["BBB","ATL"],["ATL","CCC"],["CCC","ATL"],["ATL","DDD"],["DDD","ATL"],["ATL","EEE"],["EEE","ATL"],["ATL","FFF"],["FFF","ATL"],["ATL","GGG"],["GGG","ATL"],["ATL","HHH"],["HHH","ATL"],["ATL","III"],["III","ATL"],["ATL","JJJ"],["JJJ","ATL"],["ATL","KKK"],["KKK","ATL"],["ATL","LLL"],["LLL","ATL"],["ATL","MMM"],["MMM","ATL"],["ATL","NNN"],["NNN","ATL"]]))