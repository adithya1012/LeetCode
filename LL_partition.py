'''
This is a textbook problem.

given a number partition the LL in such a way that it will divide the lower than partition value left side and more than
the partition value on the right side
'''

from LL_template import LL, Create_LL, Print_LL


def partition(head: LL, x: int) -> LL:
    left_head = left = LL(0)  # Dummy node for left partition
    right_head = right = LL(0)  # Dummy node for right partition
    equal = equal_head = LL(0)
    while head:
        if head.val < x:
            left.next = head  # Add to left partition
            left = left.next
        elif head.val == x:
            equal.next = head
            equal = equal.next
        else:
            right.next = head  # Add to right partition
            right = right.next
        head = head.next  # Move to next node

    right.next = None  # Prevent cycle in linked list
    left.next = equal_head.next  # Merge the two partitions
    equal.next = right_head.next

    return left_head.next

Print_LL(partition(Create_LL([1,8,5,10,3,2,1,5]), 5))

