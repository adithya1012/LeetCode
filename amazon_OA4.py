# In order to ensure maximum security, the developers at Amazon employ multiple encryption methods to keep user data protected.
# In one method, numbers are encrypted using a scheme called 'Pascal Triangle. When an array of digits is fed to this system, it sums the adjacent digits. It then takes the rightmost digit (least significant digit) of each addition for the next step. Thus, the number of digits in each step is reduced by 1. This procedure is repeated until there are only 2 digits left, and this sequence of 2 digits forms the encrypted number.
# Given the initial sequence of the digits of numbers, find the encrypted number. You should report a string of digits representing the encrypted number.


def encrypt(nums):
    if len(nums) in [0,1,2]:
        return nums
    while len(nums) != 2:
        tmp = []
        for i in range(len(nums)-1):
            tmp.append((nums[i]+nums[i+1])%10)
        nums = tmp
    return nums

print(encrypt([1]))
print(encrypt([1,2]))
print(encrypt([4,5]))
print(encrypt([1,2,3]))
print(encrypt([4,5,6,7]))
print(encrypt([1,2,3,4]))
