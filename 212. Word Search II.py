
def findWords(board, words):
    matching_words = set(words)
    result = set()
    visit = set()
    def dfs(word, mw, i, j):
        if word in mw:
            result.add(word)
            mw.remove(word)
        if min(i,j) < 0 or i == len(board) or j == len(board[0]) or (i,j) in visit:
            return
        visit.add((i,j))
        word += board[i][j]
        l = len(word)-1
        nmw = set()
        for newword in mw:
            if l >= len(newword):
                continue
            if newword[l] == board[i][j]:
                nmw.add(newword)
        if nmw:
            dfs(word, nmw, i+1, j)
            dfs(word, nmw, i-1, j)
            dfs(word, nmw, i, j+1)
            dfs(word, nmw, i, j-1)
    for i in range(len(board)):
        for j in range(len(board[0])):
            visit = set()
            print(matching_words - result)
            dfs("", matching_words-result, i,j)
    return list(result)

print(findWords([["a","b","c","e"],
                        ["x","x","c","d"],
                        ["x","x","b","a"]], ["abc","abcd"]))
