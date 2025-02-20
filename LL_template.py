'''
This is a template file for all the LinkedList problems.
'''

class LL:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

def Create_LL(list):
    '''
    THis is the function that will create a linked list from list
    :param list: List of values
    :return: head of the linkedlist
    '''

    head = LL()
    tmp = head

    for i in list:
        tmp.next = LL(i)
        tmp = tmp.next

    return head.next

def Print_LL(head):
    print("LinkedList: ", end=" ")
    while head:
        print(head.val, end="->")
        head = head.next


