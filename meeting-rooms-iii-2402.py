import heapq

def mostBooked(n, meetings):

    end_meeting = [float("inf")] * n
    available = [True] * n
    count = [0] * n
    time = 0
    heapq.heapify(meetings)
    while meetings:
        start, end = heapq.heappop(meetings)
        if time in end_meeting:
            for i, val in enumerate(end_meeting):
                if val == time:
                    end_meeting[i] = float("inf")
                    available[i] = True
        if any(available):
            for i, val in enumerate(available):
                if val:
                    available[i] = False
                    end_meeting[i] = end
                    count[i] += 1
                    break
        else:
            time = min(end_meeting)
            index = end_meeting.index(time)
            available[index] = False
            count[index] += 1
            end_meeting[index] = end+time
            time -= 1
        time += 1
    return count.index(max(count))

print(mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))
