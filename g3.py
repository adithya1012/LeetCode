# Q: You have given movies and movies network (movies which have same genere) and rating for each of these movies.
# You have to return list of K most highly rated movies which are related to movie A.
import heapq
from collections import defaultdict


# https://claude.ai/chat/9b63b7bb-4a3b-45e0-b146-d3591859647d

# Sol: Build graph from movie relations. BFS over graph from movie A by maintaining the MIN Heap of size K.


def MovieNetwork(source, movies, movie_rating, k):
    graph = defaultdict(list)
    for m1, m2 in movies:
        graph[m1].append(m2)
        graph[m2].append(m1)
    visit = set()
    def dfs(m):
        if m in visit:
            return
        visit.add(m)
        for new_m in graph[m]:
            dfs(new_m)
    dfs(source)

    movies_rating = []
    for m in visit:
        movies_rating.append([-movie_rating[m], m])
    heapq.heapify(movies_rating)
    res = []
    while k:
        _, movie = heapq.heappop(movies_rating)
        res.append(movie)
        k-=1
    return res

# Follow up: Just explain the quick select method for solving this instead of using the heap.

