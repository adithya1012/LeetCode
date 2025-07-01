# https://www.youtube.com/watch?v=zgKGtQh6Omo
from collections import defaultdict


# Amazon Prime Air is developing a system that divides shipping routes using flight optimization routing systems to a cluster of aircrafts that can fulfill these routes. Each shipping route is identified by a unique integer identifier, requires a fixed non-zero amount of travel distance between airports, and is defined to be either a forward shipping route or a return shipping route. Identifiers are guaranteed to be unique within their own route type, but not across route types.
# Each aircraft should be assigned two shipping routes at once: one forward route and one return route. Due to the complex scheduling of flight plans, all aircraft have a fixed maximum operating travel distance, and cannot be scheduled to fly a shipping route that gequires more travel distance than the prescribed maximum operating travel distance. The goal of the system is to optimize the total operating travel distance of a given aircraft. A forward/return shipping route pair is considered to be
# "optimal" if there does not exist another pair that has a higher operating travel distance than this pair, and also has a total less than or equal to the maximum operating travel distance of the aircraft.

# For example, if the aircraft has a maximum operating travel distance of 3000 miles, a forward/return shipping route pair using a total of 2900 miles would be optimal if there does not exist a pair that uses a total operating travel distance of 3000 miles, but would not be considered optimal if such a pair did exist.
# Your task is to write an algorithm to optimize the sets of forward/return shipping route pairs that allow the aircraft to be optimally utilized, given a list of forward shipping routes and a list of return shipping routes.

# maxTravelDist = 7000
# forwardRouteList - [[1,2000],[2,4000],[3,6000]]
# returnRouteList = [[1,2000]]
# Output:
# [[2,1]]
# Explanation:
# There are only three combinations, [1,11, [2,1], and [3,1], which have a total of 4000, 6000, and 8000 miles, respectively. Since 6000 is the largest use that does not exceed 7000, [2,1] is the only optimal pair.
# Example 2:
# Input:
# maxTravelDist = 10000
# forwardRouteList = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
# returnRouteList = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
# Output:
# ([2, 4], [3, 2])

def routePairs(maxTravelDist, forwardRoute, returnRoute):
    forwardRoute.sort(key=lambda k : k[1])
    returnRoute.sort(key=lambda k: k[1])
    f, r = 0, len(returnRoute)-1
    mapper = defaultdict(list)
    while f < len(forwardRoute) and r >= 0:
        route = [forwardRoute[f][0], returnRoute[r][0]]
        diff = maxTravelDist - (forwardRoute[f][1]+returnRoute[r][1])
        if diff >= 0:
            mapper[diff].append(route)
        if diff >= 0:
            f += 1
        else:
            r -= 1

    routes = []
    if mapper:
        routes = mapper[min(mapper)]
    return routes

print(routePairs(10000, [[1, 3000], [2, 5000], [3, 7000], [4, 10000]], [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]))
print(routePairs(7000, [[1, 2000], [2, 4000], [3, 6000]], [[1, 2000]]))