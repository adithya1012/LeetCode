from collections import Counter
import heapq


def isNStraightHand(hand, groupSize):
    count = Counter(hand)

    if len(hand) % groupSize:
        return False

    heap = list(count.keys())
    heapq.heapify(heap)

    while heap:
        start = heapq.heappop(heap)
        for i in range(start, start + groupSize + 1):
            if i not in count or count[i] == 0:
                return False
            count[i] -= 1
            if i == start and count[i]:
                heapq.heappush(heap, i)
    return True

print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))