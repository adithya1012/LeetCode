from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        nei = defaultdict(list)
        wordList.append(beginWord)

        def diff(actual_word):
            diff = 0
            res = []
            for word in wordList:
                for i in range(len(word)):
                    if word[i] != actual_word[i]:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    res.append(word)
            return res

        for word in wordList:
            nei[word] = diff(word)
        print(nei)
        q = deque([[beginWord, [beginWord]]])  # word, sequence_word
        visit = set([beginWord])
        self.res = []
        self.min_len = float("inf")

        def dfs(word, visit, lst):
            if word == endWord:
                if self.min_len > len(lst):
                    self.res = [lst.copy()]
                    self.min_len = len(lst)
                elif self.min_len == len(lst):
                    self.res.append(lst.copy())
                return
            if len(lst) >= self.min_len:
                return

            for new_word in nei[word]:
                if new_word in visit:
                    continue
                visit.add(new_word)
                lst.append(new_word)
                dfs(new_word, visit, lst)
                visit.remove(new_word)
                lst.pop()

        dfs(beginWord, {beginWord}, [beginWord])
        return self.res


print(Solution().findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))