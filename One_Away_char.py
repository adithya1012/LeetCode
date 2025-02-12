'''
This is the question from CCI book

2 strings are given and identify that is any edits happened on the second strng based on first.
there are 3 types edits allowed
Insert a char
Delete a char
Replace a char

EX:
pale,ple -> true
pales,pale -> true
pale,bale -> true
pale,bae -> false

'''

def one_char_away(str1, str2):
    if str1 == str2:
        return True
    if abs(len(str2) - len(str1)) > 1:
        return False
    update = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if update:
                return False
            if i+1 < len(str2) and str2[i+1] == str1[i]:
                str2 = str2[0:i]+str2[i+1:]
            else:
                return False
            update = True
    return True
