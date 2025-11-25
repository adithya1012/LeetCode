# Q: Given graph of cities and time taken to travel between them.
# You have given source city A and list of favourite cities.
# Output the smallest time taken to reach any of the favourite cities from city A.
from collections import defaultdict
import heapq


class Solution:
    def __init__(self, fav_cities, city_travel_time):
        self.city_travel_time = city_travel_time
        self.fav_cities = set(fav_cities)
        self.graph = self.construct_graph(self.city_travel_time)
        self.reverse_graph = self.reverse_construct_graph(self.city_travel_time)

    def construct_graph(self, city_travel_time):
        graph = defaultdict(list)
        for frm, to, time in city_travel_time:
            graph[frm].append([to, time])
        return graph

    def reverse_construct_graph(self, city_travel_time):
        graph = defaultdict(list)
        for frm, to, time in city_travel_time:
            graph[to].append([frm, time])
        return graph

    def time_for_fav_city(self, source):
        heap = [[0, source]]
        visit = set()
        while heap:
            time, city = heapq.heappop(heap)
            if city in self.fav_cities:
                return time
            if city in visit:
                continue
            visit.add(city)
            for new_city, new_time in self.graph[city]:
                heapq.heappush(heap, [new_time + time, new_city])
        return -1

    def dijkstra(self, source, graph):
        heap = [[0, source]]
        all_city = {source: 0}

        while heap:
            time, city = heapq.heappop(heap)

            # Skip if we've already found a better path to this city
            if time > all_city.get(city, float("inf")):
                continue

            for new_city, new_time in graph[city]:
                new_total_time = new_time + time
                # Only add to heap if this path is better
                if new_total_time < all_city.get(new_city, float("inf")):
                    all_city[new_city] = new_total_time
                    heapq.heappush(heap, [new_total_time, new_city])

        return all_city

    def shortest_distance_fav_1(self, source, target):
        source_fav_distance = self.dijkstra(source, self.graph)
        target_fav_distance = self.dijkstra(target, self.reverse_graph)

        min_total = float("inf")
        for fav in self.fav_cities:
            if fav in source_fav_distance and fav in target_fav_distance:
                min_total = min(min_total, source_fav_distance[fav] + target_fav_distance[fav])

        return min_total if min_total != float("inf") else -1

    def shortest_distance_fav_2(self, source, target):
        # Check if source is already a favorite city
        initial_visit_fav = 1 if source in self.fav_cities else 0
        heap = [[0, source, initial_visit_fav]]
        visit = set()

        while heap:
            time, city, visit_fav = heapq.heappop(heap)

            # Found target after visiting a favorite
            if city == target and visit_fav:
                return time

            if (city, visit_fav) in visit:
                continue
            visit.add((city, visit_fav))

            # Update visit_fav flag if current city is favorite
            new_visit_fav = visit_fav or (1 if city in self.fav_cities else 0)

            for new_city, new_time in self.graph[city]:
                heapq.heappush(heap, [new_time + time, new_city, new_visit_fav])

        return -1


# Test
city_travel_time = [
    ['A', 'B', 10],
    ['A', 'C', 15],
    ['B', 'D', 12],
    ['C', 'D', 10],
    ['D', 'E', 2],
    ['C', 'E', 5],
    ['B', 'F', 5],
    ['F', 'E', 1]
]
fav_cities = ['C', 'F']

sol = Solution(fav_cities, city_travel_time)
print("Time to fav city:", sol.time_for_fav_city('A'))  # Should be 15 (A->C)
print("Method 1:", sol.shortest_distance_fav_1('A', 'E'))  # Should be 16 (A->B->F->E)
print("Method 2:", sol.shortest_distance_fav_2('A', 'E'))  # Should be 16

# Follow Up: Now in the same network of cities, you have given city S and city T and list of favourite cities.
# We have to give the shortest path from city S to city T which must go through at-least one of the favourite city.