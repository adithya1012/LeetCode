# Given two arrays A and B, remove the duplicates from A which are present in B. (can be duplicates too)
# Follow up 1 : How do you maintain the order of the elements that are returned (their actual order in A)
# Follow up 2: Maintain the reverse order.


A = [5,3,6,7,1,4]
B = [3,4,5,9,8]


def remove_duplicates_6(A, B):
    b_set = set(B)
    write_idx = 0

    for read_idx in range(len(A)):
        if A[read_idx] not in b_set:
            A[write_idx] = A[read_idx]
            write_idx += 1

    # Trim the array
    return A[:write_idx]
