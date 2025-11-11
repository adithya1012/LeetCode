import heapq
from collections import defaultdict


def findCheapestPrice(n: int, flights, src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)
    for frm, to, price in flights:
        graph[frm].append([to, price])

    visit = set()
    heap = [[0, 0, src]]  # price, stops(k), stop_address
    cheapest_price = float("inf")
    while heap:
        price, stops, node = heapq.heappop(heap)
        if node == dst:
            if stops <= k - 1:
                cheapest_price = min(cheapest_price, price)
        else:
            if node in visit:
                continue
            visit.add(node)
            for to, p in graph[node]:
                heapq.heappush(heap, [price + p, stops + 1, to])
    return cheapest_price if cheapest_price != float("inf") else -1



print(findCheapestPrice(n = 4, flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dst = 3, k = 1))



