# from collections import defaultdict
#
#
# def maxNewConnections(user_nodes, user_from, user_to, unverified):
#     print(user_nodes, user_from, user_to, unverified)
#     unverified_set = set(unverified)
#     # Build the undirected graph; initialize all nodes.
#     graph = {i: set() for i in range(1, user_nodes + 1)}
#     for u, v in zip(user_from, user_to):
#         graph[u].add(v)
#         graph[v].add(u)
#
#     # Use DFS to find connected components.
#     visited = set()
#     components = []  # Each component will be a dict: {size, edges, has_unverified}
#
#     def dfs(node, comp_nodes):
#         visited.add(node)
#         comp_nodes.append(node)
#         for nei in graph[node]:
#             if nei not in visited:
#                 dfs(nei, comp_nodes)
#
#     for node in range(1, user_nodes + 1):
#         if node not in visited:
#             comp_nodes = []
#             dfs(node, comp_nodes)
#             # Count edges in the component (each edge counted twice in an undirected graph)
#             comp_edges = sum(len(graph[n]) for n in comp_nodes) // 2
#             comp_size = len(comp_nodes)
#             has_unverified = any(n in unverified_set for n in comp_nodes)
#             components.append({'size': comp_size, 'edges': comp_edges, 'has_unverified': has_unverified})
#
#     # Separate components: anchored (with an unverified) vs free (only verified users)
#     anchored = [comp for comp in components if comp['has_unverified']]
#     free = [comp for comp in components if not comp['has_unverified']]
#
#     # Helper: maximum number of edges in a complete graph (clique) of n nodes.
#     def clique(n):
#         return n * (n - 1) // 2
#
#     if anchored:
#         # Merge all free components with the anchored component having the largest size.
#         anchored.sort(key=lambda comp: comp['size'], reverse=True)
#         best = anchored[0]
#         free_total_size = sum(comp['size'] for comp in free)
#         free_total_edges = sum(comp['edges'] for comp in free)
#         # The merged component: best anchored component + all free components.
#         merged_size = best['size'] + free_total_size
#         # Additional edges that can be added to fully clique the merged component.
#         merged_additional = clique(merged_size) - (best['edges'] + free_total_edges)
#         # For the other anchored components (which cannot merge with one another),
#         # we can only add edges within them.
#         remaining_additional = sum(clique(comp['size']) - comp['edges'] for comp in anchored[1:])
#         return merged_additional + remaining_additional
#     else:
#         # No unverified users exist, so we can merge all components.
#         total_size = sum(comp['size'] for comp in free)
#         total_edges = sum(comp['edges'] for comp in free)
#         return clique(total_size) - total_edges
#
#
# # Sample test case
# user_nodes = 6
# user_from = [1, 1, 2, 4]
# user_to = [2, 3, 3, 5]
# unverified = [2, 4]
#
# print(maxNewConnections(user_nodes, user_from, user_to, unverified))


from collections import deque


def getQueryResults(engagementScores, query):
    n = len(engagementScores)
    d = deque(engagementScores)
    simulation = []
    for _ in range(n - 1):
        a = d.popleft()
        b = d.popleft()
        if a >= b:
            d.appendleft(a)
            d.append(b)
        else:
            d.appendleft(b)
            d.append(a)
        simulation.append([d[0], d[1]])
    max_elem = d[0]
    cycle = list(d)[1:]
    cycle_len = len(cycle)
    res = []
    for op in query:
        if op <= n - 1:
            # For queries within the simulation range, use the recorded result.
            res.append(simulation[op - 1])
        else:
            # For queries beyond n-1 operations, use the cyclic behavior.
            t = op - (n - 1)
            res.append([max_elem, cycle[t % cycle_len]])
    return res


# Example usage:
if __name__ == "__main__":
    engagementScores = [3,1,4,1,5]
    query = [6,2]
    print(getQueryResults(engagementScores, query))
    # Expected output: [[9, 6], [6, 8], [9, 8]]
