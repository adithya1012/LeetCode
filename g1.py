# Given a tree of family members and their Date of birth. We have to come up with data
# structure or fuction which should output the name of member whose birthday is next from given date, the sequence should be circular.



class BinarySearch:
    # def __init__(self, array):
    #     self.birthdays = array

    def bisect_left(self, arr, bday ):
        l, r = 0, len(arr)
        while l < r:
            m = (l+r)//2
            if arr[m][0] < bday:
                l = m+1
            else:
                r = m
        return l

    def bisect_right(self, arr, bday):
        l, r = 0, len(arr)
        while l < r:
            m = (l+r)//2
            if arr[m][0] <= bday:
                l = m+1
            else:
                r = m
        return l

    def insort(self, arr, value, index):
        arr.insert(index, value)

import bisect

class Family:
    def __init__(self):
        self.birthdays = []  # [[bday, name], ...]
        self.bs = BinarySearch()

    def new_birthday(self, name: str, bday: int):
        # bisect.insort(self.birthdays, [bday, name])
        idx = self.bs.bisect_right(self.birthdays, bday)
        self.bs.insort(self.birthdays, [bday, name], idx)
        print(self.birthdays)

    def next_birthday(self, bday: int):
        # idx = bisect.bisect_right(self.birthdays, [bday, chr(127)])
        idx = self.bs.bisect_right(self.birthdays, bday)
        if idx == len(self.birthdays):
            idx = 0
        return self.birthdays[idx][1]


# fam = Family()
# fam.new_birthday("A", 5)
# fam.new_birthday("B", 6)
# fam.new_birthday("C", 7)
# fam.new_birthday("D", 4)
# fam.new_birthday("E", 1)
# fam.new_birthday("F", 2)
# fam.new_birthday("A", 5)
#
# print(fam.next_birthday(5))  # B
# print(fam.next_birthday(7))  # E
# print(fam.next_birthday(0))  # E
# print(fam.next_birthday(3))  # D

#    0,1,2,3,4,5
a = [1,1,4,4,4,7]

# For 6 -> next greater is 7
idx = bisect.bisect_right(a, 6)
print(a[idx] if idx < len(a) else None)
