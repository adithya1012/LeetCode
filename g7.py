# given a matrix with possible values [S,F, 0, 1, (any capital letter)].
#
# S- Start, F - finish, 0- can pass, 1- blockage. for the cells with capital letter, you can directly go to any cell with the same letter.
#
# Find the shortest distance to go from A to B

# Follow up: send the path also with time
import heapq
from collections import defaultdict


class Solution:
    def __init__(self, matrix):
        self.matrix = matrix
        self.special_spots, self.blocked = self.construct_teleport_spots(self.matrix)
        print(f"Special spots: {self.special_spots}")
        print(f"Blocked: {self.blocked}")

    def construct_teleport_spots(self, matrix):
        special_spots = defaultdict(set)
        blocked = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cell = matrix[i][j]
                print(f"Cell ({i},{j}): {cell}, type: {type(cell)}")
                if cell not in {1, 0, 'S', 'F'} and isinstance(cell, str) and cell.isupper():
                    special_spots[cell].add((i, j))
                    print(f"  Added to special_spots")
                if cell == 1:
                    blocked.add((i, j))
        return special_spots, blocked

    def shortest_dist(self, source, dest):
        heap = [[0, source[0], source[1]]]
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        parent = {}
        parent[(source[0], source[1])] = None
        visited = set()

        while heap:
            time, i, j = heapq.heappop(heap)
            # print(f"Pop: ({i},{j}), time={time}, value={self.matrix[i][j]}")

            if (i, j) in visited:
                # print(f"  Already visited")
                continue

            visited.add((i, j))

            if i == dest[0] and j == dest[1]:
                path = []
                current = (i, j)
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return time, path

            # Handle teleportation
            if self.matrix[i][j] in self.special_spots:
                # print(f"  Teleport available from {self.matrix[i][j]}")
                for ni, nj in self.special_spots[self.matrix[i][j]]:
                    if (ni, nj) not in visited and (ni, nj) not in parent:
                        heapq.heappush(heap, [time + 1, ni, nj])
                        parent[(ni, nj)] = (i, j)
                        # print(f"    Teleport to ({ni},{nj})")

            # Handle normal movement
            for di, dj in direction:
                ni = i + di
                nj = j + dj

                if ni < 0 or nj < 0 or ni >= len(self.matrix) or nj >= len(self.matrix[0]):
                    continue

                if (ni, nj) in self.blocked:
                    continue

                if (ni, nj) in visited:
                    continue

                if (ni, nj) not in parent:
                    heapq.heappush(heap, [time + 1, ni, nj])
                    parent[(ni, nj)] = (i, j)
                    # print(f"  Move to ({ni},{nj})")
            print(parent)

        return -1, []


# Test
matrix = [
    ['S', 0, "A"],
    ["A", 1, 0],
    [0,  0, "F"]
]

sol = Solution(matrix)
distance, path = sol.shortest_dist((0, 0), (2, 2))
print(f"\nDistance: {distance}")
print(f"Path: {path}")