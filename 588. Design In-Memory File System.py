from collections import defaultdict
import bisect

class FileSystem:

    def __init__(self):
        self.path = defaultdict(str)
        self.folder = defaultdict(list)
        # self.folder["/"] = []

    def ls(self, path: str):
        fullPath = path.split("/")
        # print(path, self.folder)
        if path in self.path:
            return [fullPath[-1]]
        return self.folder[path]

    def mkdir(self, path: str) -> None:
        fullPath = path.split("/")
        for i in range(1, len(fullPath)):
            tmpPath = "/".join(fullPath[:i]) or "/"
            if tmpPath not in self.folder or fullPath[i] not in self.folder[tmpPath]:
                bisect.insort(self.folder[tmpPath], fullPath[i])


    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.path:
            self.mkdir(filePath)
        self.path[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.path[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# print(obj.ls("/"))
# print(obj.mkdir("/a/b/c"))

a = ["", "a", "b", "c"]
for i in range(1, len(a)):
    print(a[:i])
    tmp = "/".join(a[:i]) or "/"
    print(tmp)