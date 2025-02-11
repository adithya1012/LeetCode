'''
This is a question from CCI Book.
Given a string check if this is a permutation of a palindrome.
'''

def check_palindrome(strs):
    odd_count = 0
    count = [0]*26

    for i in strs:
        index = ord(i)-ord('a')+1
        count[index] += 1
        if count[index] % 2 != 0:
            odd_count += 1
        else:
            odd_count -= 1

    return odd_count <= 1

print(check_palindrome("abcccabbbb"))

