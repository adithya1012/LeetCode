# The developers at Amazon are working on optimizing their database query times. There are n host servers, where the throughput of the f host server is given by host_throughpuli.
# These host servers are grouped into clusters of size three. The throughput of a cluster, denoted as cluster _throughput, is defined as the median of the host throughput values of the three servers in the cluster. Each host server can be part of at most one cluster, and some servers may remain unused.
# The total system throughput, called
# system_throughput, is the sum of the throughputs of all the clusters formed. The task is to find the maximum possible system_throughput.
# Note: The median of a cluster of three host servers is the throughput of the 2nd server when the three throughputs are sorted in either ascending or descending order.

# Example
# n=5
# nost throughput = [2, 3, 4, 3, 4]
# The maximum number of clusters that can be formed is 1, and two host servers will remain unused.
# One possible cluster is to select the 1st, 3rd, and 5th host servers. The cluster _throughput of [2, 4, 4] will be 4 (the median value).
# Thus, the system_ throughput for all clusters will be 4.

# Here, n= 7, and the host throughput is given by
# host_throughput = [8, 6, 3, 4, 4, 5, 6].
# The maximum number of clusters that can be formed is 2, with one host server remaining unused
# One possible way to form the clusters is to select the 15t, 2nd , and 3rd host servers for the first cluster, and the 4th,
# 1, 6th, and 7th host servers for
# the second. The clusters _throughput of the first cluster [8, 6, 3] will be 6 (the median), and the clusters_throughput of the second cluster [4, 5,
# 6] will be 5 (the median).
# Thus, the system_throughput will be 6 + 5 = 11.


def getMaxThroughput(host_throughput):
    host_throughput.sort(reverse=True)
    no_clu = len(host_throughput)//3
    total = 0
    while no_clu:
        # print(host_throughput[no_clu - 1])
        total += host_throughput[((no_clu-1)*2)+1]
        no_clu -= 1
    return total

print(getMaxThroughput([8, 6, 3, 4, 4, 5, 6]))
print(getMaxThroughput([4,6,3,5,4,5]))
print(getMaxThroughput([2,4,3,3,4]))
print(getMaxThroughput([2,4,3]))
