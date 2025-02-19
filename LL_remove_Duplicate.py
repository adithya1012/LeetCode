"""
Write a code for removing duplicate from the LinkedList

FollowUP:
Do not use the additional Buffer storage.
"""


class LinkedList:
    def __init__(self, ele = -1, next = None):
        self.ele = ele
        self.next = next

def create_LL(LL_list):
    head = LinkedList()
    tmp = head
    for i in LL_list:
        head.next = LinkedList(i)
        head = head.next
    head = tmp.next
    return head

def LL_remove_duplicate(ll):
    ele = set()
    prev = LinkedList(-1,ll)
    tmp = prev
    head = ll
    while head:
        if head.ele in ele:
            prev.next = head.next
        else:
            ele.add(head.ele)
            prev = prev.next
        head = head.next
    return tmp.next


def print_ll(ll):
    while ll:
        print(ll.ele)
        ll = ll.next

data = [3,1,4,2,3]
ll = create_LL(data)

# print_ll(ll)

ll_update = LL_remove_duplicate(ll)

print_ll(ll_update)