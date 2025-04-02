from typing import List

def canFinish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)  # Build adjacency list

    visited = set()  # Tracks nodes in the current recursion stack
    checked = set()  # Tracks nodes that are cycle-free

    def dfs(course):
        if course in checked:
            return True  # Already verified as cycle-free
        if course in visited:
            return False  # Cycle detected

        visited.add(course)  # Mark as visiting
        for prereq in graph[course]:
            if not dfs(prereq):
                return False  # Cycle found

        visited.remove(course)  # Remove after recursion finishes
        checked.add(course)  # Mark as cycle-free
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False  # If any course is in a cycle, return False

    return True  # If all courses pass, return True

print(canFinish(2, [[1,0]]))