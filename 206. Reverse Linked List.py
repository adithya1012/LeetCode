# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from LL_intersect import ListNode
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = None, head
        while r:
            tmp = r.next
            r.next = l
            l = r
            r = tmp
        return l