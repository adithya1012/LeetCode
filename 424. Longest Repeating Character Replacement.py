from itertools import count


def characterReplacement(s, k):
    s = list(s)
    print()
    s.sort(key= lambda i: count(i))
    print(s)

characterReplacement("AABABBAC", 2)