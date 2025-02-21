'''
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list,
then they are intersecting.
'''

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def LL_intersect(node1, node2):
    len1 = 0
    len2 = 0
    last1 = node1
    while last1:
        last1 = last1.next
        len1 += 1

    last2 = node2
    while last2:
        last2 = last2.next
        len2 += 1
    if last2 is not last1:
        return False
    if len1 > len2:
        diff = len1 - len2
        while diff:
            node1 = node1.next
            diff -= 1
    else:
        diff = len2 - len1
        while diff:
            node2 = node2.next
            diff -= 1

    while node1 and node2:
        if node1 is node2:
            return node1
        else:
            node1 = node1.next
            node2 = node2.next

def create_intersecting_lists():
    # Create separate nodes for the first list
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(3)

    # Create separate nodes for the second list
    head2 = ListNode(9)
    head2.next = ListNode(8)

    # Create an intersection node
    intersection = ListNode(7)
    intersection.next = ListNode(6)
    intersection.next.next = ListNode(5)

    # Attach intersection to both lists
    head1.next.next.next = intersection  # 1 -> 2 -> 3 -> 7 -> 6 -> 5
    head2.next.next = intersection       # 9 -> 8 -> 7 -> 6 -> 5

    return head1, head2, intersection

head1, head2, expected_intersection = create_intersecting_lists()

result = LL_intersect(head1, head2)

if result:
    print(f"Intersection found at node with value: {result.value}")
else:
    print("No intersection found.")

