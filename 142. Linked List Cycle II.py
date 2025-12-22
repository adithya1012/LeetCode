# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = [x]
        self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         seen = set()
#
#         while head:
#             if head in seen:
#                 return head
#             seen.add(head)
#             head = head.next
#
#         return None

node1 = ListNode(5)
node2 = ListNode(5)

print(node1 == node2)   # False
print(hash(node1) != hash(node2))

node1Hast = hash(node1)
node2.val.append(4)
node1Hast_modified = hash(node1)
print(node1Hast, node1Hast_modified)






