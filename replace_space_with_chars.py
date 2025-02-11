'''
This is a question from CCI Book.

Build URL: Replace all the spaces with '%20'. Operation should be inplace.

'''

# def space_replace(strs):
#     index = []
#     for i in range(len(strs)):
#         if strs[i] == " ":
#             index.append(i)
#     for i in reversed(index):
#         strs[i] = "%20"
#     return strs


'''
Seems like python strings are immutable and it is throwing error. LOL'''
def space_replace(strs):
    return strs.replace(" ", "%20")



print(space_replace("This is something   ."))