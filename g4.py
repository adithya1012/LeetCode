# Q: We have given list of a pair of strings. Each pair of string has exactly 1 character mismatch in them.
# we can assume that the character which are mismatched have parent -> child relation and can from chain of multiple characters.
# Eg. ('abc','abe') -> Parent ->child :: c->e
# Eg. ('abe','abf') -> Parent ->child :: c->e->f
# Form list of these pairs we would get chains of characters.
# We have to find the lenght of the longest such chain. It is given that the 1 chracter would have only 1 parent and 1 child.

# Follow Up: Now from the pairs of strings we can form the Polytree ( tree with multiple child , multiple parents). We have to find length of longest chain.

from collections import defaultdict


class Solution:
    def __init__(self, pairs):
        self.pairs = pairs
        self.graph, self.in_degree = self.construct_graph(pairs)

    def construct_graph(self, pairs):
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for parent, child in pairs:
            for i in range(len(child)):
                if child[i] != parent[i]:
                    parent_char = parent[i]
                    child_char = child[i]

                    graph[parent_char].append(child_char)
                    in_degree[child_char] += 1

                    # Ensure parent is in in_degree map (with 0 if no parents)
                    if parent_char not in in_degree:
                        in_degree[parent_char] = 0
                    break

        return graph, in_degree

    def find_long_chain(self):
        dp = {}

        def dfs(node):
            if node in dp:
                return dp[node]

            # Base case: if no children, length is 1
            if node not in self.graph or len(self.graph[node]) == 0:
                return 1

            max_length = 0
            for child in self.graph[node]:  # ✅ Iterate over children of current node
                max_length = max(max_length, dfs(child))

            dp[node] = 1 + max_length
            return dp[node]

        # Find all root nodes (nodes with in_degree 0)
        roots = [node for node in self.in_degree if self.in_degree[node] == 0]

        # If no roots found, there might be a cycle or empty graph
        if not roots:
            return 0

        # Find maximum chain length starting from any root
        max_chain = 0
        for root in roots:
            max_chain = max(max_chain, dfs(root))

        return max_chain


# Test
pairs = [
    ('abc', 'abe'),  # c → e
    ('abe', 'abf'),  # e → f
    ('xyz', 'xya'),  # z → a
]

sol = Solution(pairs)
print(sol.find_long_chain())  # Should print 3 (c → e → f)