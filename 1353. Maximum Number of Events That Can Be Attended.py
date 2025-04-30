import heapq

def maxEvents(events):
    # events.sort()
    heapq.heapify(events)
    count = 0
    lastDay = 0
    while events:
        start, end = heapq.heappop(events)
        if lastDay < start:
            lastDay = start
            count+=1
        else:
            while lastDay >= start and start <= end:
                start+=1
            if lastDay < start:
                lastDay = start
                count += 1
    return count

print(maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]))