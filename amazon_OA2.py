# Amazon ships millions of parcels to customers across the globe every day.
# In a given center, n types of products are to be shipped where the number of parcels of product type /is denoted by quantityli]. A truck can carry a maximum capacity number of parcels, with no more than max_parcels_of_same_type parcels of the same type. Find the minimum number of trucks needed to ship all parcels of all types from this center.
# Example
# Consider the number of types of products is n = 2, the quantity of each product type is quantity = [2, 4], the
# truck capacity is capacity = 3, and the maximum allowed quantity of a product type
# is max_parcels_of_same_type = 2.
#
# A truck cannot carry 3 parcels of type 2 since only max_parcels_of_same_type = 2 of any one type can be on a
# truck. All parcels can be shipped in 2 trucks without violating any constraints. The answer is 2.
#
# Explanation
# Here quantity = [3, 2, 2, 6], capacity = 2, and max_parcels_of same_type = 1.
# • Truck No. 1 = 1 product of type 1 and 1 of type 4.
# • Truck No. 2 = 1 product of type 1 and 1 of type 4.
# • Truck No. 3 = 1 product of type 1 and 1 of type 4.
# • Truck No. 4 = 1 product of type 2 and 1 of type 4.
# • Truck No. 5 = 1 product of type 2 and 1 of type 4.
# • Truck No. 6 = 1 product of type 3 and 1 of type 4.
# • Truck No. 7 = Isproduct of type 3.

import heapq

import heapq

def NoofTrucks(quantity, capacity, max_parcels_of):
    # Queue to hold leftover quantities to be reprocessed
    q = []

    # Convert quantity list into a max-heap (using negative values)
    heap = [-i for i in quantity]
    heapq.heapify(heap)

    truck = 0  # Truck counter

    # Helper to push all elements from q back into heap
    def copyquantity(heap, q):
        for i in q:
            heapq.heappush(heap, -i)

    cur_cap = capacity  # Remaining space in current truck

    while heap or q:
        if not heap:
            # Start a new truck if heap is empty but q has remainders
            truck += 1
            copyquantity(heap, q)
            q = []
            cur_cap = capacity
            # continue  # Go to next loop iteration

        # Get the Highest qunatity
        quan = -heapq.heappop(heap)
        if not quan:
            continue
        if quan > max_parcels_of:
            rem = quan - max_parcels_of
            quan = max_parcels_of

            if quan > cur_cap:
                # Not enough space even for the reduced quantity
                rem += quan - cur_cap  # combine both leftover pieces
                q.append(rem)
                truck += 1
                copyquantity(heap, q)
                q = []
                cur_cap = capacity
            else:
                # Add the leftover and fill partially
                cur_cap -= quan
                q.append(rem)
        else:
            if quan > cur_cap:
                rem = quan - cur_cap
                truck += 1
                copyquantity(heap, q + [rem])
                q = []
                cur_cap = capacity
            else:
                cur_cap -= quan

    # Account for the last truck if it was partially filled
    if cur_cap < capacity:
        truck += 1

    return truck

# print(NoofTrucks([3,2,2,6], 2, 1))

import math

def minTruck(qunatity, cap, k):
    min_truck_cap = math.ceil(sum(qunatity)/cap)
    min_truck_type_limit = 0
    for q in qunatity:
        min_truck_type_limit = max(min_truck_type_limit, math.ceil(q/k))
    return max(min_truck_cap, min_truck_type_limit)

print(minTruck([3,2,2,6], 2, 1))