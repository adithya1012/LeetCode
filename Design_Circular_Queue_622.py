class LinkedList:
    def __init__(self, val=None, nextVal=None):
        self.val = val
        self.next = nextVal

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.head = LinkedList()
        dummy = self.head
        tmp = self.head
        for i in range(k):
            tmp.val = i
            tmp.next = LinkedList()
            tmp = tmp.next
        tmp.next = dummy
        self.head = dummy
        self.tail = dummy


    def enQueue(self, value: int) -> bool:
        if (self.isFull()):
            print(self.head.val)
            return False
        self.tail.val = value
        self.tail = self.tail.next
        return True

    def deQueue(self) -> bool:
        if (self.isEmpty()):
            return False
        val = self.head.val
        self.head.val = None
        self.head = self.head.next
        return True

    def Front(self) -> int:
        if self.head == self.tail:
            return -1
        return self.tail.val

    def Rear(self) -> int:
        if self.head == self.tail:
            return -1
        return self.head.val

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        print(self.head == self.tail.next)
        return self.head == self.tail.next


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()