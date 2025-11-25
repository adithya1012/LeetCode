import heapq
from collections import defaultdict
from typing import List


# def findCheapestPrice(n: int, flights, src: int, dst: int, k: int) -> int:
#     graph = defaultdict(list)
#     for frm, to, price in flights:
#         graph[frm].append([to, price])
#
#     visit = set()
#     heap = [[0, 0, src]]  # price, stops(k), stop_address
#     cheapest_price = float("inf")
#     while heap:
#         price, stops, node = heapq.heappop(heap)
#         if node == dst:
#             if stops <= k - 1:
#                 cheapest_price = min(cheapest_price, price)
#         else:
#             if node in visit:
#                 continue
#             visit.add(node)
#             for to, p in graph[node]:
#                 heapq.heappush(heap, [price + p, stops + 1, to])
#     return cheapest_price if cheapest_price != float("inf") else -1
#
#

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for frm, to, price in flights:
            graph[frm].append([to, price])

        heap = [[0, src]]
        visit = set()
        while k+1 >= 0:
            tmp = []
            for _ in range(len(heap)):
                price, city = heapq.heappop(heap)
                if city == dst:
                    return price
                if city in visit:
                    continue
                visit.add(city)
                for new_city, new_price in graph[city]:
                    tmp.append([new_price, new_city])
            if tmp:
                heap.extend(tmp)
                heapq.heapify(heap)
            k -= 1
        return -1


# print(Solution().findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))

print(111111 % 7)


