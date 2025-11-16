from typing import List


class UF:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self,node):
        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

    def union(self,node1, node2):
        node1_p = self.find(node1)
        node2_p = self.find(node2)

        if node1_p == node2_p:
            return
        if self.rank[node1_p] > self.rank[node2_p]:
            self.parent[node1_p] = node2_p
        elif self.rank[node2_p] > self.rank[node1_p]:
            self.parent[node2_p] = node1_p
        else:
            self.parent[node2_p] = node1_p
            self.rank[node1_p] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]):
        uf = UF(len(accounts))
        accountToIndex = {}
        print(uf.parent)
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in accountToIndex:
                    uf.union(accountToIndex[email], i)
                else:
                    accountToIndex[email] = i
        print(uf.parent)
        print(accountToIndex)


Solution().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])