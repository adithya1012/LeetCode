# https://leetcode.com/discuss/post/6865859/amazon-online-assessment-sde2-jun-2025-b-r3nv/

# provides highly scalable solutions for applications hosted on
# their servers. A company that uses is planning to scale up its application horizontally. It needs to buy a certain number of servers from the given set of n servers provided by To ensure that adjacent servers have similar load handling capacity, they want the computational power of two adjacent servers to have a difference of 1 or less.
# Given the computational power of all the n servers as an array of integers powers, find the maximum number of servers that the client can buy such that the selected set of servers can be rearranged in a way that the absolute difference between the computational power of two adjacent servers is less than or equal to 1. The client wants to create a circular network so the first and last servers in the sequence are also considered adjacent.
# More formally, a sequence candidatel/ of length m is classified as a candidate for selection by the client if it can be rearranged in a way such that abs(candidate/il-candidate[i+1]) ≤ 1 for 0 ≤ i < m-1 and abs(candidate[m-1]-candidate[0]) ≤ 1.
# Find the maximum number of servers the client can buy from the n available servers.
# Note:
# • A subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements.
#
# Consider powers = [4, 3, 5, 1, 2, 2, 1].
# Some of the possible candidates are as follows:
# • Subsequence [1, 2, 2, 1], as abs(1-2) = 1, abs(2-2) = 0, abs(2-1) = 1, abs(1-1) = 0.
# • Subsequence [3, 1, 2, 2), as it can rearranged to [1, 2, 3, 2] and now abs(1-2) = 1, abs(2-3) = 1,
# abs(3-2) = 1, and abs(2-1) = 1.
# Some of the candidates which do not meet the client's criteria are as follows:
# • Subsequence [3, 1, 2), as no possible rearrangement will satisfy the above-mentioned condition.
# • Subsequence [4, 3, 5], as no possible rearrangement will satisfy the above-mentioned condition.
# The subsequence [3, 1, 2, 2, 1] can be rearranged to [2, 1, 1, 2, 31 and abs(2-1) = 1, abs(1-1) =
# 0, abs(1-2) = 1, abs(2-3) = 0 and abs(3-2) = 1.
# The maximum number of servers that the client can buy is 5.
# Function Description
# Complete the function getMaxServers in the editor below.
# getMaxServers has the following parameters:
# int powers[n]: computational capacity of all the n servers.



def solve(powers):
    n = len(powers)
    powers.sort()
    powers.append(-1)  # Sentinel value
    ans = 0
    left = 0
    total = 0

    for i in range(1, n + 1):
        if powers[i] == powers[left]:
            continue
        count = i - left
        total += count
        if powers[i] - powers[left] != 1 or count == 1:
            ans = max(ans, total)
            total = 1 if powers[i] - powers[left] == 1 else 0
        left = i

    return ans

# print(solve([4, 3, 5, 1, 2, 2, 1]))
# print(solve([1,2,3,4,5]))
# print(solve([4, 3, 5, 1, 2, 2, 1]))
# print(solve([1,2,3,4,3,2,1,1,1]))

print(solve([4, 3, 5, 1, 2, 2, 1]))
