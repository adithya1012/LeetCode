
def isPalindrome(s):
    i, j = 0, len(s)-1
    while i<j:
        i_lower = s[i].lower()
        # print(s[i], s[j])
        if not (97 <= ord(i_lower) <= 122):
            while i+1<=j and (not (97 <= ord(i_lower) <= 122)):
                i += 1
                i_lower = s[i].lower()
            # if i>j:
            #     print("here 1")
            #     print(i, j)
            #     return False
        j_lower = s[j].lower()
        if not (97 <= ord(j_lower) <= 122):
            while i+1<=j and (not (97 <= ord(j_lower) <= 122)):
                j -= 1
                j_lower = s[j].lower()
            # if i>j:
            #     print(s[:i + 1])
            #     print(s[j:])
            #     print(i, j)
            #     print("here 2")
            #     return False
        if i == j:
            return True
        if i_lower == j_lower and (97 <= ord(j_lower) <= 122) and (97 <= ord(i_lower) <= 122):
            i+=1
            j-=1
        else:
            print(s[:i+1])
            print(s[j:])
            print("here 3")
            return False
    return True


print(isPalindrome(".,"))