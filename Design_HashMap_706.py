class LinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hashMap = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        key_limit = key % self.size
        if not self.hashMap[key_limit]:
            self.hashMap[key_limit] = LinkedList(key, value)
        else:
            ele = self.hashMap[key_limit]
            while True:
                if ele.key == key:
                    ele.val = value
                    break
                elif ele.next == None:
                    ele.next = LinkedList(key, value)
                    break
                ele = ele.next
        # print(self.hashMap)

    def get(self, key: int) -> int:
        key_limit = key % self.size
        ele = self.hashMap[key_limit]
        if not ele:
            return -1
        while True:
            if ele.key == key:
                return ele.val
            elif ele.next == None:
                return -1
            ele = ele.next

    def remove(self, key: int) -> None:
        key_limit = key % self.size
        ele = self.hashMap[key_limit]
        if not ele:
            return

        if ele.key == key:
            self.hashMap[key_limit] = ele.next
            return
        pre = ele
        while True:
            if ele.key == key:
                pre.next = ele.next
                break
            elif ele.next == None:
                break
            pre = ele
            ele = ele.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)