from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t or s.val != t.val:
                return False
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# class Solution:
#     def isSubtree(self, root, subRoot) -> bool:
#         def dfs(node, subnode):
#             if not node and not subnode:
#                 return True
#             if node and subnode and node.val == subnode.val:
#                 if dfs(node.left, subnode.left) and dfs(node.right, subnode.right):
#                     return True
#                 else:
#                     return False
#             if not node or not subnode:
#                 return False
#             return dfs(node.left, subRoot) or dfs(node.right, subRoot)
#         return dfs(root, subRoot)

def build_tree(level_order):
    if not level_order:
        return None
    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1
    while i < len(level_order):
        node = queue.popleft()
        if level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1
    return root

# Define the trees
root_list = [3,4,5,1,2,None,None,None,None,0]
subroot_list = [4, 1, 2]

root = build_tree(root_list)
subRoot = build_tree(subroot_list)

# Run the function
solution = Solution()
print(solution.isSubtree(root, subRoot))  # Expected Output: True
