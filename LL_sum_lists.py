'''
This is a TextBook Problem

Sum Lists: You have two numbers represented by a linked list,where each node contains a single digit. The digits are stored in reverse order,such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. Output:2 -> 1 -> 9.Thatis,912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295. Output:9 ->1 ->2.Thatis,912.
'''

from LL_template import LL, Create_LL, Print_LL
def sum_list_reverse(node1, node2):
    # Print_LL(node1)
    sum_val = 0
    digit = 1
    while node1 and node2:
        sum_val += (node1.val + node2.val)*digit
        digit *= 10
        node1 = node1.next
        node2 = node2.next
    while node1:
        sum_val += (node1.val) * digit
        node1 = node1.next
        digit *= 10
    while node2:
        sum_val += (node2.val) * digit
        node2 = node2.next
        digit *= 10
    print(sum_val)


def sum_list_forward(node1, node2):
    sum_val = 0
    digit = 1
    while node1 and node2:
        sum_val *= 10
        sum_val += (node1.val + node2.val)
        # digit *= 10
        node1 = node1.next
        node2 = node2.next
    while node1:
        sum_val *= 10
        sum_val += (node1.val) * digit
        node1 = node1.next
    while node2:
        sum_val *= 10
        sum_val += (node2.val) * digit
        node2 = node2.next
    print(sum_val)

'''
These is another approach of solving this by keeping a carry
'''

sum_list_forward(Create_LL([1,2,3]), Create_LL([1,1]))