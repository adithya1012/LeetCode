import collections
import bisect


class FileSystem:

    def __init__(self):
        self.files = collections.defaultdict(str)  # Stores the contnet.
        self.paths = collections.defaultdict(list)  # Stores the ls in each path.

    def ls(self, path: str):
        if path in self.files:
            return [path.split("/")[-1]]
        return self.paths[path]

    def mkdir(self, path: str) -> None:
        curPaths = path.split("/")

        for i in range(1, len(curPaths)):
            cur = "/".join(curPaths[:i]) or "/"
            if cur not in self.paths or curPaths[i] not in self.paths[cur]:
                bisect.insort(self.paths[cur], curPaths[i])

    def addContentToFile(self, filePath: str, content: str) -> None:
        # print(self.paths)
        if filePath not in self.files:
            self.mkdir(filePath)

        self.files[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]

# Your FileSystem object will be instantiated and called as such:
obj = FileSystem()
param_1 = obj.ls("/")
obj.mkdir("/a/b/c")
obj.addContentToFile( "/a/b/c/d", "hello")
param_4 = obj.readContentFromFile("/a/b/c/d")
print(param_4)