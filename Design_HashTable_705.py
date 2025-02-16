class MyHashSet:

    def __init__(self):
        self.size = 10
        self.hashset = [[None]]* self.size

    def add(self, key: int) -> None:
        # if not self.contains(key):
        val = self.hash(key)
        if self.hashset[val] == None:
            self.hashset[val] = [key]
        else:
            self.hashset[val].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            val = self.hash(key)
            index = -1
            for i,j in enumerate(self.hashset[val]):
                if j == key:
                    index = i
                    break
            self.hashset[val].remove(index)

    def contains(self, key: int) -> bool:
        val = self.hash(key)
        if self.hashset[val] == None:
            return False
        else:
            for i in self.hashset[val]:
                if i == key:
                    return True
            return False

    def hash(self, key):
        return key*12345%self.size-1


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.remove(1)
param_3 = obj.contains(1)
print(param_3)