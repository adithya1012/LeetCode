'''
This is the problem from the text book. finding the kth element from the last.

Iterative approach
'''

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

data = [3,1,4,2,3]
ll = create_LL(data)

k = 3 # remove the 3rd from the last element
p1 = ll
p2 = ll
for i in range(k):
    if p1.next != None:
        p1 = p1.next
print(p1.ele)
while p1:
    p1 = p1.next
    p2 = p2.next

print(p2.ele)

