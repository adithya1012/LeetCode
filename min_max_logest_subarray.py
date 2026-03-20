from collections import deque

def longest_valid_ctr_subarray(ctrs, t):
    max_dq = deque()  # Stores indices of potential maximums
    min_dq = deque()  # Stores indices of potential minimums
    left = 0
    max_len = 0

    for right in range(len(ctrs)):
        # Maintain monotonic deques
        while max_dq and ctrs[max_dq[-1]] <= ctrs[right]:
            max_dq.pop()
        max_dq.append(right)

        while min_dq and ctrs[min_dq[-1]] >= ctrs[right]:
            min_dq.pop()
        min_dq.append(right)

        # Shrink the window if the condition ctrs[max] - ctrs[min] > t is met
        while ctrs[max_dq[0]] - ctrs[min_dq[0]] > t:
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()

        max_len = max(max_len, right - left + 1)

    return max_len

# Example usage:
ctrs = [0.1, 0.15, 0.2, 0.21, 0.19]
t = 0.05
result = longest_valid_ctr_subarray(ctrs, t) # Output: 3
print(result)