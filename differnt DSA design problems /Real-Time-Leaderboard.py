# You are given a continuous stream of data, where each entry is a (playerId, score) tuple.
# Design a function that can, at any moment, return the top 10 players with the highest scores.
# The stream is very large, so you cannot afford to re-sort the entire dataset every time a new score comes in.


# The Practical DSA Solution: The optimal solution involves using two data structures:
# A Hash Map to store the score for each player for O(1) updates.
# A Min-Heap of size K (in this case, 10).
# When a new score arrives, you compare it to the smallest score in the heap (the root).
# If the new score is higher, you remove the root and insert the new score.
# This keeps the heap updated with the top 10 scores in O(log K) time, which is much more efficient than re-sorting everything

import collections
import heapq

class LeaderBoard:
    def __init__(self, top):
        self.heap = [] # will store top k ppl : [[score, personID]]
        self.top_winners = top
        self.players = collections.defaultdict(int) # {player1: Score, Player2: Score}
        self.current_top_k = set()

    def new_record(self, playerID, score): # hoping that everytime the score will come in the increasing order for each player.
        if playerID in self.current_top_k:
            self.heap.pop(self.heap.index([self.players[playerID], playerID])) # O(k) time complexity
            heapq.heappush(self.heap, [score, playerID])
        elif len(self.current_top_k) < self.top_winners:
            heapq.heappush(self.heap, [score, playerID])
            self.current_top_k.add(playerID)
        elif -self.heap[0][0] < score:
            old_score, old_player = heapq.heappop(self.heap)
            self.current_top_k.remove(old_player)
            heapq.heappush(self.heap, [score, playerID])
            self.current_top_k.add(playerID)

        self.players[playerID] = score

    def get_top_k(self):
        return self.heap

