'''
This is a text book problem.
Palindrome: Implement a function to check if a linked list is a palindrome.
'''

from LL_template import Create_LL, LL, Print_LL
def palindrom(head):
    half = []
    p1, p2 = head, head.next
    half.append(p1.val)
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        half.append(p1.val)
    if p2:
        p1 = p1.next
    half = half[::-1]
    i = 0
    Print_LL(p1)
    while p1:
        if p1.val != half[i]:
            return False
        p1 = p1.next
        i += 1
    return True

print(palindrom(Create_LL([1])))