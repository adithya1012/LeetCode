import unittest
class LinkedList:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


class Test(unittest.TestCase):
    # def __init__(self, *args):
    #     super.__init__(*args)
    #     pass

    def create_LL(self, lst, val):
        head = LinkedList()
        dummy = head
        node = None
        for i in lst:
            tmp = LinkedList(i)
            head.next = tmp
            if tmp.val == val:
                node = tmp
            head = head.next
        return dummy.next, node


    def LL_to_list(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res


    def test_removeBeginning(self):
        lst = [1, 2, 3, 4]
        val = 1
        output = [2, 3, 4]
        head, node = self.create_LL(lst, val)
        solution = Solution()
        solution.deleteNode(node)
        result = self.LL_to_list(head)
        if result == output:
            print("Testcase Passes")
            return True
        else:
            print(f" Testcase Failed: For {node.val} Returned {result} Expected: {output}")
            return False


    def test_removeEnd(self):
        lst = [1, 2, 3, 4]
        val = 3
        output = [1, 2, 4]
        head, node = self.create_LL(lst, val)
        solution = Solution()
        solution.deleteNode(node)
        result = self.LL_to_list(head)
        if result == output:
            print("Testcase Passes")
            return True
        else:
            print(f" Testcase Failed: For {node.val} Returned {result} Expected: {output}")
            return False


    def test_removeMiddle(self):
        lst = [1, 2, 3, 4]
        val = 2
        output = [1, 3, 4]
        head, node = self.create_LL(lst, val)
        solution = Solution()
        solution.deleteNode(node)
        result = self.LL_to_list(head)


        if result == output:
            print("Beginning Testcase Passes")
            return True
        else:
            print(f"Testcase Failed: For {node.val} Returned {result} Expected: {output}")
            return False

if __name__ == "__main__":
    failed = 0
    passed = 0
    test = Test()
    if test.test_removeBeginning():
        passed += 1
    else:
        failed += 1

    if test.test_removeEnd():
        passed += 1
    else:
        failed += 1

    if test.test_removeMiddle():
        passed += 1
    else:
        failed += 1

    print(f"Failed: {failed} and Passed: {passed}")
